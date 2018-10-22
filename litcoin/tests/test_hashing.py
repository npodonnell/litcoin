#!/usr/bin/env python3

from litcoin.hashing import single_sha, double_sha, hash160
import unittest


TEST_CASES = [
    { 
        'hex': '', 
        'single_sha': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'double_sha': '5df6e0e2761359d30a8275058e299fcc0381534545f55cf43e41983f5d4c9456',
        'hash160': 'b472a266d0bd89c13706a4132ccfb16f7c3b9fcb'
    },
    { 
        'hex': '00', 
        'single_sha': '6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d',
        'double_sha': '1406e05881e299367766d313e26c05564ec91bf721d31726bd6e46e60689539a',
        'hash160': '9f7fd096d37ed2c0e3f7f0cfc924beef4ffceb68'
    },
    { 
        'hex': 'c014', 
        'single_sha': 'a7947486b1ad9a4281645ceb1910c2126173f72a6f7926d5af7b6840092c4a4b',
        'double_sha': '1bb412767d2cf88d74ed9c028dad3afbcd52513137486cc3e39fcf8dbfcdf0a0',
        'hash160': 'eb07ebb0194eb36c024d73cb6a1d52d75d2d0a07'
    },
    { 
        'hex': '001400', 
        'single_sha': '593458868b6612185a9391ad4c065ab0ed3b16633759e26407632b83a0a2de82',
        'double_sha': '40ba5105abf072100bd8d3e0b4b5446281ad6c8ea42629c8100022336f64a465',
        'hash160': 'c9910198e241c31634785e88b869c4db6414d962'
    },
    { 
        'hex': '1289d0ca0b2108cbadefff9678acdd8760a8967876cdd876aaaacbdeeef7860a2a', 
        'single_sha': '3d40affad91d57640dc5b1343f4acc0be92f1f39fd10ccf51010d328034ae98e',
        'double_sha': '9734b0b8c4fc9719db5d5fe15ca9102ee6d9f3945bba9819c433c11964dd335c',
        'hash160': 'a7ead10f72ddee539382f2cfff6e523a8eab3608'
    }
]


class TestHashing(unittest.TestCase):
    def test_single_sha(self):
        for test_case in TEST_CASES:
            actual = bytes.fromhex(test_case['single_sha'])
            expected = single_sha(bytes.fromhex(test_case['hex']))
            assert actual == expected


    def test_double_sha(self):
        for test_case in TEST_CASES:
            actual = bytes.fromhex(test_case['double_sha'])
            expected = double_sha(bytes.fromhex(test_case['hex']))
            assert actual == expected
        

    def test_hash160(self):
        for test_case in TEST_CASES:
            actual = bytes.fromhex(test_case['hash160'])
            expected = hash160(bytes.fromhex(test_case['hex']))
            assert actual == expected
