#!/usr/bin/env python3


def serialize_uint32(n):
    assert type(n) == int
    assert 0 <= n
    assert n <= 0xffffffff
    return int.to_bytes(n, 4, byteorder='little', signed=False)


def deserialize_uint32(data, i=0):
    assert type(data) == bytes
    assert type(i) == int
    assert 0 <= i
    assert i + 3 < len(data)
    return int.from_bytes(data[i:i+4], byteorder='little', signed=False)
