# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pose_v.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import pose_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pose_v.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x0cpose_v.proto\x12\x0bgazebo.msgs\x1a\npose.proto\")\n\x06Pose_V\x12\x1f\n\x04pose\x18\x01 \x03(\x0b\x32\x11.gazebo.msgs.Pose')
  ,
  dependencies=[pose_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POSE_V = _descriptor.Descriptor(
  name='Pose_V',
  full_name='gazebo.msgs.Pose_V',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.Pose_V.pose', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=41,
  serialized_end=82,
)

_POSE_V.fields_by_name['pose'].message_type = pose_pb2._POSE
DESCRIPTOR.message_types_by_name['Pose_V'] = _POSE_V

Pose_V = _reflection.GeneratedProtocolMessageType('Pose_V', (_message.Message,), dict(
  DESCRIPTOR = _POSE_V,
  __module__ = 'pose_v_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Pose_V)
  ))
_sym_db.RegisterMessage(Pose_V)


# @@protoc_insertion_point(module_scope)
