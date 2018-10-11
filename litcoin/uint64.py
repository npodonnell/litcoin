#!/usr/bin/env python3

def validate_uint64(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffff, '`n` must fit within 64 bits'


def serialize_uint64(n):
    validate_uint64(n)
    return int.to_bytes(n, 8, byteorder='little', signed=False)


def deserialize_uint64(data, i=0):
    assert type(data) == bytes
    assert type(i) == int
    assert 0 <= i
    assert i + 8 <= len(data)
    return int.from_bytes(data[i:i+8], byteorder='little', signed=False)
