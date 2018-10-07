#!/usr/bin/env python3


def serialize_uint256(n):
    assert type(n) == int
    assert 0 <= n
    assert n <= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    return int.to_bytes(n, 32, byteorder='little', signed=False)


def deserialize_uint256(data, i=0):
    assert type(data) == bytes
    assert type(i) == int
    assert 0 <= i
    assert i + 31 < len(data)
    return int.from_bytes(data[i:i+32], byteorder='little', signed=False)
