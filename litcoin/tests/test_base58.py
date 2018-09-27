#!/usr/bin/env python3

from litcoin.base58 import base58_encode, base58_decode

TEST_CASES = [
    {'hex': '', 'b58': ''},
    {'hex': '00', 'b58': '1'},
    {'hex': '01', 'b58': '2'},
    {'hex': '0000', 'b58': '11'},
    {'hex': '000100', 'b58': '15R'},
    {'hex': '00010001', 'b58': '1LUx'},
    {'hex': 'ff', 'b58': '5Q'},
    {'hex': 'ffff', 'b58': 'LUv'},
    {'hex': '0102030405060708090a0b0c0d0e0f', 'b58': '2drXXUifSrRnXLGbXg8E'}
]

def test_base58_encode():
    for test_case in TEST_CASES:
        actual = base58_encode(bytes.fromhex(test_case['hex']))
        expected = test_case['b58']
        assert actual == expected

def test_base58_decode():
    for test_case in TEST_CASES:
        actual = base58_decode(test_case['b58'])
        expected = bytes.fromhex(test_case['hex'])
        assert actual == expected
