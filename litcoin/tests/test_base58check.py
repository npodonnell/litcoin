#!/usr/bin/env python3

from litcoin.base58check import base58check_encode, base58check_decode

TEST_CASES = [
    {'hex': '', 'b58c': '3QJmnh'},
    {'hex': '00', 'b58c': '1Wh4bh'},
    {'hex': '01', 'b58c': 'BXvDbH'},
    {'hex': '0000', 'b58c': '112edB6q'},
    {'hex': '000100', 'b58c': '1Vyy3ex3'},
    {'hex': '00010001', 'b58c': '13CUzk4iA2'},
    {'hex': 'ff', 'b58c': 'VrZDWwe'},
    {'hex': 'ffff', 'b58c': '3CUsNEUP5'},
    {'hex': '0102030405060708090a0b0c0d0e0f', 'b58c': 'Bhh3pU9gLXZiNDL6PEZxnvuRw'}
]

def test_base58check_encode():
    for test_case in TEST_CASES:
        actual = base58check_encode(bytes.fromhex(test_case['hex']))
        expected = test_case['b58c']
        assert actual == expected

def test_base58check_decode():
    for test_case in TEST_CASES:
        actual = base58check_decode(test_case['b58c'])
        expected = bytes.fromhex(test_case['hex'])
        assert actual == expected
