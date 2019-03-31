#!/usr/bin/env python3

from litcoin.uint64 import UINT64_SIZE_IN_BYTES, serialize_uint64
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES, serialize_varint
from litcoin.script.serialization import serialize_script
from litcoin.txoutput import TXOUTPUT_SIZE_RANGE_IN_BYTES, make_txoutput, validate_txoutput, \
    serialize_txoutput, deserialize_txoutput, txoutput_to_human_readable, txoutput_copy
from litcoin.binhex import b
from litcoin.script.humanreadable import script_to_human_readable
import unittest

VALUE = 42
LOCKING_SCRIPT = b('')


class TestTxoutput(unittest.TestCase):
    def test_TXOUTPUT_SIZE_RANGE_IN_BYTES(self):
        assert TXOUTPUT_SIZE_RANGE_IN_BYTES == (UINT64_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0],)

    def test_make_txoutput(self):
        actual = make_txoutput(VALUE, LOCKING_SCRIPT)
        expected = {'value': VALUE, 'locking_script': LOCKING_SCRIPT}
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because `value` argument is the wrong type'):
            make_txoutput(42.0, LOCKING_SCRIPT)
        with self.assertRaises(AssertionError, msg='should be raised because `locking_script` argument is the wrong type'):
            make_txoutput(VALUE, 'wrong type')
        with self.assertRaises(TypeError, msg='should be raised because `locking_script` argument is missing'):
            make_txoutput(VALUE)
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            make_txoutput()

    def test_validate_txoutput(self):
        validate_txoutput({'value': VALUE, 'locking_script': LOCKING_SCRIPT})

        with self.assertRaises(AssertionError, msg='should be raised because `txoutput` has an extra unnecessary attribute'):
            validate_txoutput({'value': VALUE, 'locking_script': LOCKING_SCRIPT, 'unnecessary_attribute': 42})
        with self.assertRaises(AssertionError, msg='should be raised because `txoutput.value` is invalid'):
            validate_txoutput({'value': 42.0, 'locking_script': LOCKING_SCRIPT})
        with self.assertRaises(AssertionError, msg='should be raised because `txoutput.locking_script` is invalid'):
            validate_txoutput({'value': VALUE, 'locking_script': 'invlalid-locking-script'})
        with self.assertRaises(AssertionError, msg='should be raised because `txoutput.value` is missing'):
            validate_txoutput({'locking_script': LOCKING_SCRIPT})
        with self.assertRaises(AssertionError, msg='should be raised because `txoutput.locking_script` is missing'):
            validate_txoutput({'value': VALUE})
        with self.assertRaises(AssertionError, msg='should be raised because `txoutput` argument is empty dict'):
            validate_txoutput({})
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_txoutput()
        
    def test_serialize_txoutput(self):
        actual = serialize_txoutput({'value': VALUE, 'locking_script': LOCKING_SCRIPT})
        expected = serialize_uint64(VALUE) + serialize_varint(len(LOCKING_SCRIPT)) + \
            serialize_script(LOCKING_SCRIPT)
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because txoutput is invalid'):
            serialize_txoutput({})
    
    def test_deserialize_txoutput(self):
        #TODO - requires script deserialization
        pass

    
    def test_txoutput_to_human_readable(self):
        actual = txoutput_to_human_readable(make_txoutput(VALUE, LOCKING_SCRIPT))
        expected = {
            'value': VALUE,
            'locking_script': script_to_human_readable(LOCKING_SCRIPT)
        }

        assert actual == expected


    def test_txoutput_copy(self):
        original = make_txoutput(VALUE, LOCKING_SCRIPT)
        copy = txoutput_copy(original)

        assert type(copy) is type(original)
        assert sorted(copy.keys()) == sorted(original.keys())
        assert id(copy) != id(original)

        assert copy["locking_script"] == original["locking_script"]
        assert copy["value"] == original["value"]
