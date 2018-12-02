#!/usr/bin/env python3

from litcoin.serialization import validate_data

UINT8_SIZE_IN_BYTES = 1


def validate_uint8(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xff, '`n` must fit within 8 bits'


def serialize_uint8(n):
    validate_uint8(n)
    return int.to_bytes(n, UINT8_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint8(data, i=0):
    validate_data(data, i, UINT8_SIZE_IN_BYTES)
    return int.from_bytes(data[i : i + UINT8_SIZE_IN_BYTES], byteorder='little', signed=False)
