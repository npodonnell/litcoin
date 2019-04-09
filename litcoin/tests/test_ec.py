#!/usr/bin/env python3

from litcoin.ec import PRIVKEY_SIZE_BYTES, UNCOMPRESSED_PUBKEY_SIZE_BYTES, \
    COMPRESSED_PUBKEY_SIZE_BYTES, validate_privkey, validate_pubkey, \
    make_privkey, derive_pubkey, sign_message, verify_signature
from litcoin.binhex import b, x
import unittest

VALID_PRIVKEY = b('7fb4f6e09d5344c46b4551fe08af8033d5d5864d9bbe551f282a574c928e945b')

TOO_SHORT_PRIVKEY = b('7fb4f6e09d5344c46b4551fe08af8033d5d5864d9bbe551f282a574c928e94')
TOO_LONG_PRIVKEY = b('7fb4f6e09d5344c46b4551fe08af8033d5d5864d9bbe551f282a574c928e945bff')

VALID_UNCOMPRESSED_PUBKEY = b('041d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa12bc93b5e89d20236bb095d00f580821b2c4034cf3b35b5b2e6bc89a5f09ec8a19a')
VALID_COMPRESSED_PUBKEY = b('021d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa12b')

TOO_SHORT_UNCOMPRESSED_PUBKEY = b('041d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa12bc93b5e89d20236bb095d00f580821b2c4034cf3b35b5b2e6bc89a5f09ec8a1')
TOO_LONG_UNCOMPRESSED_PUBKEY = b('041d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa12bc93b5e89d20236bb095d00f580821b2c4034cf3b35b5b2e6bc89a5f09ec8a19a34')
WRONG_LEADING_BYTE_UNCOMPRESSED_PUBKEY = b('031d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa12bc93b5e89d20236bb095d00f580821b2c4034cf3b35b5b2e6bc89a5f09ec8a19a')
TOO_SHORT_COMPRESSED_PUBKEY = b('021d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa1')
TOO_LONG_COMPRESSED_PUBKEY = b('021d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa12b42')
WRONG_LEADING_BYTE_COMPRESSED_PUBKEY = b('041d5219a13f0f23ebbd8e88abe9ab9eac77f9daaa859cfff0580279a15d9aa12b')


class TestEc(unittest.TestCase):
    def test_validate_privkey(self):
        validate_privkey(VALID_PRIVKEY)

        with self.assertRaises(AssertionError, msg='Should be raised because `privkey` is too short'):
            validate_privkey(TOO_SHORT_PRIVKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `privkey` is too long'):
            validate_privkey(TOO_LONG_PRIVKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `privkey` is wrong type'):
            validate_privkey('wrong type')


    def test_validate_pubkey(self):
        validate_pubkey(VALID_UNCOMPRESSED_PUBKEY)
        validate_pubkey(VALID_COMPRESSED_PUBKEY)

        with self.assertRaises(AssertionError, msg='Should be raised because `pubkey` (uncompressed) is too short'):
            validate_pubkey(TOO_SHORT_UNCOMPRESSED_PUBKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `pubkey` (uncompressed) is too long'):
            validate_pubkey(TOO_LONG_UNCOMPRESSED_PUBKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `pubkey` (uncompressed) has wrong leading byte'):
            validate_pubkey(WRONG_LEADING_BYTE_UNCOMPRESSED_PUBKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `pubkey` (compressed) is too short'):
            validate_pubkey(TOO_SHORT_COMPRESSED_PUBKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `pubkey` (compressed) is too long'):
            validate_pubkey(TOO_LONG_COMPRESSED_PUBKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `pubkey` (compressed) has wrong leading byte'):
            validate_pubkey(WRONG_LEADING_BYTE_COMPRESSED_PUBKEY)
        with self.assertRaises(AssertionError, msg='Should be raised because `pubkey` is wrong type'):
            validate_pubkey('wrong type')


    def test_make_privkey(self):
        privkey1 = make_privkey()
        privkey2 = make_privkey()
        assert type(privkey1) == bytes
        assert type(privkey2) == bytes
        assert len(privkey1) == PRIVKEY_SIZE_BYTES
        assert len(privkey2) == PRIVKEY_SIZE_BYTES
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

        with self.assertRaises(AssertionError, msg='Should be raised because passphrase is incorrect type'):
            make_privkey(passphrase=42)


    def test_derive_pubkey(self):
        actual = derive_pubkey(VALID_PRIVKEY, True)
        expected = VALID_COMPRESSED_PUBKEY
        assert actual == expected, 'Failed to derive compressed pubkey'

        actual = derive_pubkey(VALID_PRIVKEY, False)
        expected = VALID_UNCOMPRESSED_PUBKEY
        assert actual == expected, 'Failed to derive uncompressed pubkey'


    def test_sign_message(self):
        privkey = b("1744903d5062e0fe6b92a2df283495f99e16e9f42546c69be2be4349b658727b")
        hashed_message = b("70bc18bef5ae66b72d1995f8db90a583a60d77b4066e4653f1cead613025861c")

        signature = sign_message(hashed_message, privkey)
        assert type(signature) is bytes, "`signature` should be of type `bytes`"

    def test_verify_signature(self):
        pubkey = b("02c7a6af8f2e3663cfd9fe112303042fdaa6e693e753d4f2c57d45534b88aae838")
        hashed_message = b("70bc18bef5ae66b72d1995f8db90a583a60d77b4066e4653f1cead613025861c")
        
        signature = b("30460221008b409a819a0e99e2ba8d310b4184de6b62a1c6aa49d36512702591c7d4c2b27b022100fc73f7785b8163beb589543cb1ae6ca0a03fc5d4b4572423b1b7b28a623ad1ec")
        actual = verify_signature(signature, hashed_message, pubkey)
        expected = True
        assert actual == expected, "Failed to get expected positive result for signature verification"

        signature = b("30460221008b409a819a0e99e2ba8d310b3184de6b62a1c6aa49d36512702591c7d4c2b27b022100fc73f7785b8163beb589543cb1ae6ca0a03fc5d4b4572423b1b7b28a623ad1ec")
        actual = verify_signature(signature, hashed_message, pubkey)
        expected = False
        assert actual == expected, "Failed to get expected positive result for signature verification"
