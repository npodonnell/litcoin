#!/usr/bin/env python3

from litcoin.serialization import ensure_enough_data

UINT8_SIZE_IN_BYTES = 1


def validate_uint8(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xff, '`n` must fit within 8 bits'


def serialize_uint8(n):
    validate_uint8(n)
    return int.to_bytes(n, UINT8_SIZE_IN_BYTES, byteorder='little', signed=False)


def deserialize_uint8(data, pos=0):
    ensure_enough_data(data, pos, UINT8_SIZE_IN_BYTES)
    next_pos = pos + UINT8_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder='little', signed=False)
    return (res, next_pos)


def uint8_to_bytes(n: int) -> bytes:
    validate_uint8(n)
    return int.to_bytes(n, UINT8_SIZE_IN_BYTES, byteorder='big', signed=False)
