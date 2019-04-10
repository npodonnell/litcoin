#!/usr/bin/env python3

from litcoin.serialization import ensure_enough_data

UINT64_SIZE_IN_BYTES = 8


def validate_uint64(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffff, '`n` must fit within 64 bits'


def serialize_uint64(n):
    validate_uint64(n)
    return int.to_bytes(n, UINT64_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint64(data, pos=0):
    ensure_enough_data(data, pos, UINT64_SIZE_IN_BYTES)
    next_pos = pos + UINT64_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder='little', signed=False)
    return (res, next_pos)
