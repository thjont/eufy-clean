import asyncio
import hashlib
import hmac
import json
import random
import string
import time
import uuid

import aiohttp
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad


class TuyaCloudRequestError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


class TuyaCloud:
    def __init__(self, options):
        if not options.get('key') or not options.get('secret') or len(options['key']) != 20 or len(options['secret']) != 32:
            raise ValueError('Invalid format for key or secret.')
        self.key = options['key']
        self.secret = options['secret']
        self.apiEtVersion = options.get('apiEtVersion')
        self.ttid = options.get('ttid', 'tuya')
        self.deviceID = options.get('deviceID', ''.join(random.choices(string.ascii_lowercase + string.digits, k=44)))
        self.endpoint = options.get('endpoint')
        self.region = options.get('region', 'AZ')
        self.sid = options.get('sid')

        if self.apiEtVersion:
            self.keyHmac = f"{options['certSign']}_{options['secret2']}_{self.secret}"

        if not self.endpoint:
            if self.region == 'AZ':
                self.endpoint = 'https://a1.tuyaus.com/api.json'
            elif self.region == 'AY':
                self.endpoint = 'https://a1.tuyacn.com/api.json'
            elif self.region == 'EU':
                self.endpoint = 'https://a1.tuyaeu.com/api.json'
            elif self.region == 'IN':
                self.endpoint = 'https://a1.tuyain.com/api.json'
            else:
                raise ValueError('Bad region identifier.')

    def _mobile_hash(self, data):
        pre_hash = hashlib.md5(data.encode()).hexdigest()
        return pre_hash[8:16] + pre_hash[0:8] + pre_hash[24:32] + pre_hash[16:24]

    async def request(self, options):
        if not options.get('action'):
            raise ValueError('Must specify an action to call.')
        if not self.sid and options.get('requiresSID', True):
            raise ValueError('Must call login() first.')

        d = int(time.time())
        pairs = {
            'a': options['action'],
            'deviceId': self.deviceID,
            'sdkVersion': '3.0.0cAnker',
            'os': 'Android',
            'lang': 'en',
            'appVersion': '2.3.2',
            'v': options.get('version', '1.0'),
            'clientId': self.key,
            'time': d,
        }

        if options.get('data'):
            pairs['postData'] = json.dumps(options['data'])
        if options.get('gid'):
            pairs['gid'] = options['gid']
        if self.apiEtVersion:
            pairs.update({
                'et': self.apiEtVersion,
                'ttid': self.ttid,
                'appVersion': '3.8.5',
                'appRnVersion': '5.11',
                'platform': 'Android',
                'requestId': str(uuid.uuid4())
            })
        if options.get('requiresSID', True):
            pairs['sid'] = self.sid

        values_to_sign = [
            'a', 'v', 'lat', 'lon', 'lang', 'deviceId', 'imei', 'imsi', 'appVersion', 'ttid', 'isH5', 'h5Token', 'os',
            'clientId', 'postData', 'time', 'requestId', 'n4h5', 'sid', 'sp', 'et'
        ]

        sorted_pairs = dict(sorted(pairs.items()))
        str_to_sign = '||'.join(f"{k}={self._mobile_hash(v) if k == 'postData' else v}" for k, v in sorted_pairs.items() if k in values_to_sign and v)

        if self.apiEtVersion:
            pairs['sign'] = hmac.new(self.keyHmac.encode(), str_to_sign.encode(), hashlib.sha256).hexdigest()
        else:
            str_to_sign += f"||{self.secret}"
            pairs['sign'] = hashlib.md5(str_to_sign.encode()).hexdigest()

        async with aiohttp.ClientSession() as session:
            async with session.get(self.endpoint, params=pairs, timeout=10) as response:
                data = await response.json()

        if not data.get('success'):
            raise TuyaCloudRequestError(data['errorCode'], data['errorMsg'])

        return data['result']

    async def register(self, options):
        try:
            api_result = await self.request({
                'action': 'tuya.m.user.email.register',
                'data': {'countryCode': self.region, 'email': options['email'], 'passwd': hashlib.md5(options['password'].encode()).hexdigest()},
                'requiresSID': False,
            })
            self.sid = api_result['sid']
            return self.sid
        except TuyaCloudRequestError as err:
            if err.code == 'USER_NAME_IS_EXIST':
                return await self.login(options)
            raise

    async def login(self, options):
        api_result = await self.request({
            'action': 'tuya.m.user.email.password.login',
            'data': {'countryCode': self.region, 'email': options['email'], 'passwd': hashlib.md5(options['password'].encode()).hexdigest()},
            'requiresSID': False,
        })
        self.sid = api_result['sid']
        if options.get('returnFullLoginResponse'):
            return api_result
        return self.sid

    async def login_ex(self, options):
        token = await self.request({
            'action': 'tuya.m.user.uid.token.create',
            'data': {'countryCode': self.region, 'uid': f"eh-{options['uid']}"},
            'requiresSID': False,
        })

        key = RSA.construct((int(token['publicKey'], 16), int(token['exponent'])))
        cipher = AES.new(b'$N\x6d\x8aV\xac\x87\x91$C-\x8bl\xbc\xa2\xc4', AES.MODE_CBC, b'w$V\xf2\xa7fL\xf39,5\x97\xe9>WG')
        filleduid = pad(f"eh-{options['uid']}".encode(), AES.block_size)
        encrypted = cipher.encrypt(filleduid).hex().upper()
        encrypted_pass = key.encrypt(hashlib.md5(encrypted.encode()).digest(), 32)[0].hex()

        api_result = await self.request({
            'action': 'tuya.m.user.uid.password.login',
            'data': {
                'countryCode': self.region,
                'uid': f"eh-{options['uid']}",
                'createGroup': True,
                'passwd': encrypted_pass,
                'ifencrypt': 1,
                'options': {'group': 1},
                'token': token['token'],
            },
            'requiresSID': False,
        })

        if api_result['domain']['mobileApiUrl'] and not self.endpoint.startswith(api_result['domain']['mobileApiUrl']):
            self.endpoint = f"{api_result['domain']['mobileApiUrl']}/api.json"
            self.region = api_result['domain']['regionCode']

        self.sid = api_result['sid']
        if options.get('returnFullLoginResponse'):
            return api_result
        return self.sid

    async def wait_for_token(self, options):
        devices = options.get('devices', 1)
        for _ in range(200):
            try:
                token_result = await self.request({'action': 'tuya.m.device.list.token', 'data': {'token': options['token']}})
                if len(token_result) >= devices:
                    return token_result
                await asyncio.sleep(0.2)
            except Exception as err:
                raise err
        raise TimeoutError('Timed out waiting for device(s) to connect to cloud')
