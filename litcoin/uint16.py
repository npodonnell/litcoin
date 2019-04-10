#!/usr/bin/env python3

from litcoin.serialization import ensure_enough_data

UINT16_SIZE_IN_BYTES = 2


def validate_uint16(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffff, '`n` must fit within 16 bits'


def serialize_uint16(n):
    validate_uint16(n)
    return int.to_bytes(n, UINT16_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint16(data, pos=0):
    ensure_enough_data(data, pos, UINT16_SIZE_IN_BYTES)
    next_pos = pos + UINT16_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder='little', signed=False)
    return (res, next_pos)
