# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sum.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsum.proto\x12\x03sum\"\"\n\nSumRequest\x12\t\n\x01\x61\x18\x01 \x01(\x03\x12\t\n\x01\x62\x18\x02 \x01(\x03\"\x1d\n\x0bSumResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03\x32\x38\n\nSumService\x12*\n\x03Sum\x12\x0f.sum.SumRequest\x1a\x10.sum.SumResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sum_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUMREQUEST._serialized_start=18
  _SUMREQUEST._serialized_end=52
  _SUMRESPONSE._serialized_start=54
  _SUMRESPONSE._serialized_end=83
  _SUMSERVICE._serialized_start=85
  _SUMSERVICE._serialized_end=141
# @@protoc_insertion_point(module_scope)
