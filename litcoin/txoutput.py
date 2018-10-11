#!/usr/bin/env python3

from litcoin.uint64 import validate_uint64, serialize_uint64
from litcoin.varint import serialize_varint
from litcoin.script.validation import validate_script
from litcoin.script.serialization import serialize_script


def make_txoutput(value, locking_script):
    validate_uint64(value)
    validate_script(locking_script)
    
    return {
        'value': value,
        'locking_script': locking_script
    }


def validate_txoutput(txoutput):
    assert type(txoutput) == dict, 'type of txoutput should be dict'
    assert set(txoutput.keys()) == {'value', 'locking_script'}, 'txoutput should have only `value` and `locking_script` keys'
    validate_uint64(txoutput['value'])
    validate_script(txoutput['locking_script'])


def serialize_txoutput(txoutput):
    validate_txoutput(txoutput)
    return serialize_uint64(txoutput['value']) + 
        serialize_varint(len(txoutput['locking_script'])) +
        serialize_script(txoutput['locking_script'])


def deserialize_txoutput(data, i=0):
    pass
