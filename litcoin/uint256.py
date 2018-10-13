#!/usr/bin/env python3

from litcoin.serialization import validate_data

UINT256_SIZE_IN_BYTES = 32


def validate_uint256(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, '`n` must fit within 256 bits'


def serialize_uint256(n):
    validate_uint256(n)
    return int.to_bytes(n, UINT256_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint256(data, i=0):
    validate_data(data, i, UINT256_SIZE_IN_BYTES)
    return int.from_bytes(data[i : i + UINT256_SIZE_IN_BYTES], byteorder='little', signed=False)
