#!/usr/bin/env python3


def serialize_varint(n):
    assert type(n) == int
    assert 0 <= n

    if n <= 0xfc:
        return int.to_bytes(n, 1, byteorder='little', signed=False)
    if n <= 0xffff:
        return b'\xfd' + int.to_bytes(n, 2, byteorder='little', signed=False)
    if n <= 0xffffffff:
        return b'\xfe' + int.to_bytes(n, 4, byteorder='little', signed=False)
    if n <= 0xffffffffffffffff:
        return b'\xff' + int.to_bytes(n, 8, byteorder='little', signed=False)
    
    assert False


def deserialize_varint(data, i):
    assert type(data) == bytes
    assert type(i) == int
    assert i < len(data)

    f = int.from_bytes(data[i:i+1], byteorder='little', signed=False)

    if f <= 0xfc:
        return (f, 1)
    if f == 0xfd:
        assert i + 2 < len(data)
        return (int.from_bytes(data[i+1:i+3], byteorder='little', signed=False), 2)
    if f == 0xfe:
        assert i + 4 < len(data)
        return (int.from_bytes(data[i+1:i+5], byteorder='little', signed=False), 4)
    if f == 0xff:
        assert i + 8 < len(data)
        return (int.from_bytes(data[i+1:i+9], byteorder='little', signed=False), 8)
