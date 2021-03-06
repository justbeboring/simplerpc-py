# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bhello.proto\x12\x02pb\"\x17\n\x07Payload\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t22\n\x0cHelloService\x12\"\n\x04\x45\x63ho\x12\x0b.pb.Payload\x1a\x0b.pb.Payload\"\x00\x62\x06proto3'
)




_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='pb.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='pb.Payload.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=42,
)

DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOAD,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:pb.Payload)
  })
_sym_db.RegisterMessage(Payload)



_HELLOSERVICE = _descriptor.ServiceDescriptor(
  name='HelloService',
  full_name='pb.HelloService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=44,
  serialized_end=94,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='pb.HelloService.Echo',
    index=0,
    containing_service=None,
    input_type=_PAYLOAD,
    output_type=_PAYLOAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLOSERVICE)

DESCRIPTOR.services_by_name['HelloService'] = _HELLOSERVICE

# @@protoc_insertion_point(module_scope)
