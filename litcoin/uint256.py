#!/usr/bin/env python3

def is_uint256(n):
    return (type(n) == int) and (0 <= n) and (n <= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)


def serialize_uint256(n):
    assert is_uint256(n)
    return int.to_bytes(n, 32, byteorder='little', signed=False)


def deserialize_uint256(data, i=0):
    assert type(data) == bytes
    assert type(i) == int
    assert 0 <= i
    assert i + 31 < len(data)
    return int.from_bytes(data[i:i+32], byteorder='little', signed=False)
