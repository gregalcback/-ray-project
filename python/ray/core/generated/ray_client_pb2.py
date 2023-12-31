# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/ray_client.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!src/ray/protobuf/ray_client.proto\x12\x07ray.rpc\"\x95\x01\n\x03\x41rg\x12$\n\x05local\x18\x01 \x01(\x0e\x32\x15.ray.rpc.Arg.Locality\x12\x14\n\x0creference_id\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x1b\n\x04type\x18\x04 \x01(\x0e\x32\r.ray.rpc.Type\"\'\n\x08Locality\x12\x0c\n\x08INTERNED\x10\x00\x12\r\n\tREFERENCE\x10\x01\"&\n\x0bTaskOptions\x12\x17\n\x0fpickled_options\x18\x01 \x01(\x0c\"\xf8\x03\n\nClientTask\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".ray.rpc.ClientTask.RemoteExecType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\npayload_id\x18\x03 \x01(\x0c\x12\x1a\n\x04\x61rgs\x18\x04 \x03(\x0b\x32\x0c.ray.rpc.Arg\x12/\n\x06kwargs\x18\x05 \x03(\x0b\x32\x1f.ray.rpc.ClientTask.KwargsEntry\x12\x11\n\tclient_id\x18\x06 \x01(\t\x12%\n\x07options\x18\x07 \x01(\x0b\x32\x14.ray.rpc.TaskOptions\x12.\n\x10\x62\x61seline_options\x18\x08 \x01(\x0b\x32\x14.ray.rpc.TaskOptions\x12\x11\n\tnamespace\x18\t \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\n \x01(\x0c\x12\x10\n\x08\x63hunk_id\x18\x0b \x01(\x05\x12\x14\n\x0ctotal_chunks\x18\x0c \x01(\x05\x1a;\n\x0bKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1b\n\x05value\x18\x02 \x01(\x0b\x32\x0c.ray.rpc.Arg:\x02\x38\x01\"Y\n\x0eRemoteExecType\x12\x0c\n\x08\x46UNCTION\x10\x00\x12\t\n\x05\x41\x43TOR\x10\x01\x12\n\n\x06METHOD\x10\x02\x12\x11\n\rSTATIC_METHOD\x10\x03\x12\x0f\n\x0bNAMED_ACTOR\x10\x04\"D\n\x10\x43lientTaskTicket\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x12\n\nreturn_ids\x18\x02 \x03(\x0c\x12\r\n\x05\x65rror\x18\x03 \x01(\x0c\"\x7f\n\nPutRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x15\n\rclient_ref_id\x18\x02 \x01(\x0c\x12\x10\n\x08\x63hunk_id\x18\x03 \x01(\x05\x12\x14\n\x0ctotal_chunks\x18\x04 \x01(\x05\x12\x12\n\ntotal_size\x18\x05 \x01(\x03\x12\x10\n\x08owner_id\x18\x06 \x01(\x0c\"7\n\x0bPutResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\r\n\x05valid\x18\x02 \x01(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\x0c\"h\n\nGetRequest\x12\x0b\n\x03ids\x18\x04 \x03(\x0c\x12\x0f\n\x07timeout\x18\x02 \x01(\x02\x12\x14\n\x0c\x61synchronous\x18\x03 \x01(\x08\x12\x16\n\x0estart_chunk_id\x18\x05 \x01(\x05\x12\x0e\n\x02id\x18\x01 \x01(\x0c\x42\x02\x18\x01\"u\n\x0bGetResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\r\n\x05\x65rror\x18\x03 \x01(\x0c\x12\x10\n\x08\x63hunk_id\x18\x04 \x01(\x05\x12\x14\n\x0ctotal_chunks\x18\x05 \x01(\x05\x12\x12\n\ntotal_size\x18\x06 \x01(\x04\"Z\n\x0bWaitRequest\x12\x12\n\nobject_ids\x18\x01 \x03(\x0c\x12\x13\n\x0bnum_returns\x18\x02 \x01(\x03\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x11\n\tclient_id\x18\x04 \x01(\t\"U\n\x0cWaitResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x18\n\x10ready_object_ids\x18\x02 \x03(\x0c\x12\x1c\n\x14remaining_object_ids\x18\x03 \x03(\x0c\"\xad\x01\n\x0f\x43lusterInfoType\"\x99\x01\n\x08TypeEnum\x12\x12\n\x0eIS_INITIALIZED\x10\x00\x12\t\n\x05NODES\x10\x01\x12\x15\n\x11\x43LUSTER_RESOURCES\x10\x02\x12\x17\n\x13\x41VAILABLE_RESOURCES\x10\x03\x12\x13\n\x0fRUNTIME_CONTEXT\x10\x04\x12\x0c\n\x08TIMELINE\x10\x05\x12\x08\n\x04PING\x10\x06\x12\x11\n\rDASHBOARD_URL\x10\x07\"E\n\x12\x43lusterInfoRequest\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.ray.rpc.ClusterInfoType.TypeEnum\"\x8a\x04\n\x13\x43lusterInfoResponse\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.ray.rpc.ClusterInfoType.TypeEnum\x12\x0e\n\x04json\x18\x02 \x01(\tH\x00\x12\x44\n\x0eresource_table\x18\x03 \x01(\x0b\x32*.ray.rpc.ClusterInfoResponse.ResourceTableH\x00\x12\x46\n\x0fruntime_context\x18\x04 \x01(\x0b\x32+.ray.rpc.ClusterInfoResponse.RuntimeContextH\x00\x1a\x83\x01\n\rResourceTable\x12\x44\n\x05table\x18\x01 \x03(\x0b\x32\x35.ray.rpc.ClusterInfoResponse.ResourceTable.TableEntry\x1a,\n\nTableEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x8c\x01\n\x0eRuntimeContext\x12\x0e\n\x06job_id\x18\x01 \x01(\x0c\x12\x0f\n\x07node_id\x18\x02 \x01(\x0c\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x13\n\x0bruntime_env\x18\x04 \x01(\t\x12\x1c\n\x14\x63\x61pture_client_tasks\x18\x05 \x01(\x08\x12\x13\n\x0bgcs_address\x18\x06 \x01(\tB\x0f\n\rresponse_type\"\xaf\x02\n\x10TerminateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x39\n\x05\x61\x63tor\x18\x02 \x01(\x0b\x32(.ray.rpc.TerminateRequest.ActorTerminateH\x00\x12\x44\n\x0btask_object\x18\x03 \x01(\x0b\x32-.ray.rpc.TerminateRequest.TaskObjectTerminateH\x00\x1a\x30\n\x0e\x41\x63torTerminate\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x12\n\nno_restart\x18\x02 \x01(\x08\x1a\x43\n\x13TaskObjectTerminate\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x12\x11\n\trecursive\x18\x03 \x01(\x08\x42\x10\n\x0eterminate_type\"\x1f\n\x11TerminateResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\"D\n\x0fKVExistsRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x16\n\tnamespace\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\x0c\n\n_namespace\"\"\n\x10KVExistsResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\"A\n\x0cKVGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x16\n\tnamespace\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\x0c\n\n_namespace\"-\n\rKVGetResponse\x12\x12\n\x05value\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x42\x08\n\x06_value\"c\n\x0cKVPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x11\n\toverwrite\x18\x03 \x01(\x08\x12\x16\n\tnamespace\x18\x04 \x01(\x0cH\x00\x88\x01\x01\x42\x0c\n\n_namespace\"\'\n\rKVPutResponse\x12\x16\n\x0e\x61lready_exists\x18\x01 \x01(\x08\"X\n\x0cKVDelRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x15\n\rdel_by_prefix\x18\x02 \x01(\x08\x12\x16\n\tnamespace\x18\x03 \x01(\x0cH\x00\x88\x01\x01\x42\x0c\n\n_namespace\"$\n\rKVDelResponse\x12\x13\n\x0b\x64\x65leted_num\x18\x01 \x01(\x05\"E\n\rKVListRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c\x12\x16\n\tnamespace\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\x0c\n\n_namespace\"\x1e\n\x0eKVListResponse\x12\x0c\n\x04keys\x18\x01 \x03(\x0c\"B\n\x1d\x43lientPinRuntimeEnvURIRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x14\n\x0c\x65xpiration_s\x18\x02 \x01(\x05\" \n\x1e\x43lientPinRuntimeEnvURIResponse\"Z\n\x0bInitRequest\x12\x12\n\njob_config\x18\x01 \x01(\x0c\x12\x17\n\x0fray_init_kwargs\x18\x02 \x01(\t\x12\x1e\n\x16reconnect_grace_period\x18\x03 \x01(\x05\"\'\n\x0cInitResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x17\n\x15PrepRuntimeEnvRequest\"\x18\n\x16PrepRuntimeEnvResponse\"6\n\x1c\x43lientListNamedActorsRequest\x12\x16\n\x0e\x61ll_namespaces\x18\x01 \x01(\x08\"4\n\x1d\x43lientListNamedActorsResponse\x12\x13\n\x0b\x61\x63tors_json\x18\x01 \x01(\t\"\x1d\n\x0eReleaseRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x0c\"\x1d\n\x0fReleaseResponse\x12\n\n\x02ok\x18\x02 \x03(\x08\"\x17\n\x15\x43onnectionInfoRequest\"\x88\x01\n\x16\x43onnectionInfoResponse\x12\x13\n\x0bnum_clients\x18\x01 \x01(\x05\x12\x13\n\x0bray_version\x18\x02 \x01(\t\x12\x12\n\nray_commit\x18\x03 \x01(\t\x12\x16\n\x0epython_version\x18\x04 \x01(\t\x12\x18\n\x10protocol_version\x18\x05 \x01(\t\"\x1a\n\x18\x43onnectionCleanupRequest\"\x1b\n\x19\x43onnectionCleanupResponse\"$\n\x12\x41\x63knowledgeRequest\x12\x0e\n\x06req_id\x18\x01 \x01(\x05\"\xc4\x04\n\x0b\x44\x61taRequest\x12\x0e\n\x06req_id\x18\x01 \x01(\x05\x12\"\n\x03get\x18\x02 \x01(\x0b\x32\x13.ray.rpc.GetRequestH\x00\x12\"\n\x03put\x18\x03 \x01(\x0b\x32\x13.ray.rpc.PutRequestH\x00\x12*\n\x07release\x18\x04 \x01(\x0b\x32\x17.ray.rpc.ReleaseRequestH\x00\x12\x39\n\x0f\x63onnection_info\x18\x05 \x01(\x0b\x32\x1e.ray.rpc.ConnectionInfoRequestH\x00\x12$\n\x04init\x18\x06 \x01(\x0b\x32\x14.ray.rpc.InitRequestH\x00\x12:\n\x10prep_runtime_env\x18\x07 \x01(\x0b\x32\x1e.ray.rpc.PrepRuntimeEnvRequestH\x00\x12?\n\x12\x63onnection_cleanup\x18\x08 \x01(\x0b\x32!.ray.rpc.ConnectionCleanupRequestH\x00\x12\x32\n\x0b\x61\x63knowledge\x18\t \x01(\x0b\x32\x1b.ray.rpc.AcknowledgeRequestH\x00\x12#\n\x04task\x18\n \x01(\x0b\x32\x13.ray.rpc.ClientTaskH\x00\x12.\n\tterminate\x18\x0b \x01(\x0b\x32\x19.ray.rpc.TerminateRequestH\x00\x12\x42\n\x11list_named_actors\x18\x0c \x01(\x0b\x32%.ray.rpc.ClientListNamedActorsRequestH\x00\x42\x06\n\x04type\"\xba\x04\n\x0c\x44\x61taResponse\x12\x0e\n\x06req_id\x18\x01 \x01(\x05\x12#\n\x03get\x18\x02 \x01(\x0b\x32\x14.ray.rpc.GetResponseH\x00\x12#\n\x03put\x18\x03 \x01(\x0b\x32\x14.ray.rpc.PutResponseH\x00\x12+\n\x07release\x18\x04 \x01(\x0b\x32\x18.ray.rpc.ReleaseResponseH\x00\x12:\n\x0f\x63onnection_info\x18\x05 \x01(\x0b\x32\x1f.ray.rpc.ConnectionInfoResponseH\x00\x12%\n\x04init\x18\x06 \x01(\x0b\x32\x15.ray.rpc.InitResponseH\x00\x12;\n\x10prep_runtime_env\x18\x07 \x01(\x0b\x32\x1f.ray.rpc.PrepRuntimeEnvResponseH\x00\x12@\n\x12\x63onnection_cleanup\x18\x08 \x01(\x0b\x32\".ray.rpc.ConnectionCleanupResponseH\x00\x12\x30\n\x0btask_ticket\x18\n \x01(\x0b\x32\x19.ray.rpc.ClientTaskTicketH\x00\x12/\n\tterminate\x18\x0b \x01(\x0b\x32\x1a.ray.rpc.TerminateResponseH\x00\x12\x43\n\x11list_named_actors\x18\x0c \x01(\x0b\x32&.ray.rpc.ClientListNamedActorsResponseH\x00\x42\x06\n\x04typeJ\x04\x08\t\x10\nR\x0b\x61\x63knowledge\"7\n\x12LogSettingsRequest\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x10\n\x08loglevel\x18\x02 \x01(\x05\"3\n\x07LogData\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t*\x13\n\x04Type\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x32\x96\x08\n\x0cRayletDriver\x12\x35\n\x04Init\x12\x14.ray.rpc.InitRequest\x1a\x15.ray.rpc.InitResponse\"\x00\x12S\n\x0ePrepRuntimeEnv\x12\x1e.ray.rpc.PrepRuntimeEnvRequest\x1a\x1f.ray.rpc.PrepRuntimeEnvResponse\"\x00\x12:\n\tGetObject\x12\x13.ray.rpc.GetRequest\x1a\x14.ray.rpc.GetResponse\"\x00\x30\x01\x12\x38\n\tPutObject\x12\x13.ray.rpc.PutRequest\x1a\x14.ray.rpc.PutResponse\"\x00\x12;\n\nWaitObject\x12\x14.ray.rpc.WaitRequest\x1a\x15.ray.rpc.WaitResponse\"\x00\x12<\n\x08Schedule\x12\x13.ray.rpc.ClientTask\x1a\x19.ray.rpc.ClientTaskTicket\"\x00\x12\x44\n\tTerminate\x12\x19.ray.rpc.TerminateRequest\x1a\x1a.ray.rpc.TerminateResponse\"\x00\x12J\n\x0b\x43lusterInfo\x12\x1b.ray.rpc.ClusterInfoRequest\x1a\x1c.ray.rpc.ClusterInfoResponse\"\x00\x12\x38\n\x05KVGet\x12\x15.ray.rpc.KVGetRequest\x1a\x16.ray.rpc.KVGetResponse\"\x00\x12\x38\n\x05KVPut\x12\x15.ray.rpc.KVPutRequest\x1a\x16.ray.rpc.KVPutResponse\"\x00\x12\x38\n\x05KVDel\x12\x15.ray.rpc.KVDelRequest\x1a\x16.ray.rpc.KVDelResponse\"\x00\x12;\n\x06KVList\x12\x16.ray.rpc.KVListRequest\x1a\x17.ray.rpc.KVListResponse\"\x00\x12\x41\n\x08KVExists\x12\x18.ray.rpc.KVExistsRequest\x1a\x19.ray.rpc.KVExistsResponse\"\x00\x12\x62\n\x0fListNamedActors\x12%.ray.rpc.ClientListNamedActorsRequest\x1a&.ray.rpc.ClientListNamedActorsResponse\"\x00\x12\x65\n\x10PinRuntimeEnvURI\x12&.ray.rpc.ClientPinRuntimeEnvURIRequest\x1a\'.ray.rpc.ClientPinRuntimeEnvURIResponse\"\x00\x32S\n\x12RayletDataStreamer\x12=\n\x08\x44\x61tapath\x12\x14.ray.rpc.DataRequest\x1a\x15.ray.rpc.DataResponse\"\x00(\x01\x30\x01\x32U\n\x11RayletLogStreamer\x12@\n\tLogstream\x12\x1b.ray.rpc.LogSettingsRequest\x1a\x10.ray.rpc.LogData\"\x00(\x01\x30\x01\x42\x03\xf8\x01\x01\x62\x06proto3')

