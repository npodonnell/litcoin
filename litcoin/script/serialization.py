#!/usr/bin/env python3

from ..varint import VARINT_SIZE_RANGE_IN_BYTES, serialize_varint, deserialize_varint
from ..serialization import ensure_enough_data

SCRIPT_SERIALIZED_MIN_SIZE = VARINT_SIZE_RANGE_IN_BYTES[0]


def serialize_script(script):
    assert type(script) is bytes, "Script should be `bytes` type"
    return serialize_varint(len(script)) + script


def deserialize_script(data, pos=0):
    ensure_enough_data(data, pos, SCRIPT_SERIALIZED_MIN_SIZE)
    (script_length, pos) = deserialize_varint(data, pos)
    next_pos = pos + script_length
    assert next_pos <= len(data), "Not enough data remaining to hold {0} bytes of script".format(script_length)
    return (data[pos : next_pos], next_pos)
