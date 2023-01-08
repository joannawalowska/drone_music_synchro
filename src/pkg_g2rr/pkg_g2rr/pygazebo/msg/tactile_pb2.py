# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tactile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import time_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tactile.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\rtactile.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\"j\n\x07Tactile\x12\x16\n\x0e\x63ollision_name\x18\x01 \x03(\t\x12\x14\n\x0c\x63ollision_id\x18\x02 \x03(\r\x12\x10\n\x08pressure\x18\x03 \x03(\x01\x12\x1f\n\x04time\x18\x04 \x02(\x0b\x32\x11.gazebo.msgs.Time')
  ,
  dependencies=[time_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TACTILE = _descriptor.Descriptor(
  name='Tactile',
  full_name='gazebo.msgs.Tactile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collision_name', full_name='gazebo.msgs.Tactile.collision_name', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_id', full_name='gazebo.msgs.Tactile.collision_id', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pressure', full_name='gazebo.msgs.Tactile.pressure', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='gazebo.msgs.Tactile.time', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=148,
)

_TACTILE.fields_by_name['time'].message_type = time_pb2._TIME
DESCRIPTOR.message_types_by_name['Tactile'] = _TACTILE

Tactile = _reflection.GeneratedProtocolMessageType('Tactile', (_message.Message,), dict(
  DESCRIPTOR = _TACTILE,
  __module__ = 'tactile_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Tactile)
  ))
_sym_db.RegisterMessage(Tactile)


# @@protoc_insertion_point(module_scope)
