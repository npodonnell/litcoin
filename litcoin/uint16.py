#!/usr/bin/env python3

from litcoin.serialization import validate_data

UINT16_SIZE_IN_BYTES = 2


def validate_uint16(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffff, '`n` must fit within 16 bits'


def serialize_uint16(n):
    validate_uint16(n)
    return int.to_bytes(n, UINT16_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint16(data, i=0):
    validate_data(data, i, UINT16_SIZE_IN_BYTES)
    return int.from_bytes(data[i : i + UINT16_SIZE_IN_BYTES], byteorder='little', signed=False)