_TYPE = DESCRIPTOR.enum_types_by_name['Type']
Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
DEFAULT = 0


_ARG = DESCRIPTOR.message_types_by_name['Arg']
_TASKOPTIONS = DESCRIPTOR.message_types_by_name['TaskOptions']
_CLIENTTASK = DESCRIPTOR.message_types_by_name['ClientTask']
_CLIENTTASK_KWARGSENTRY = _CLIENTTASK.nested_types_by_name['KwargsEntry']
_CLIENTTASKTICKET = DESCRIPTOR.message_types_by_name['ClientTaskTicket']
_PUTREQUEST = DESCRIPTOR.message_types_by_name['PutRequest']
_PUTRESPONSE = DESCRIPTOR.message_types_by_name['PutResponse']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_WAITREQUEST = DESCRIPTOR.message_types_by_name['WaitRequest']
_WAITRESPONSE = DESCRIPTOR.message_types_by_name['WaitResponse']
_CLUSTERINFOTYPE = DESCRIPTOR.message_types_by_name['ClusterInfoType']
_CLUSTERINFOREQUEST = DESCRIPTOR.message_types_by_name['ClusterInfoRequest']
_CLUSTERINFORESPONSE = DESCRIPTOR.message_types_by_name['ClusterInfoResponse']
_CLUSTERINFORESPONSE_RESOURCETABLE = _CLUSTERINFORESPONSE.nested_types_by_name['ResourceTable']
_CLUSTERINFORESPONSE_RESOURCETABLE_TABLEENTRY = _CLUSTERINFORESPONSE_RESOURCETABLE.nested_types_by_name['TableEntry']
_CLUSTERINFORESPONSE_RUNTIMECONTEXT = _CLUSTERINFORESPONSE.nested_types_by_name['RuntimeContext']
_TERMINATEREQUEST = DESCRIPTOR.message_types_by_name['TerminateRequest']
_TERMINATEREQUEST_ACTORTERMINATE = _TERMINATEREQUEST.nested_types_by_name['ActorTerminate']
_TERMINATEREQUEST_TASKOBJECTTERMINATE = _TERMINATEREQUEST.nested_types_by_name['TaskObjectTerminate']
_TERMINATERESPONSE = DESCRIPTOR.message_types_by_name['TerminateResponse']
_KVEXISTSREQUEST = DESCRIPTOR.message_types_by_name['KVExistsRequest']
_KVEXISTSRESPONSE = DESCRIPTOR.message_types_by_name['KVExistsResponse']
_KVGETREQUEST = DESCRIPTOR.message_types_by_name['KVGetRequest']
_KVGETRESPONSE = DESCRIPTOR.message_types_by_name['KVGetResponse']
_KVPUTREQUEST = DESCRIPTOR.message_types_by_name['KVPutRequest']
_KVPUTRESPONSE = DESCRIPTOR.message_types_by_name['KVPutResponse']
_KVDELREQUEST = DESCRIPTOR.message_types_by_name['KVDelRequest']
_KVDELRESPONSE = DESCRIPTOR.message_types_by_name['KVDelResponse']
_KVLISTREQUEST = DESCRIPTOR.message_types_by_name['KVListRequest']
_KVLISTRESPONSE = DESCRIPTOR.message_types_by_name['KVListResponse']
_CLIENTPINRUNTIMEENVURIREQUEST = DESCRIPTOR.message_types_by_name['ClientPinRuntimeEnvURIRequest']
_CLIENTPINRUNTIMEENVURIRESPONSE = DESCRIPTOR.message_types_by_name['ClientPinRuntimeEnvURIResponse']
_INITREQUEST = DESCRIPTOR.message_types_by_name['InitRequest']
_INITRESPONSE = DESCRIPTOR.message_types_by_name['InitResponse']
_PREPRUNTIMEENVREQUEST = DESCRIPTOR.message_types_by_name['PrepRuntimeEnvRequest']
_PREPRUNTIMEENVRESPONSE = DESCRIPTOR.message_types_by_name['PrepRuntimeEnvResponse']
_CLIENTLISTNAMEDACTORSREQUEST = DESCRIPTOR.message_types_by_name['ClientListNamedActorsRequest']
_CLIENTLISTNAMEDACTORSRESPONSE = DESCRIPTOR.message_types_by_name['ClientListNamedActorsResponse']
_RELEASEREQUEST = DESCRIPTOR.message_types_by_name['ReleaseRequest']
_RELEASERESPONSE = DESCRIPTOR.message_types_by_name['ReleaseResponse']
_CONNECTIONINFOREQUEST = DESCRIPTOR.message_types_by_name['ConnectionInfoRequest']
_CONNECTIONINFORESPONSE = DESCRIPTOR.message_types_by_name['ConnectionInfoResponse']
_CONNECTIONCLEANUPREQUEST = DESCRIPTOR.message_types_by_name['ConnectionCleanupRequest']
_CONNECTIONCLEANUPRESPONSE = DESCRIPTOR.message_types_by_name['ConnectionCleanupResponse']
_ACKNOWLEDGEREQUEST = DESCRIPTOR.message_types_by_name['AcknowledgeRequest']
_DATAREQUEST = DESCRIPTOR.message_types_by_name['DataRequest']
_DATARESPONSE = DESCRIPTOR.message_types_by_name['DataResponse']
_LOGSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['LogSettingsRequest']
_LOGDATA = DESCRIPTOR.message_types_by_name['LogData']
_ARG_LOCALITY = _ARG.enum_types_by_name['Locality']
_CLIENTTASK_REMOTEEXECTYPE = _CLIENTTASK.enum_types_by_name['RemoteExecType']
_CLUSTERINFOTYPE_TYPEENUM = _CLUSTERINFOTYPE.enum_types_by_name['TypeEnum']
Arg = _reflection.GeneratedProtocolMessageType('Arg', (_message.Message,), {
  'DESCRIPTOR' : _ARG,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.Arg)
  })
