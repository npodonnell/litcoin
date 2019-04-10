#!/usr/bin/env python3

from litcoin.serialization import ensure_enough_data

INT32_SIZE_IN_BYTES = 4


def validate_int32(n):
    assert type(n) == int, 'type of `n` should be int'
    assert -0x7fffffff <= n and n <= 0x7fffffff, '`n` must fit within 32 bits'


def serialize_int32(n):
    validate_int32(n)
    return int.to_bytes(n, INT32_SIZE_IN_BYTES, byteorder='little', signed=True)


def deserialize_int32(data, pos=0):
    ensure_enough_data(data, pos, INT32_SIZE_IN_BYTES)
    next_pos = pos + INT32_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder='little', signed=True)
    return (res, next_pos)
