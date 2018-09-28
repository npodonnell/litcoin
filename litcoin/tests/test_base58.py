#!/usr/bin/env python3

from litcoin.base58 import base58_encode, base58_decode


TEST_CASES = [
    {'hex': '', 'base58': ''},
    {'hex': '00', 'base58': '1'},
    {'hex': '01', 'base58': '2'},
    {'hex': '0000', 'base58': '11'},
    {'hex': '000100', 'base58': '15R'},
    {'hex': '00010001', 'base58': '1LUx'},
    {'hex': 'ff', 'base58': '5Q'},
    {'hex': 'ffff', 'base58': 'LUv'},
    {'hex': '0102030405060708090a0b0c0d0e0f', 'base58': '2drXXUifSrRnXLGbXg8E'}
]


def test_base58_encode():
    for test_case in TEST_CASES:
        actual = base58_encode(bytes.fromhex(test_case['hex']))
        expected = test_case['base58']
        assert actual == expected


def test_base58_decode():
    for test_case in TEST_CASES:
        actual = base58_decode(test_case['base58'])
        expected = bytes.fromhex(test_case['hex'])
        assert actual == expected