_sym_db.RegisterMessage(Arg)

TaskOptions = _reflection.GeneratedProtocolMessageType('TaskOptions', (_message.Message,), {
  'DESCRIPTOR' : _TASKOPTIONS,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.TaskOptions)
  })
_sym_db.RegisterMessage(TaskOptions)

ClientTask = _reflection.GeneratedProtocolMessageType('ClientTask', (_message.Message,), {

  'KwargsEntry' : _reflection.GeneratedProtocolMessageType('KwargsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLIENTTASK_KWARGSENTRY,
    '__module__' : 'src.ray.protobuf.ray_client_pb2'
    # @@protoc_insertion_point(class_scope:ray.rpc.ClientTask.KwargsEntry)
    })
  ,
  'DESCRIPTOR' : _CLIENTTASK,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClientTask)
  })
_sym_db.RegisterMessage(ClientTask)
_sym_db.RegisterMessage(ClientTask.KwargsEntry)

ClientTaskTicket = _reflection.GeneratedProtocolMessageType('ClientTaskTicket', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTTASKTICKET,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClientTaskTicket)
  })
_sym_db.RegisterMessage(ClientTaskTicket)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PutResponse)
  })
_sym_db.RegisterMessage(PutResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

WaitRequest = _reflection.GeneratedProtocolMessageType('WaitRequest', (_message.Message,), {
  'DESCRIPTOR' : _WAITREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.WaitRequest)
  })
