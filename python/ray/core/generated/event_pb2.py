# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csrc/ray/protobuf/event.proto\x12\x07ray.rpc\"\x82\x04\n\x05\x45vent\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12.\n\x0bsource_type\x18\x02 \x01(\x0e\x32\x19.ray.rpc.Event.SourceType\x12\x17\n\x0fsource_hostname\x18\x03 \x01(\t\x12\x12\n\nsource_pid\x18\x04 \x01(\x05\x12)\n\x08severity\x18\x05 \x01(\x0e\x32\x17.ray.rpc.Event.Severity\x12\r\n\x05label\x18\x06 \x01(\t\x12\x0f\n\x07message\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x08 \x01(\x03\x12\x37\n\rcustom_fields\x18\t \x03(\x0b\x32 .ray.rpc.Event.CustomFieldsEntry\x1a\x33\n\x11\x43ustomFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"o\n\nSourceType\x12\n\n\x06\x43OMMON\x10\x00\x12\x0f\n\x0b\x43ORE_WORKER\x10\x01\x12\x07\n\x03GCS\x10\x02\x12\n\n\x06RAYLET\x10\x03\x12\x15\n\x11\x43LUSTER_LIFECYCLE\x10\x04\x12\x0e\n\nAUTOSCALER\x10\x05\x12\x08\n\x04JOBS\x10\x06\"M\n\x08Severity\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\t\n\x05\x46\x41TAL\x10\x03\x12\t\n\x05\x44\x45\x42UG\x10\x04\x12\t\n\x05TRACE\x10\x05\")\n\x11ReportEventsReply\x12\x14\n\x0csend_success\x18\x01 \x01(\x08\",\n\x13ReportEventsRequest\x12\x15\n\revent_strings\x18\x01 \x03(\t2^\n\x12ReportEventService\x12H\n\x0cReportEvents\x12\x1c.ray.rpc.ReportEventsRequest\x1a\x1a.ray.rpc.ReportEventsReplyB\x03\xf8\x01\x01\x62\x06proto3')



_EVENT = DESCRIPTOR.message_types_by_name['Event']
_EVENT_CUSTOMFIELDSENTRY = _EVENT.nested_types_by_name['CustomFieldsEntry']
_REPORTEVENTSREPLY = DESCRIPTOR.message_types_by_name['ReportEventsReply']
_REPORTEVENTSREQUEST = DESCRIPTOR.message_types_by_name['ReportEventsRequest']
_EVENT_SOURCETYPE = _EVENT.enum_types_by_name['SourceType']
_EVENT_SEVERITY = _EVENT.enum_types_by_name['Severity']
Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'CustomFieldsEntry' : _reflection.GeneratedProtocolMessageType('CustomFieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_CUSTOMFIELDSENTRY,
    '__module__' : 'src.ray.protobuf.event_pb2'
    # @@protoc_insertion_point(class_scope:ray.rpc.Event.CustomFieldsEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'src.ray.protobuf.event_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.CustomFieldsEntry)

ReportEventsReply = _reflection.GeneratedProtocolMessageType('ReportEventsReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTEVENTSREPLY,
  '__module__' : 'src.ray.protobuf.event_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportEventsReply)
  })
_sym_db.RegisterMessage(ReportEventsReply)

ReportEventsRequest = _reflection.GeneratedProtocolMessageType('ReportEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTEVENTSREQUEST,
  '__module__' : 'src.ray.protobuf.event_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportEventsRequest)
  })
_sym_db.RegisterMessage(ReportEventsRequest)

_REPORTEVENTSERVICE = DESCRIPTOR.services_by_name['ReportEventService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _EVENT_CUSTOMFIELDSENTRY._options = None
  _EVENT_CUSTOMFIELDSENTRY._serialized_options = b'8\001'
  _EVENT._serialized_start=42
  _EVENT._serialized_end=556
  _EVENT_CUSTOMFIELDSENTRY._serialized_start=313
  _EVENT_CUSTOMFIELDSENTRY._serialized_end=364
  _EVENT_SOURCETYPE._serialized_start=366
  _EVENT_SOURCETYPE._serialized_end=477
  _EVENT_SEVERITY._serialized_start=479
  _EVENT_SEVERITY._serialized_end=556
  _REPORTEVENTSREPLY._serialized_start=558
  _REPORTEVENTSREPLY._serialized_end=599
  _REPORTEVENTSREQUEST._serialized_start=601
  _REPORTEVENTSREQUEST._serialized_end=645
  _REPORTEVENTSERVICE._serialized_start=647
  _REPORTEVENTSERVICE._serialized_end=741
# @@protoc_insertion_point(module_scope)
