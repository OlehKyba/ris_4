# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ris_4.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bris_4.proto\x12\x05ris_4\"*\n\x1a\x44\x65\x63reaseByOneLetterRequest\x12\x0c\n\x04word\x18\x01 \x01(\t\"3\n\x1b\x44\x65\x63reaseByOneLetterResponse\x12\x14\n\x0cis_decreased\x18\x01 \x01(\x08\x32k\n\x0bRIS4Service\x12\\\n\x13\x44\x65\x63reaseByOneLetter\x12!.ris_4.DecreaseByOneLetterRequest\x1a\".ris_4.DecreaseByOneLetterResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ris_4_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DECREASEBYONELETTERREQUEST._serialized_start=22
  _DECREASEBYONELETTERREQUEST._serialized_end=64
  _DECREASEBYONELETTERRESPONSE._serialized_start=66
  _DECREASEBYONELETTERRESPONSE._serialized_end=117
  _RIS4SERVICE._serialized_start=119
  _RIS4SERVICE._serialized_end=226
# @@protoc_insertion_point(module_scope)