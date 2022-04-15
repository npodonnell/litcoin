#!/usr/bin/env python3

from .serialization import ensure_enough_data
from .binhex import b, x

UINT256_SIZE_IN_BYTES = 32


def validate_uint256(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, '`n` must fit within 256 bits'


def serialize_uint256(n):
    validate_uint256(n)
    return int.to_bytes(n, UINT256_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint256(data, pos=0):
    ensure_enough_data(data, pos, UINT256_SIZE_IN_BYTES)
    next_pos = pos + UINT256_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder='little', signed=False)
    return (res, next_pos)


def uint256_to_bytes(n: int) -> bytes:
    validate_uint256(n)
    return int.to_bytes(n, UINT256_SIZE_IN_BYTES, byteorder='big', signed=False)
    

def uint256_from_bytes(b: bytes) -> int:
    assert type(b) is bytes, "`b` should be of type `bytes`"
    assert len(b) == 32, "`b` should be of length 32"
    return int.from_bytes(b, byteorder='big', signed=False)


def uint256_to_hex(n):
    validate_uint256(n)
    return x(int.to_bytes(n, UINT256_SIZE_IN_BYTES, byteorder='big', signed=False))


def uint256_from_hex(s):
    assert type(s) is str, "`s` should be of type `str`"
    assert len(s) == 64, "`s` should be of length 64"
    return int.from_bytes(b(s), byteorder='big', signed=False)
