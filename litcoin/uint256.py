#!/usr/bin/env python3

from .serialization import ensure_enough_data
from .binhex import x

UINT256_SIZE_IN_BYTES = 32


def validate_uint256(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, '`n` must fit within 256 bits'


def uint256_to_hex(n):
    validate_uint256(n)
    return x(serialize_uint256(n))


def serialize_uint256(n):
    validate_uint256(n)
    return int.to_bytes(n, UINT256_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint256(data, pos=0):
    ensure_enough_data(data, pos, UINT256_SIZE_IN_BYTES)
    next_pos = pos + UINT256_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder='little', signed=False)
    return (res, next_pos)