_sym_db.RegisterMessage(WaitRequest)

WaitResponse = _reflection.GeneratedProtocolMessageType('WaitResponse', (_message.Message,), {
  'DESCRIPTOR' : _WAITRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.WaitResponse)
  })
_sym_db.RegisterMessage(WaitResponse)

ClusterInfoType = _reflection.GeneratedProtocolMessageType('ClusterInfoType', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERINFOTYPE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClusterInfoType)
  })
_sym_db.RegisterMessage(ClusterInfoType)

ClusterInfoRequest = _reflection.GeneratedProtocolMessageType('ClusterInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERINFOREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClusterInfoRequest)
  })
_sym_db.RegisterMessage(ClusterInfoRequest)

ClusterInfoResponse = _reflection.GeneratedProtocolMessageType('ClusterInfoResponse', (_message.Message,), {

  'ResourceTable' : _reflection.GeneratedProtocolMessageType('ResourceTable', (_message.Message,), {

    'TableEntry' : _reflection.GeneratedProtocolMessageType('TableEntry', (_message.Message,), {
      'DESCRIPTOR' : _CLUSTERINFORESPONSE_RESOURCETABLE_TABLEENTRY,
      '__module__' : 'src.ray.protobuf.ray_client_pb2'
      # @@protoc_insertion_point(class_scope:ray.rpc.ClusterInfoResponse.ResourceTable.TableEntry)
      })
    ,
    'DESCRIPTOR' : _CLUSTERINFORESPONSE_RESOURCETABLE,
    '__module__' : 'src.ray.protobuf.ray_client_pb2'
    # @@protoc_insertion_point(class_scope:ray.rpc.ClusterInfoResponse.ResourceTable)
    })
  ,

  'RuntimeContext' : _reflection.GeneratedProtocolMessageType('RuntimeContext', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTERINFORESPONSE_RUNTIMECONTEXT,
    '__module__' : 'src.ray.protobuf.ray_client_pb2'
    # @@protoc_insertion_point(class_scope:ray.rpc.ClusterInfoResponse.RuntimeContext)
    })
  ,
  'DESCRIPTOR' : _CLUSTERINFORESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClusterInfoResponse)
  })
