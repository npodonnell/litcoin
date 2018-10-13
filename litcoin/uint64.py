#!/usr/bin/env python3

from litcoin.serialization import validate_data

UINT64_SIZE_IN_BYTES = 8


def validate_uint64(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffff, '`n` must fit within 64 bits'


def serialize_uint64(n):
    validate_uint64(n)
    return int.to_bytes(n, UINT64_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint64(data, i=0):
    validate_data(data, i, UINT64_SIZE_IN_BYTES)
    return int.from_bytes(data[i : i + UINT64_SIZE_IN_BYTES], byteorder='little', signed=False)
