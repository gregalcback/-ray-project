# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/reporter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import metrics_pb2 as opencensus_dot_proto_dot_metrics_dot_v1_dot_metrics__pb2
from . import common_pb2 as src_dot_ray_dot_protobuf_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsrc/ray/protobuf/reporter.proto\x12\x07ray.rpc\x1a)opencensus/proto/metrics/v1/metrics.proto\x1a\x1dsrc/ray/protobuf/common.proto\"9\n\x18GetProfilingStatsRequest\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\"S\n\x16GetProfilingStatsReply\x12\x17\n\x0fprofiling_stats\x18\x01 \x01(\t\x12\x0f\n\x07std_out\x18\x02 \x01(\t\x12\x0f\n\x07std_err\x18\x03 \x01(\t\"B\n\x13GetTracebackRequest\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x13\n\x06native\x18\x02 \x01(\x08H\x00\x88\x01\x01\x42\t\n\x07_native\"4\n\x11GetTracebackReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06output\x18\x02 \x01(\t\"\x86\x01\n\x13\x43puProfilingRequest\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x13\n\x06\x66ormat\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x64uration\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x13\n\x06native\x18\x04 \x01(\x08H\x02\x88\x01\x01\x42\t\n\x07_formatB\x0b\n\t_durationB\t\n\x07_native\"4\n\x11\x43puProfilingReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06output\x18\x02 \x01(\t\"D\n\x14ReportMetricsRequest\x12,\n\x0emetrics_points\x18\x01 \x03(\x0b\x32\x14.ray.rpc.MetricPoint\"9\n\x12ReportMetricsReply\x12#\n\x1bmetrcs_description_required\x18\x01 \x01(\x08\"a\n\x16ReportOCMetricsRequest\x12\x34\n\x07metrics\x18\x01 \x03(\x0b\x32#.opencensus.proto.metrics.v1.Metric\x12\x11\n\tworker_id\x18\x02 \x01(\x0c\"\x16\n\x14ReportOCMetricsReply\"\xd3\x01\n\x10StreamLogRequest\x12\x15\n\rlog_file_name\x18\x01 \x01(\t\x12\x12\n\nkeep_alive\x18\x02 \x01(\x08\x12\x12\n\x05lines\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08interval\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x19\n\x0cstart_offset\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x17\n\nend_offset\x18\x06 \x01(\x05H\x03\x88\x01\x01\x42\x08\n\x06_linesB\x0b\n\t_intervalB\x0f\n\r_start_offsetB\r\n\x0b_end_offset\"\x1e\n\x0eStreamLogReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"&\n\x0fListLogsRequest\x12\x13\n\x0bglob_filter\x18\x01 \x01(\t\"\"\n\rListLogsReply\x12\x11\n\tlog_files\x18\x01 \x03(\t2\x9e\x03\n\x0fReporterService\x12W\n\x11GetProfilingStats\x12!.ray.rpc.GetProfilingStatsRequest\x1a\x1f.ray.rpc.GetProfilingStatsReply\x12K\n\rReportMetrics\x12\x1d.ray.rpc.ReportMetricsRequest\x1a\x1b.ray.rpc.ReportMetricsReply\x12Q\n\x0fReportOCMetrics\x12\x1f.ray.rpc.ReportOCMetricsRequest\x1a\x1d.ray.rpc.ReportOCMetricsReply\x12H\n\x0cGetTraceback\x12\x1c.ray.rpc.GetTracebackRequest\x1a\x1a.ray.rpc.GetTracebackReply\x12H\n\x0c\x43puProfiling\x12\x1c.ray.rpc.CpuProfilingRequest\x1a\x1a.ray.rpc.CpuProfilingReply2\x8d\x01\n\nLogService\x12<\n\x08ListLogs\x12\x18.ray.rpc.ListLogsRequest\x1a\x16.ray.rpc.ListLogsReply\x12\x41\n\tStreamLog\x12\x19.ray.rpc.StreamLogRequest\x1a\x17.ray.rpc.StreamLogReply0\x01\x42\x03\xf8\x01\x01\x62\x06proto3')



_GETPROFILINGSTATSREQUEST = DESCRIPTOR.message_types_by_name['GetProfilingStatsRequest']
_GETPROFILINGSTATSREPLY = DESCRIPTOR.message_types_by_name['GetProfilingStatsReply']
_GETTRACEBACKREQUEST = DESCRIPTOR.message_types_by_name['GetTracebackRequest']
_GETTRACEBACKREPLY = DESCRIPTOR.message_types_by_name['GetTracebackReply']
_CPUPROFILINGREQUEST = DESCRIPTOR.message_types_by_name['CpuProfilingRequest']
_CPUPROFILINGREPLY = DESCRIPTOR.message_types_by_name['CpuProfilingReply']
_REPORTMETRICSREQUEST = DESCRIPTOR.message_types_by_name['ReportMetricsRequest']
_REPORTMETRICSREPLY = DESCRIPTOR.message_types_by_name['ReportMetricsReply']
_REPORTOCMETRICSREQUEST = DESCRIPTOR.message_types_by_name['ReportOCMetricsRequest']
_REPORTOCMETRICSREPLY = DESCRIPTOR.message_types_by_name['ReportOCMetricsReply']
_STREAMLOGREQUEST = DESCRIPTOR.message_types_by_name['StreamLogRequest']
_STREAMLOGREPLY = DESCRIPTOR.message_types_by_name['StreamLogReply']
_LISTLOGSREQUEST = DESCRIPTOR.message_types_by_name['ListLogsRequest']
_LISTLOGSREPLY = DESCRIPTOR.message_types_by_name['ListLogsReply']
GetProfilingStatsRequest = _reflection.GeneratedProtocolMessageType('GetProfilingStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROFILINGSTATSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetProfilingStatsRequest)
  })
