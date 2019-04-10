#!/usr/bin/env python3

from litcoin.serialization import validate_data

INT32_SIZE_IN_BYTES = 4


def validate_int32(n):
    assert type(n) == int, 'type of `n` should be int'
    assert -0x7fffffff <= n and n <= 0x7fffffff, '`n` must fit within 32 bits'


def serialize_int32(n):
    validate_int32(n)
    return int.to_bytes(n, INT32_SIZE_IN_BYTES, byteorder='little', signed=True)


def deserialize_int32(data, i=0):
    validate_data(data, i, INT32_SIZE_IN_BYTES)
    return int.from_bytes(data[i : i + INT32_SIZE_IN_BYTES], byteorder='little', signed=True)
