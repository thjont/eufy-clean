# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/cloud/scene.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...proto.cloud import \
    clean_param_pb2 as proto_dot_cloud_dot_clean__param__pb2
from ...proto.cloud import common_pb2 as proto_dot_cloud_dot_common__pb2
from ...proto.cloud import timing_pb2 as proto_dot_cloud_dot_timing__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17proto/cloud/scene.proto\x12\x0bproto.cloud\x1a\x18proto/cloud/common.proto\x1a\x1dproto/cloud/clean_param.proto\x1a\x18proto/cloud/timing.proto\"\x8f\x08\n\tSceneTask\x12\r\n\x05index\x18\x01 \x01(\r\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.proto.cloud.SceneTask.Type\x12:\n\x0c\x63urrent_room\x18\x03 \x01(\x0b\x32\".proto.cloud.SceneTask.CurrentRoomH\x00\x12\x34\n\tall_rooms\x18\x04 \x01(\x0b\x32\x1f.proto.cloud.SceneTask.AllRoomsH\x00\x1a\xc1\x01\n\x07General\x12*\n\nclean_type\x18\x01 \x01(\x0b\x32\x16.proto.cloud.CleanType\x12\x13\n\x0b\x63lean_times\x18\x02 \x01(\r\x12\x1d\n\x03\x66\x61n\x18\x03 \x01(\x0b\x32\x10.proto.cloud.Fan\x12&\n\x08mop_mode\x18\x04 \x01(\x0b\x32\x14.proto.cloud.MopMode\x12.\n\x0c\x63lean_extent\x18\x05 \x01(\x0b\x32\x18.proto.cloud.CleanExtent\x1a\xce\x03\n\x0b\x43urrentRoom\x12.\n\x04mode\x18\x01 \x01(\x0e\x32 .proto.cloud.SceneTask.CleanMode\x12\x36\n\x05units\x18\x02 \x03(\x0b\x32\'.proto.cloud.SceneTask.CurrentRoom.Unit\x1a\xd6\x02\n\x04Unit\x12/\n\x07general\x18\x01 \x01(\x0b\x32\x1e.proto.cloud.SceneTask.General\x12G\n\nroom_clean\x18\x02 \x01(\x0b\x32\x31.proto.cloud.SceneTask.CurrentRoom.Unit.RoomCleanH\x00\x12G\n\nzone_clean\x18\x03 \x01(\x0b\x32\x31.proto.cloud.SceneTask.CurrentRoom.Unit.ZoneCleanH\x00\x1aH\n\tRoomClean\x12\x0f\n\x07room_id\x18\x01 \x01(\r\x12*\n\nroom_scene\x18\x02 \x01(\x0b\x32\x16.proto.cloud.RoomScene\x1a\x38\n\tZoneClean\x12+\n\nquadrangle\x18\x01 \x01(\x0b\x32\x17.proto.cloud.QuadrangleB\x07\n\x05Param\x1ak\n\x08\x41llRooms\x12.\n\x04mode\x18\x01 \x01(\x0e\x32 .proto.cloud.SceneTask.CleanMode\x12/\n\x07general\x18\x02 \x01(\x0b\x32\x1e.proto.cloud.SceneTask.General\"\'\n\x04Type\x12\x10\n\x0c\x43URRENT_ROOM\x10\x00\x12\r\n\tALL_ROOMS\x10\x01\"#\n\tCleanMode\x12\x0b\n\x07GENERAL\x10\x00\x12\t\n\x05SMART\x10\x01\x42\x06\n\x04Task\"\x80\x04\n\tSceneInfo\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.proto.cloud.SceneInfo.Id\x12\r\n\x05valid\x18\x02 \x01(\x08\x12<\n\x0einvalid_reason\x18\x03 \x01(\x0e\x32$.proto.cloud.SceneInfo.InvalidReason\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\r\n\x05mapid\x18\x05 \x01(\r\x12\x15\n\restimate_time\x18\x06 \x01(\r\x12\r\n\x05index\x18\x07 \x01(\r\x12)\n\x04type\x18\x08 \x01(\x0e\x32\x1b.proto.cloud.SceneInfo.Type\x1a\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\r\"p\n\rInvalidReason\x12\n\n\x06NORMAL\x10\x00\x12\x11\n\rMAP_NOT_EXIST\x10\x01\x12\x15\n\x11MAP_NOT_AVAILABLE\x10\x02\x12\x11\n\rMAP_NOT_MATCH\x10\x03\x12\t\n\x05OTHER\x10\x04\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x05\"\x89\x01\n\x04Type\x12\x10\n\x0cSCENE_NORMAL\x10\x00\x12\x1e\n\x1aWHOLE_HOUSE_DAILY_CLEANING\x10\x01\x12\x1d\n\x19WHOLE_HOUSE_DEEP_CLEANING\x10\x02\x12\x19\n\x15\x41\x46TER_DINNER_CLEANING\x10\x03\x12\x15\n\x11PET_AREA_CLEANING\x10\x04\"\xa3\x03\n\x0cSceneRequest\x12\x30\n\x06method\x18\x01 \x01(\x0e\x32 .proto.cloud.SceneRequest.Method\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x32\n\x06\x63ommon\x18\x03 \x01(\x0b\x32 .proto.cloud.SceneRequest.CommonH\x00\x12\x30\n\x05scene\x18\x04 \x01(\x0b\x32\x1f.proto.cloud.SceneRequest.SceneH\x00\x1a\x1a\n\x06\x43ommon\x12\x10\n\x08scene_id\x18\x01 \x01(\r\x1a\x7f\n\x05Scene\x12$\n\x04info\x18\x01 \x01(\x0b\x32\x16.proto.cloud.SceneInfo\x12%\n\x05tasks\x18\x02 \x03(\x0b\x32\x16.proto.cloud.SceneTask\x12)\n\x04\x64\x65sc\x18\x03 \x01(\x0b\x32\x1b.proto.cloud.TimerInfo.Desc\"H\n\x06Method\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\r\n\tADD_SCENE\x10\x01\x12\x10\n\x0c\x44\x45LETE_SCENE\x10\x02\x12\x10\n\x0cMODIFY_SCENE\x10\x03\x42\x07\n\x05Param\"\x9e\x02\n\rSceneResponse\x12\x30\n\x06method\x18\x01 \x01(\x0e\x32 .proto.cloud.SceneRequest.Method\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x31\n\x06result\x18\x03 \x01(\x0b\x32!.proto.cloud.SceneResponse.Result\x12%\n\x05infos\x18\x04 \x03(\x0b\x32\x16.proto.cloud.SceneInfo\x1at\n\x06Result\x12\x36\n\x05value\x18\x01 \x01(\x0e\x32\'.proto.cloud.SceneResponse.Result.Value\x12\x10\n\x08\x65rr_code\x18\x02 \x01(\r\" \n\x05Value\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.cloud.scene_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCENETASK._serialized_start=124
  _SCENETASK._serialized_end=1163
  _SCENETASK_GENERAL._serialized_start=310
  _SCENETASK_GENERAL._serialized_end=503
  _SCENETASK_CURRENTROOM._serialized_start=506
  _SCENETASK_CURRENTROOM._serialized_end=968
  _SCENETASK_CURRENTROOM_UNIT._serialized_start=626
  _SCENETASK_CURRENTROOM_UNIT._serialized_end=968
  _SCENETASK_CURRENTROOM_UNIT_ROOMCLEAN._serialized_start=829
  _SCENETASK_CURRENTROOM_UNIT_ROOMCLEAN._serialized_end=901
  _SCENETASK_CURRENTROOM_UNIT_ZONECLEAN._serialized_start=903
  _SCENETASK_CURRENTROOM_UNIT_ZONECLEAN._serialized_end=959
  _SCENETASK_ALLROOMS._serialized_start=970
  _SCENETASK_ALLROOMS._serialized_end=1077
  _SCENETASK_TYPE._serialized_start=1079
  _SCENETASK_TYPE._serialized_end=1118
  _SCENETASK_CLEANMODE._serialized_start=1120
  _SCENETASK_CLEANMODE._serialized_end=1155
  _SCENEINFO._serialized_start=1166
  _SCENEINFO._serialized_end=1678
  _SCENEINFO_ID._serialized_start=1405
  _SCENEINFO_ID._serialized_end=1424
  _SCENEINFO_INVALIDREASON._serialized_start=1426
  _SCENEINFO_INVALIDREASON._serialized_end=1538
  _SCENEINFO_TYPE._serialized_start=1541
  _SCENEINFO_TYPE._serialized_end=1678
  _SCENEREQUEST._serialized_start=1681
  _SCENEREQUEST._serialized_end=2100
  _SCENEREQUEST_COMMON._serialized_start=1862
  _SCENEREQUEST_COMMON._serialized_end=1888
  _SCENEREQUEST_SCENE._serialized_start=1890
  _SCENEREQUEST_SCENE._serialized_end=2017
  _SCENEREQUEST_METHOD._serialized_start=2019
  _SCENEREQUEST_METHOD._serialized_end=2091
  _SCENERESPONSE._serialized_start=2103
  _SCENERESPONSE._serialized_end=2389
  _SCENERESPONSE_RESULT._serialized_start=2273
  _SCENERESPONSE_RESULT._serialized_end=2389
  _SCENERESPONSE_RESULT_VALUE._serialized_start=2357
  _SCENERESPONSE_RESULT_VALUE._serialized_end=2389
# @@protoc_insertion_point(module_scope)