_sym_db.RegisterMessage(GetProfilingStatsRequest)

GetProfilingStatsReply = _reflection.GeneratedProtocolMessageType('GetProfilingStatsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETPROFILINGSTATSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetProfilingStatsReply)
  })
_sym_db.RegisterMessage(GetProfilingStatsReply)

GetTracebackRequest = _reflection.GeneratedProtocolMessageType('GetTracebackRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRACEBACKREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetTracebackRequest)
  })
_sym_db.RegisterMessage(GetTracebackRequest)

GetTracebackReply = _reflection.GeneratedProtocolMessageType('GetTracebackReply', (_message.Message,), {
  'DESCRIPTOR' : _GETTRACEBACKREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetTracebackReply)
  })
_sym_db.RegisterMessage(GetTracebackReply)

CpuProfilingRequest = _reflection.GeneratedProtocolMessageType('CpuProfilingRequest', (_message.Message,), {
  'DESCRIPTOR' : _CPUPROFILINGREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CpuProfilingRequest)
  })
_sym_db.RegisterMessage(CpuProfilingRequest)

CpuProfilingReply = _reflection.GeneratedProtocolMessageType('CpuProfilingReply', (_message.Message,), {
  'DESCRIPTOR' : _CPUPROFILINGREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CpuProfilingReply)
  })
_sym_db.RegisterMessage(CpuProfilingReply)

ReportMetricsRequest = _reflection.GeneratedProtocolMessageType('ReportMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTMETRICSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportMetricsRequest)
  })
_sym_db.RegisterMessage(ReportMetricsRequest)

ReportMetricsReply = _reflection.GeneratedProtocolMessageType('ReportMetricsReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTMETRICSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportMetricsReply)
  })
_sym_db.RegisterMessage(ReportMetricsReply)

ReportOCMetricsRequest = _reflection.GeneratedProtocolMessageType('ReportOCMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTOCMETRICSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportOCMetricsRequest)
  })
_sym_db.RegisterMessage(ReportOCMetricsRequest)

ReportOCMetricsReply = _reflection.GeneratedProtocolMessageType('ReportOCMetricsReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTOCMETRICSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportOCMetricsReply)
  })
_sym_db.RegisterMessage(ReportOCMetricsReply)

StreamLogRequest = _reflection.GeneratedProtocolMessageType('StreamLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.StreamLogRequest)
  })
_sym_db.RegisterMessage(StreamLogRequest)

StreamLogReply = _reflection.GeneratedProtocolMessageType('StreamLogReply', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.StreamLogReply)
  })
_sym_db.RegisterMessage(StreamLogReply)

ListLogsRequest = _reflection.GeneratedProtocolMessageType('ListLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ListLogsRequest)
  })
_sym_db.RegisterMessage(ListLogsRequest)

ListLogsReply = _reflection.GeneratedProtocolMessageType('ListLogsReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ListLogsReply)
  })
_sym_db.RegisterMessage(ListLogsReply)

_REPORTERSERVICE = DESCRIPTOR.services_by_name['ReporterService']
_LOGSERVICE = DESCRIPTOR.services_by_name['LogService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _GETPROFILINGSTATSREQUEST._serialized_start=118
  _GETPROFILINGSTATSREQUEST._serialized_end=175
  _GETPROFILINGSTATSREPLY._serialized_start=177
  _GETPROFILINGSTATSREPLY._serialized_end=260
  _GETTRACEBACKREQUEST._serialized_start=262
  _GETTRACEBACKREQUEST._serialized_end=328
  _GETTRACEBACKREPLY._serialized_start=330
  _GETTRACEBACKREPLY._serialized_end=382
  _CPUPROFILINGREQUEST._serialized_start=385
  _CPUPROFILINGREQUEST._serialized_end=519
  _CPUPROFILINGREPLY._serialized_start=521
  _CPUPROFILINGREPLY._serialized_end=573
  _REPORTMETRICSREQUEST._serialized_start=575
  _REPORTMETRICSREQUEST._serialized_end=643
  _REPORTMETRICSREPLY._serialized_start=645
  _REPORTMETRICSREPLY._serialized_end=702
  _REPORTOCMETRICSREQUEST._serialized_start=704
  _REPORTOCMETRICSREQUEST._serialized_end=801
  _REPORTOCMETRICSREPLY._serialized_start=803
  _REPORTOCMETRICSREPLY._serialized_end=825
  _STREAMLOGREQUEST._serialized_start=828
  _STREAMLOGREQUEST._serialized_end=1039
  _STREAMLOGREPLY._serialized_start=1041
  _STREAMLOGREPLY._serialized_end=1071
  _LISTLOGSREQUEST._serialized_start=1073
  _LISTLOGSREQUEST._serialized_end=1111
  _LISTLOGSREPLY._serialized_start=1113
  _LISTLOGSREPLY._serialized_end=1147
  _REPORTERSERVICE._serialized_start=1150
  _REPORTERSERVICE._serialized_end=1564
  _LOGSERVICE._serialized_start=1567
  _LOGSERVICE._serialized_end=1708
# @@protoc_insertion_point(module_scope)
