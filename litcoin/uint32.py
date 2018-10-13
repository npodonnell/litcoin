#!/usr/bin/env python3

from litcoin.serialization import validate_data

UINT32_SIZE_IN_BYTES = 4


def validate_uint32(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffff, '`n` must fit within 32 bits'


def serialize_uint32(n):
    validate_uint32(n)
    return int.to_bytes(n, UINT32_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint32(data, i=0):
    validate_data(data, i, UINT32_SIZE_IN_BYTES)
    return int.from_bytes(data[i : i + UINT32_SIZE_IN_BYTES], byteorder='little', signed=False)
