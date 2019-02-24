#!/usr/bin/env python3

from litcoin.binhex import b
from litcoin.txid import TXID_SIZE_IN_BYTES, make_txid, validate_txid, serialize_txid, deserialize_txid
import unittest


class TestTxid(unittest.TestCase):
    def test_TXID_SIZE_IN_BYTES(self):
        assert TXID_SIZE_IN_BYTES == 32

    def test_make_txid(self):
        actual = make_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"))
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected

        actual = make_txid("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected

        actual = make_txid(0xbc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52)
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected

        with self.assertRaises(ValueError, msg='should be raised because `input` argument is a too short byte array'):
            make_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b"))
        with self.assertRaises(ValueError, msg='should be raised because `input` argument is a too long byte array'):
            make_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b5223"))
        with self.assertRaises(ValueError, msg='should be raised because `input` argument is invalid, non-hex string'):
            make_txid("I am not hex")
        with self.assertRaises(ValueError, msg='should be raised because `input` argument is a negative integer'):
            make_txid(-0xbc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52)
        with self.assertRaises(ValueError, msg='should be raised because `input` argument is a greater than 256-bit integer'):
            make_txid(0x10000000000000000000000000000000000000000000000000000000000000000)

    def test_validate_txid(self):
        validate_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"))

        with self.assertRaises(AssertionError, msg="should be raised because txid is too short"):
            validate_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b"))
        with self.assertRaises(AssertionError, msg="should be raised because txid is too long"):
            validate_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b5223"))

    def test_serialize_txid(self):
        actual = serialize_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"))
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected
    
    def test_deserialize_txid(self):
        actual = deserialize_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"))
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected

        actual = deserialize_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"), 0)
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected

        actual = deserialize_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52cc"), 0)
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected

        actual = deserialize_txid(b("ccbc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"), 1)
        expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
        assert actual == expected

        with self.assertRaises(AssertionError, msg="should be raised because `i` argument is negative"):
            deserialize_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"), -1)
        with self.assertRaises(AssertionError, msg="should be raised because `data` argument is 31 bytes long"):
            deserialize_txid(b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b"))
        with self.assertRaises(AssertionError, msg="should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized"):
            actual = deserialize_txid(b("ccbc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"), 0)
            expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
            assert actual == expected
        with self.assertRaises(AssertionError, msg="should be raised because `i` argument is 2 when it should be 1 thus there's an overflow"):
            actual = deserialize_txid(b("ccbc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52"), 2)
            expected = b("bc008e61ff421ce00705f939af8f8b300395e55d3e72ffd77ba68f9ebc7f3b52")
            assert actual == expected
        with self.assertRaises(AssertionError, msg="should be raised because `data` argument is of the wrong type"):
            deserialize_txid("wrong type")
        with self.assertRaises(TypeError, msg="should be raised because all arguments are missing"):
            deserialize_txid()
