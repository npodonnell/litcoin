#!/usr/bin/env python3

from litcoin.serialization import validate_data

INT64_SIZE_IN_BYTES = 8


def validate_int64(n):
    assert type(n) == int, 'type of `n` should be int'
    assert -0x7fffffffffffffff <= n and n <= 0x7fffffffffffffff, '`n` must fit within 64 bits'


def serialize_int64(n):
    validate_int64(n)
    return int.to_bytes(n, INT64_SIZE_IN_BYTES, byteorder='little', signed=True)


def deserialize_int64(data, i=0):
    validate_data(data, i, INT64_SIZE_IN_BYTES)
    return int.from_bytes(data[i : i + INT64_SIZE_IN_BYTES], byteorder='little', signed=True)