_sym_db.RegisterMessage(ClusterInfoResponse)
_sym_db.RegisterMessage(ClusterInfoResponse.ResourceTable)
_sym_db.RegisterMessage(ClusterInfoResponse.ResourceTable.TableEntry)
_sym_db.RegisterMessage(ClusterInfoResponse.RuntimeContext)

TerminateRequest = _reflection.GeneratedProtocolMessageType('TerminateRequest', (_message.Message,), {

  'ActorTerminate' : _reflection.GeneratedProtocolMessageType('ActorTerminate', (_message.Message,), {
    'DESCRIPTOR' : _TERMINATEREQUEST_ACTORTERMINATE,
    '__module__' : 'src.ray.protobuf.ray_client_pb2'
    # @@protoc_insertion_point(class_scope:ray.rpc.TerminateRequest.ActorTerminate)
    })
  ,

  'TaskObjectTerminate' : _reflection.GeneratedProtocolMessageType('TaskObjectTerminate', (_message.Message,), {
    'DESCRIPTOR' : _TERMINATEREQUEST_TASKOBJECTTERMINATE,
    '__module__' : 'src.ray.protobuf.ray_client_pb2'
    # @@protoc_insertion_point(class_scope:ray.rpc.TerminateRequest.TaskObjectTerminate)
    })
  ,
  'DESCRIPTOR' : _TERMINATEREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.TerminateRequest)
  })
