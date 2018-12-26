#!/usr/bin/env python3

from litcoin.uint64 import UINT64_SIZE_IN_BYTES, validate_uint64, serialize_uint64, deserialize_uint64
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES, serialize_varint
from litcoin.script.validator import validate_script
from litcoin.script.serialization import serialize_script
from litcoin.serialization import validate_data

TXOUTPUT_SIZE_RANGE_IN_BYTES = ( \
    UINT64_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0] \
)


def make_txoutput(value, locking_script):
    validate_uint64(value)
    validate_script(locking_script)
    
    return {
        'value': value,
        'locking_script': locking_script
    }


def validate_txoutput(txoutput):
    assert type(txoutput) == dict, 'type of txoutput should be dict'
    assert set(txoutput.keys()) == {'value', 'locking_script'}, \
        'txoutput should have only `value` and `locking_script` keys'
    
    validate_uint64(txoutput['value'])
    validate_script(txoutput['locking_script'])


def serialize_txoutput(txoutput):
    validate_txoutput(txoutput)
    return serialize_uint64(txoutput['value']) + \
        serialize_varint(len(txoutput['locking_script'])) + \
        serialize_script(txoutput['locking_script'])


def deserialize_txoutput(data, i=0):
    validate_data(data, i, TXOUTPUT_SIZE_RANGE_IN_BYTES[0])

    # deserialize value
    value = deserialize_uint64(data, i)
    i += UINT64_SIZE_IN_BYTES

    # deserialize locking script
    (locking_script_length, locking_script_length_length) = deserialize_varint(data, i)
    i += locking_script_length_length
    assert i + locking_script_length <= len(data)
    locking_script = data[i : i + locking_script_length]

    return make_txoutput(value, locking_script)