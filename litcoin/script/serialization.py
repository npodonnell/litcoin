#!/usr/bin/env python3

from ..varint import VARINT_SIZE_RANGE_IN_BYTES, serialize_varint, deserialize_varint
from ..serialization import validate_data

SCRIPT_SERIALIZED_MIN_SIZE = VARINT_SIZE_RANGE_IN_BYTES[0]

def serialize_script(script):
    assert type(script) is bytes, "Script should be `bytes` type"
    return serialize_varint(len(script)) + script


def deserialize_script(data, i=0):
    validate_data(data, i, SCRIPT_SERIALIZED_MIN_SIZE)
    (script_length, script_length_length) = deserialize_varint(data, i)
    i += script_length_length
    assert i + script_length <= len(data), \
        "Not enough data remaining to hold {0} bytes of script".format(script_length)
    return (data[i : i + script_length], script_length + script_length_length)