_sym_db.RegisterMessage(TerminateRequest)
_sym_db.RegisterMessage(TerminateRequest.ActorTerminate)
_sym_db.RegisterMessage(TerminateRequest.TaskObjectTerminate)

TerminateResponse = _reflection.GeneratedProtocolMessageType('TerminateResponse', (_message.Message,), {
  'DESCRIPTOR' : _TERMINATERESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.TerminateResponse)
  })
_sym_db.RegisterMessage(TerminateResponse)

KVExistsRequest = _reflection.GeneratedProtocolMessageType('KVExistsRequest', (_message.Message,), {
  'DESCRIPTOR' : _KVEXISTSREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVExistsRequest)
  })
_sym_db.RegisterMessage(KVExistsRequest)

KVExistsResponse = _reflection.GeneratedProtocolMessageType('KVExistsResponse', (_message.Message,), {
  'DESCRIPTOR' : _KVEXISTSRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVExistsResponse)
  })
_sym_db.RegisterMessage(KVExistsResponse)

KVGetRequest = _reflection.GeneratedProtocolMessageType('KVGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _KVGETREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVGetRequest)
  })
_sym_db.RegisterMessage(KVGetRequest)

KVGetResponse = _reflection.GeneratedProtocolMessageType('KVGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _KVGETRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVGetResponse)
  })
_sym_db.RegisterMessage(KVGetResponse)

KVPutRequest = _reflection.GeneratedProtocolMessageType('KVPutRequest', (_message.Message,), {
  'DESCRIPTOR' : _KVPUTREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVPutRequest)
  })
_sym_db.RegisterMessage(KVPutRequest)

KVPutResponse = _reflection.GeneratedProtocolMessageType('KVPutResponse', (_message.Message,), {
  'DESCRIPTOR' : _KVPUTRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVPutResponse)
  })
_sym_db.RegisterMessage(KVPutResponse)

KVDelRequest = _reflection.GeneratedProtocolMessageType('KVDelRequest', (_message.Message,), {
  'DESCRIPTOR' : _KVDELREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVDelRequest)
  })
_sym_db.RegisterMessage(KVDelRequest)

KVDelResponse = _reflection.GeneratedProtocolMessageType('KVDelResponse', (_message.Message,), {
  'DESCRIPTOR' : _KVDELRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVDelResponse)
  })
_sym_db.RegisterMessage(KVDelResponse)

KVListRequest = _reflection.GeneratedProtocolMessageType('KVListRequest', (_message.Message,), {
  'DESCRIPTOR' : _KVLISTREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVListRequest)
  })
_sym_db.RegisterMessage(KVListRequest)

KVListResponse = _reflection.GeneratedProtocolMessageType('KVListResponse', (_message.Message,), {
  'DESCRIPTOR' : _KVLISTRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.KVListResponse)
  })
_sym_db.RegisterMessage(KVListResponse)

ClientPinRuntimeEnvURIRequest = _reflection.GeneratedProtocolMessageType('ClientPinRuntimeEnvURIRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTPINRUNTIMEENVURIREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClientPinRuntimeEnvURIRequest)
  })
_sym_db.RegisterMessage(ClientPinRuntimeEnvURIRequest)

ClientPinRuntimeEnvURIResponse = _reflection.GeneratedProtocolMessageType('ClientPinRuntimeEnvURIResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTPINRUNTIMEENVURIRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClientPinRuntimeEnvURIResponse)
  })
_sym_db.RegisterMessage(ClientPinRuntimeEnvURIResponse)

InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.InitRequest)
  })
_sym_db.RegisterMessage(InitRequest)

InitResponse = _reflection.GeneratedProtocolMessageType('InitResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.InitResponse)
  })
_sym_db.RegisterMessage(InitResponse)

PrepRuntimeEnvRequest = _reflection.GeneratedProtocolMessageType('PrepRuntimeEnvRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPRUNTIMEENVREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PrepRuntimeEnvRequest)
  })
_sym_db.RegisterMessage(PrepRuntimeEnvRequest)

PrepRuntimeEnvResponse = _reflection.GeneratedProtocolMessageType('PrepRuntimeEnvResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPRUNTIMEENVRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PrepRuntimeEnvResponse)
  })
_sym_db.RegisterMessage(PrepRuntimeEnvResponse)

ClientListNamedActorsRequest = _reflection.GeneratedProtocolMessageType('ClientListNamedActorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTLISTNAMEDACTORSREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClientListNamedActorsRequest)
  })
