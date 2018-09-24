#!/usr/bin/env python3

from litcoin.base58 import base58_encode

def test_base58_encode():
    actual = base58_encode(b'')
    expected = ''
    assert(actual == expected)

    actual = base58_encode(bytes.fromhex('3a'))
    expected = '21'
    assert(actual == expected)

    actual = base58_encode(bytes.fromhex('0001'))
    expected = '12'
    assert(actual == expected)

    actual = base58_encode(b'litcoin')
    expected = '57HQmfS6vq'
    assert(actual == expected)


def test_base58_decode():
    pass