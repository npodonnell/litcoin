#!/usr/bin/env python3

from litcoin.serialization import ensure_enough_data

UINT32_SIZE_IN_BYTES = 4


def validate_uint32(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffff, '`n` must fit within 32 bits'


def serialize_uint32(n):
    validate_uint32(n)
    return int.to_bytes(n, UINT32_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint32(data, pos=0):
    ensure_enough_data(data, pos, UINT32_SIZE_IN_BYTES)
    next_pos = pos + UINT32_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder='little', signed=False)
    return (res, next_pos)
