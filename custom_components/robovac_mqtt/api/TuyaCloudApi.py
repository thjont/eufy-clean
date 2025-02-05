import logging

from ..lib.TuyaCloud import TuyaCloud

_LOGGER = logging.getLogger(__name__)


class TuyaCloudApi:
    def __init__(self, username: str, password: str, user_id: str, region: str):
        self.username = username
        self.password = password
        self.user_id = user_id

        _LOGGER.debug('TuyaCloudApi', {'region': region})

        self.tuya_cloud = TuyaCloud(dict(
            key='yx5v9uc3ef9wg3v9atje',
            secret='s8x78u7xwymasd9kqa7a73pjhxqsedaj',
            secret2='cepev5pfnhua4dkqkdpmnrdxx378mpjr',
            certSign='A',
            apiEtVersion='0.0.1',
            region=region,
            ttid='android',
        ))

    async def login(self) -> str:
        sid = await self.tuya_cloud.login_ex(dict(
            email=self.username,
            password=self.password,
            uid=self.user_id,
            return_full_login_response='false'
        ))
        _LOGGER.debug('Logged in to Tuya Cloud', {'sid': sid})
        return sid

    async def get_device_list(self) -> list:
        groups = await self.tuya_cloud.request(action='tuya.m.location.list')
        for group in groups:
            devices = await self.tuya_cloud.request(action='tuya.m.my.group.device.list', gid=group['groupId'])
            shared_devices = await self.tuya_cloud.request(action='tuya.m.my.shared.device.list')

            print(f'Found {len(devices)} devices and {len(shared_devices)} sharedDevices via Tuya Cloud')

            return devices + shared_devices

    async def get_device(self, device_id: str) -> dict:
        groups = await self.tuya_cloud.request(action='tuya.m.location.list')
        for group in groups:
            devices = await self.tuya_cloud.request(action='tuya.m.my.group.device.list', gid=group['groupId'])
            shared_devices = await self.tuya_cloud.request(action='tuya.m.my.shared.device.list')

            return next((device for device in devices + shared_devices if device['devId'] == device_id), None)

    async def send_command(self, device_id: str, dps: dict) -> None:
        print(f'Sending command to device {device_id}', {'action': 'tuya.m.device.dp.publish', 'deviceID': device_id, 'data': dps})
        await self.tuya_cloud.request(action='tuya.m.device.dp.publish', deviceID=device_id, data={'dps': dps, 'devId': device_id, 'gwId': device_id})
