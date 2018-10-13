#!/usr/bin/env python3

from litcoin.serialization import validate_data
from litcoin.uint16 import UINT16_SIZE_IN_BYTES, serialize_uint16, deserialize_uint16
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, serialize_uint32, deserialize_uint32
from litcoin.uint64 import UINT64_SIZE_IN_BYTES, serialize_uint64, deserialize_uint64

VARINT_SIZE_RANGE_IN_BYTES = (1, 9)


def validate_varint(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffff, '`n` must fit within 64 bits'


def serialize_varint(n):
    validate_varint(n)

    if n <= 0xfc:
        return int.to_bytes(n, 1, byteorder='little', signed=False)
    if n <= 0xffff:
        return b'\xfd' + int.to_bytes(n, 2, byteorder='little', signed=False)
    if n <= 0xffffffff:
        return b'\xfe' + int.to_bytes(n, 4, byteorder='little', signed=False)  
    return b'\xff' + int.to_bytes(n, 8, byteorder='little', signed=False)


def deserialize_varint(data, i=0):
    validate_data(data, i, VARINT_SIZE_RANGE_IN_BYTES[0])

    f = int.from_bytes(data[i : i + 1], byteorder='little', signed=False)

    if f <= 0xfc:
        return (f, 1)
    if f == 0xfd:
        assert i + UINT16_SIZE_IN_BYTES < len(data)
        return (deserialize_uint16(data, i + 1), UINT16_SIZE_IN_BYTES)
    if f == 0xfe:
        assert i + UINT32_SIZE_IN_BYTES < len(data)
        return (deserialize_uint32(data, i + 1), UINT32_SIZE_IN_BYTES)
    if f == 0xff:
        assert i + UINT64_SIZE_IN_BYTES < len(data)
        return (deserialize_uint64(data, i + 1), UINT64_SIZE_IN_BYTES)