_sym_db.RegisterMessage(ClientListNamedActorsRequest)

ClientListNamedActorsResponse = _reflection.GeneratedProtocolMessageType('ClientListNamedActorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTLISTNAMEDACTORSRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ClientListNamedActorsResponse)
  })
_sym_db.RegisterMessage(ClientListNamedActorsResponse)

ReleaseRequest = _reflection.GeneratedProtocolMessageType('ReleaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReleaseRequest)
  })
_sym_db.RegisterMessage(ReleaseRequest)

ReleaseResponse = _reflection.GeneratedProtocolMessageType('ReleaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _RELEASERESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReleaseResponse)
  })
_sym_db.RegisterMessage(ReleaseResponse)

ConnectionInfoRequest = _reflection.GeneratedProtocolMessageType('ConnectionInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONINFOREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ConnectionInfoRequest)
  })
_sym_db.RegisterMessage(ConnectionInfoRequest)

ConnectionInfoResponse = _reflection.GeneratedProtocolMessageType('ConnectionInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONINFORESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ConnectionInfoResponse)
  })
_sym_db.RegisterMessage(ConnectionInfoResponse)

ConnectionCleanupRequest = _reflection.GeneratedProtocolMessageType('ConnectionCleanupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONCLEANUPREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ConnectionCleanupRequest)
  })
_sym_db.RegisterMessage(ConnectionCleanupRequest)

ConnectionCleanupResponse = _reflection.GeneratedProtocolMessageType('ConnectionCleanupResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONCLEANUPRESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ConnectionCleanupResponse)
  })
_sym_db.RegisterMessage(ConnectionCleanupResponse)

AcknowledgeRequest = _reflection.GeneratedProtocolMessageType('AcknowledgeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACKNOWLEDGEREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.AcknowledgeRequest)
  })
_sym_db.RegisterMessage(AcknowledgeRequest)

DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.DataRequest)
  })
_sym_db.RegisterMessage(DataRequest)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATARESPONSE,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.DataResponse)
  })
_sym_db.RegisterMessage(DataResponse)

LogSettingsRequest = _reflection.GeneratedProtocolMessageType('LogSettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGSETTINGSREQUEST,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.LogSettingsRequest)
  })
_sym_db.RegisterMessage(LogSettingsRequest)

LogData = _reflection.GeneratedProtocolMessageType('LogData', (_message.Message,), {
  'DESCRIPTOR' : _LOGDATA,
  '__module__' : 'src.ray.protobuf.ray_client_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.LogData)
  })
_sym_db.RegisterMessage(LogData)

