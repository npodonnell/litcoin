#!/usr/bin/env python3

def validate_uint32(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffff, '`n` must fit within 32 bits'


def serialize_uint32(n):
    validate_uint32(n)
    return int.to_bytes(n, 4, byteorder='little', signed=False)


def deserialize_uint32(data, i=0):
    assert type(data) == bytes
    assert type(i) == int
    assert 0 <= i
    assert i + 4 <= len(data)
    return int.from_bytes(data[i:i+4], byteorder='little', signed=False)
