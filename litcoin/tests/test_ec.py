#!/usr/bin/env python3

from litcoin.ec import validate_privkey, compress_ec_point, make_privkey, derive_pubkey, sign_message, \
    verify_signature
from litcoin.binhex import b
import unittest

VALID_PRIVKEY = '7fb4f6e09d5344c46b4551fe08af8033d5d5864d9bbe551f282a574c928e945b'
NONHEX_PRIVKEY = '7gb4f6e09d5344c46b4551fe08af8033d5d5864d9bbe551f282a574c928e945b'
TOO_SHORT_PRIVKEY = '8be5d14cf68e613515a2ee1a6f09f34f9f567d6ed68e72eb5768b6dfd19a61'
TOO_LONG_PRIVKEY = 'd5ebe46d38e62125e31739cd3de9efbd90e6d9be1cca7d4d66e5bc666cb995fe41'

class TestEc(unittest.TestCase):
    def test_validate_privkey(self):
        validate_privkey(b(VALID_PRIVKEY))

        with self.assertRaises(AssertionError, msg='should be raised because `privkey` contains non-hex character'):
            validate_privkey(b(NONHEX_PRIVKEY))
        with self.assertRaises(AssertionError, msg='should be raised because `privkey` is too short'):
            validate_privkey(b(TOO_SHORT_PRIVKEY))
        with self.assertRaises(AssertionError, msg='should be raised because `privkey` is too long'):
            validate_privkey(b(TOO_LONG_PRIVKEY))
        with self.assertRaises(AssertionError, msg='should be raised because `privkey` is wrong type'):
            validate_privkey(VALID_PRIVKEY)
        with self.assertRaises(TypeError, msg='should be raised because `privkey` is not present'):
            validate_privkey()


    def test_compress_ec_point(self):
        actual = compress_ec_point(0, 0)
        expected = b('020000000000000000000000000000000000000000000000000000000000000000')
        assert actual == expected

        actual = compress_ec_point(0, 1)
        expected = b('030000000000000000000000000000000000000000000000000000000000000000')
        assert actual == expected

        actual = compress_ec_point(1, 0)
        expected = b('020000000000000000000000000000000000000000000000000000000000000001')
        assert actual == expected

        actual = compress_ec_point(1, 1)
        expected = b('030000000000000000000000000000000000000000000000000000000000000001')
        assert actual == expected

        actual = compress_ec_point(1, 1)
        expected = b('030000000000000000000000000000000000000000000000000000000000000001')
        assert actual == expected


    def test_make_privkey(self):
        for _ in range(0, 1000):
            privkey1 = make_privkey()
            privkey2 = make_privkey()
            assert type(privkey1) == bytes
            assert type(privkey2) == bytes
            assert len(privkey1) == 32
            assert len(privkey2) == 32
            assert privkey1 != privkey2

        actual = make_privkey(passphrase='')
        expected = b('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')
        assert actual == expected

        actual = make_privkey(passphrase='bitcoin')
        expected = b('6b88c087247aa2f07ee1c5956b8e1a9f4c7f892a70e324f1bb3d161e05ca107b')
        assert actual == expected

        actual = make_privkey(passphrase='litecoin')
        expected = b('6ce9fe4549f0f60d6fcc7697681ec2e6ed2eade066c3f6829628a59ce5cfc64b')
        assert actual == expected

        actual = make_privkey(passphrase='litcoin')
        expected = b('83154786b09476e9221d30bb1f98cb678c02bc8ddc97deeb654f6dcd93f95474')
        assert actual == expected


    def test_derive_pubkey(self):
        actual = derive_pubkey(b('7cf3547ccfbf3b17d3eae42256396c0544714b0df4f8c8c4268a3e2d705eaf73'))
        expected = b('02172204d37ae71933f2595bc74eb90e984254759c560245d8bf523e0d60c1477b')
        assert actual == expected

        actual = derive_pubkey(b('0ec786c41a15ced8b1d018539cdcbdc50c40e733a9ba6775ce5733d75bb78a42'))
        expected = b('032be7848317b80628112869f4da0edfbc1f4ca9539a8c94355bad5961a36d33d6')
        assert actual == expected


    def test_sign_message(self):
        pass


    def test_verify_message(self):
        pass
