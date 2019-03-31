#!/usr/bin/env python3

from litcoin.outpoint import OUTPOINT_SIZE_IN_BYTES, make_outpoint, serialize_outpoint
from litcoin.script.serialization import serialize_script
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, serialize_uint32
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES, serialize_varint
from litcoin.txinput import TXINPUT_SIZE_RANGE_IN_BYTES, make_txinput, validate_txinput, serialize_txinput, \
    deserialize_txinput, txinput_to_human_readable, txinput_copy
from litcoin.outpoint import outpoint_to_human_readable
from litcoin.script.humanreadable import script_to_human_readable
from litcoin.binhex import b, x
import unittest

OUTPOINT = make_outpoint(b('8000000000000000000000000000000000000000000000000000000000000001'), 42)
UNLOCKING_SCRIPT = b('')
SEQUENCE_NO = 42


class TestTxinput(unittest.TestCase):
    def test_TXINPUT_SIZE_RANGE_IN_BYTES(self):
        assert TXINPUT_SIZE_RANGE_IN_BYTES == (OUTPOINT_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0] + UINT32_SIZE_IN_BYTES,)

    def test_make_txinput(self):
        actual = make_txinput(OUTPOINT, UNLOCKING_SCRIPT, SEQUENCE_NO)
        expected = {'outpoint': OUTPOINT, 'unlocking_script': UNLOCKING_SCRIPT, 'sequence_no': SEQUENCE_NO}
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because `outpoint` argument is the wrong type'):
            make_txinput('wrong type', UNLOCKING_SCRIPT, SEQUENCE_NO)
        with self.assertRaises(AssertionError, msg='should be raised because `unlocking_script` argument is the wrong type'):
            make_txinput(OUTPOINT, 'wrong type', SEQUENCE_NO)
        with self.assertRaises(AssertionError, msg='should be raised because `sequence_no` argument is the wrong type'):
            make_txinput(OUTPOINT, UNLOCKING_SCRIPT, 42.0)
        with self.assertRaises(TypeError, msg='should be raised because `sequence_no` argument is missing'):
            make_txinput(OUTPOINT, UNLOCKING_SCRIPT)
        with self.assertRaises(TypeError, msg='should be raised because `sequence_no` and `unlocking_script` arguments are missing'):
            make_txinput(OUTPOINT)
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            make_txinput()
    
    def test_validate_txinput(self):
        validate_txinput({'outpoint': OUTPOINT, 'unlocking_script': UNLOCKING_SCRIPT, 'sequence_no': SEQUENCE_NO})

        with self.assertRaises(AssertionError, msg='should be raised because `txinput` has an extra unnecessary attribute'):
            validate_txinput({'outpoint': OUTPOINT, 'unlocking_script': UNLOCKING_SCRIPT, 'sequence_no': SEQUENCE_NO, 'unnecessary_attribute': 42})
        with self.assertRaises(AssertionError, msg='should be raised because `txinput.outpoint` is invalid'):
            validate_txinput({'outpoint': {'invalid': 'outpoint'}, 'unlocking_script': UNLOCKING_SCRIPT, 'sequence_no': SEQUENCE_NO})
        with self.assertRaises(AssertionError, msg='should be raised because `txinput.unlocking_script` is invalid'):
            validate_txinput({'outpoint': OUTPOINT, 'unlocking_script': 'invalid-script', 'sequence_no': SEQUENCE_NO})
        with self.assertRaises(AssertionError, msg='should be raised because `txinput.sequence_no` is invalid'):
            validate_txinput({'outpoint': OUTPOINT, 'unlocking_script': UNLOCKING_SCRIPT, 'sequence_no': -1})
        with self.assertRaises(AssertionError, msg='should be raised because `txinput.outpoint` is missing'):
            validate_txinput({'unlocking_script': UNLOCKING_SCRIPT, 'sequence_no': SEQUENCE_NO})
        with self.assertRaises(AssertionError, msg='should be raised because `txinput.unlocking_script` is missing'):
            validate_txinput({'outpoint': OUTPOINT, 'sequence_no': SEQUENCE_NO})
        with self.assertRaises(AssertionError, msg='should be raised because `txinput.sequence_no` is missing'):
            validate_txinput({'outpoint': OUTPOINT, 'unlocking_script': UNLOCKING_SCRIPT})
        with self.assertRaises(AssertionError, msg='should be raised because `txinput` argument is empty dict'):
            validate_txinput({})
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_txinput()
    
    def test_serialize_txinput(self):
        actual = serialize_txinput({'outpoint': OUTPOINT, 'unlocking_script': UNLOCKING_SCRIPT, 'sequence_no': SEQUENCE_NO})
        expected = serialize_outpoint(OUTPOINT) + serialize_varint(len(UNLOCKING_SCRIPT)) + \
            serialize_script(UNLOCKING_SCRIPT) + serialize_uint32(SEQUENCE_NO)
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because txinput is invalid'):
            serialize_txinput({})
    
    def test_deserialize_txinput(self):
        #TODO - requires script deserialization
        pass

    def test_txinput_to_human_readable(self):
        actual = txinput_to_human_readable(make_txinput(OUTPOINT, UNLOCKING_SCRIPT, SEQUENCE_NO))
        expected = {
            'outpoint': outpoint_to_human_readable(OUTPOINT),
            'unlocking_script': script_to_human_readable(UNLOCKING_SCRIPT),
            'sequence_no': SEQUENCE_NO
        }

        assert actual == expected


    def test_txinput_copy(self):
        original = make_txinput(OUTPOINT, UNLOCKING_SCRIPT, SEQUENCE_NO)
        copy = txinput_copy(original)

        assert type(copy) is type(original)
        assert sorted(copy.keys()) == sorted(original.keys())
        assert id(copy) != id(original)

        assert copy["unlocking_script"] == original["unlocking_script"]
        assert copy["sequence_no"] == original["sequence_no"]

        assert type(copy["outpoint"]) is type(original["outpoint"])
        assert sorted(copy["outpoint"].keys()) == sorted(original["outpoint"].keys())
        assert id(copy["outpoint"]) != id(original["outpoint"])

        assert copy["outpoint"]["txid"] == original["outpoint"]["txid"]
        assert copy["outpoint"]["output_index"] == original["outpoint"]["output_index"]
