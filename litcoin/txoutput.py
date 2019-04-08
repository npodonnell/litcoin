#!/usr/bin/env python3

from litcoin.int64 import INT64_SIZE_IN_BYTES, validate_int64, serialize_int64, deserialize_int64
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES
from litcoin.script.validator import validate_script
from litcoin.script.humanreadable import script_to_human_readable
from litcoin.script.serialization import serialize_script, deserialize_script
from litcoin.script.copy import script_copy
from litcoin.serialization import validate_data

TXOUTPUT_SIZE_RANGE_IN_BYTES = ( \
    INT64_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0], \
)


def make_txoutput(value, locking_script):
    validate_int64(value)
    validate_script(locking_script)
    
    return {
        'value': value,
        'locking_script': locking_script
    }


def validate_txoutput(txoutput):
    assert type(txoutput) == dict, 'type of txoutput should be dict'
    assert set(txoutput.keys()) == {'value', 'locking_script'}, \
        'txoutput should have only `value` and `locking_script` keys'
    
    validate_int64(txoutput['value'])
    validate_script(txoutput['locking_script'])


def serialize_txoutput(txoutput):
    validate_txoutput(txoutput)
    return serialize_int64(txoutput['value']) + serialize_script(txoutput['locking_script'])


def deserialize_txoutput(data, i=0):
    validate_data(data, i, TXOUTPUT_SIZE_RANGE_IN_BYTES[0])

    # deserialize value
    value = deserialize_int64(data, i)
    i += INT64_SIZE_IN_BYTES

    # deserialize locking script
    (locking_script, _) = deserialize_script(data, i)

    return make_txoutput(value, locking_script)


def txoutput_to_human_readable(txoutput):
    return {
        'value': txoutput['value'],
        'locking_script': script_to_human_readable(txoutput['locking_script'])
    }


def txoutput_copy(txoutput):
    return {
        "value": txoutput["value"],
        "locking_script": script_copy(txoutput["locking_script"])
    }