_RAYLETDRIVER = DESCRIPTOR.services_by_name['RayletDriver']
_RAYLETDATASTREAMER = DESCRIPTOR.services_by_name['RayletDataStreamer']
_RAYLETLOGSTREAMER = DESCRIPTOR.services_by_name['RayletLogStreamer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _CLIENTTASK_KWARGSENTRY._options = None
  _CLIENTTASK_KWARGSENTRY._serialized_options = b'8\001'
  _GETREQUEST.fields_by_name['id']._options = None
  _GETREQUEST.fields_by_name['id']._serialized_options = b'\030\001'
  _CLUSTERINFORESPONSE_RESOURCETABLE_TABLEENTRY._options = None
  _CLUSTERINFORESPONSE_RESOURCETABLE_TABLEENTRY._serialized_options = b'8\001'
  _TYPE._serialized_start=5092
  _TYPE._serialized_end=5111
  _ARG._serialized_start=47
  _ARG._serialized_end=196
  _ARG_LOCALITY._serialized_start=157
  _ARG_LOCALITY._serialized_end=196
  _TASKOPTIONS._serialized_start=198
  _TASKOPTIONS._serialized_end=236
  _CLIENTTASK._serialized_start=239
  _CLIENTTASK._serialized_end=743
  _CLIENTTASK_KWARGSENTRY._serialized_start=593
  _CLIENTTASK_KWARGSENTRY._serialized_end=652
  _CLIENTTASK_REMOTEEXECTYPE._serialized_start=654
  _CLIENTTASK_REMOTEEXECTYPE._serialized_end=743
  _CLIENTTASKTICKET._serialized_start=745
  _CLIENTTASKTICKET._serialized_end=813
  _PUTREQUEST._serialized_start=815
  _PUTREQUEST._serialized_end=942
  _PUTRESPONSE._serialized_start=944
  _PUTRESPONSE._serialized_end=999
  _GETREQUEST._serialized_start=1001
  _GETREQUEST._serialized_end=1105
  _GETRESPONSE._serialized_start=1107
  _GETRESPONSE._serialized_end=1224
  _WAITREQUEST._serialized_start=1226
  _WAITREQUEST._serialized_end=1316
  _WAITRESPONSE._serialized_start=1318
  _WAITRESPONSE._serialized_end=1403
  _CLUSTERINFOTYPE._serialized_start=1406
  _CLUSTERINFOTYPE._serialized_end=1579
  _CLUSTERINFOTYPE_TYPEENUM._serialized_start=1426
  _CLUSTERINFOTYPE_TYPEENUM._serialized_end=1579
  _CLUSTERINFOREQUEST._serialized_start=1581
  _CLUSTERINFOREQUEST._serialized_end=1650
  _CLUSTERINFORESPONSE._serialized_start=1653
  _CLUSTERINFORESPONSE._serialized_end=2175
  _CLUSTERINFORESPONSE_RESOURCETABLE._serialized_start=1884
  _CLUSTERINFORESPONSE_RESOURCETABLE._serialized_end=2015
  _CLUSTERINFORESPONSE_RESOURCETABLE_TABLEENTRY._serialized_start=1971
  _CLUSTERINFORESPONSE_RESOURCETABLE_TABLEENTRY._serialized_end=2015
  _CLUSTERINFORESPONSE_RUNTIMECONTEXT._serialized_start=2018
  _CLUSTERINFORESPONSE_RUNTIMECONTEXT._serialized_end=2158
  _TERMINATEREQUEST._serialized_start=2178
  _TERMINATEREQUEST._serialized_end=2481
  _TERMINATEREQUEST_ACTORTERMINATE._serialized_start=2346
  _TERMINATEREQUEST_ACTORTERMINATE._serialized_end=2394
  _TERMINATEREQUEST_TASKOBJECTTERMINATE._serialized_start=2396
  _TERMINATEREQUEST_TASKOBJECTTERMINATE._serialized_end=2463
  _TERMINATERESPONSE._serialized_start=2483
  _TERMINATERESPONSE._serialized_end=2514
  _KVEXISTSREQUEST._serialized_start=2516
  _KVEXISTSREQUEST._serialized_end=2584
  _KVEXISTSRESPONSE._serialized_start=2586
  _KVEXISTSRESPONSE._serialized_end=2620
  _KVGETREQUEST._serialized_start=2622
  _KVGETREQUEST._serialized_end=2687
  _KVGETRESPONSE._serialized_start=2689
  _KVGETRESPONSE._serialized_end=2734
  _KVPUTREQUEST._serialized_start=2736
  _KVPUTREQUEST._serialized_end=2835
  _KVPUTRESPONSE._serialized_start=2837
  _KVPUTRESPONSE._serialized_end=2876
  _KVDELREQUEST._serialized_start=2878
  _KVDELREQUEST._serialized_end=2966
  _KVDELRESPONSE._serialized_start=2968
  _KVDELRESPONSE._serialized_end=3004
  _KVLISTREQUEST._serialized_start=3006
  _KVLISTREQUEST._serialized_end=3075
  _KVLISTRESPONSE._serialized_start=3077
  _KVLISTRESPONSE._serialized_end=3107
  _CLIENTPINRUNTIMEENVURIREQUEST._serialized_start=3109
  _CLIENTPINRUNTIMEENVURIREQUEST._serialized_end=3175
  _CLIENTPINRUNTIMEENVURIRESPONSE._serialized_start=3177
  _CLIENTPINRUNTIMEENVURIRESPONSE._serialized_end=3209
  _INITREQUEST._serialized_start=3211
  _INITREQUEST._serialized_end=3301
  _INITRESPONSE._serialized_start=3303
  _INITRESPONSE._serialized_end=3342
  _PREPRUNTIMEENVREQUEST._serialized_start=3344
  _PREPRUNTIMEENVREQUEST._serialized_end=3367
  _PREPRUNTIMEENVRESPONSE._serialized_start=3369
  _PREPRUNTIMEENVRESPONSE._serialized_end=3393
  _CLIENTLISTNAMEDACTORSREQUEST._serialized_start=3395
  _CLIENTLISTNAMEDACTORSREQUEST._serialized_end=3449
  _CLIENTLISTNAMEDACTORSRESPONSE._serialized_start=3451
  _CLIENTLISTNAMEDACTORSRESPONSE._serialized_end=3503
  _RELEASEREQUEST._serialized_start=3505
  _RELEASEREQUEST._serialized_end=3534
  _RELEASERESPONSE._serialized_start=3536
  _RELEASERESPONSE._serialized_end=3565
  _CONNECTIONINFOREQUEST._serialized_start=3567
  _CONNECTIONINFOREQUEST._serialized_end=3590
  _CONNECTIONINFORESPONSE._serialized_start=3593
  _CONNECTIONINFORESPONSE._serialized_end=3729
  _CONNECTIONCLEANUPREQUEST._serialized_start=3731
  _CONNECTIONCLEANUPREQUEST._serialized_end=3757
  _CONNECTIONCLEANUPRESPONSE._serialized_start=3759
  _CONNECTIONCLEANUPRESPONSE._serialized_end=3786
  _ACKNOWLEDGEREQUEST._serialized_start=3788
  _ACKNOWLEDGEREQUEST._serialized_end=3824
  _DATAREQUEST._serialized_start=3827
  _DATAREQUEST._serialized_end=4407
  _DATARESPONSE._serialized_start=4410
  _DATARESPONSE._serialized_end=4980
  _LOGSETTINGSREQUEST._serialized_start=4982
  _LOGSETTINGSREQUEST._serialized_end=5037
  _LOGDATA._serialized_start=5039
  _LOGDATA._serialized_end=5090
  _RAYLETDRIVER._serialized_start=5114
  _RAYLETDRIVER._serialized_end=6160
  _RAYLETDATASTREAMER._serialized_start=6162
  _RAYLETDATASTREAMER._serialized_end=6245
  _RAYLETLOGSTREAMER._serialized_start=6247
  _RAYLETLOGSTREAMER._serialized_end=6332
# @@protoc_insertion_point(module_scope)
