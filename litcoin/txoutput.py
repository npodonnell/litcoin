#!/usr/bin/env python3

from .int64 import INT64_SIZE_IN_BYTES, validate_int64, serialize_int64, deserialize_int64
from .varint import VARINT_SIZE_RANGE_IN_BYTES
from .script.validator import validate_script
from .script.humanreadable import script_to_human_readable
from .script.serialization import serialize_script, deserialize_script
from .script.compiler import compile_script
from .script.standard import make_p2pkh_locking_script, make_p2sh_locking_script
from .script.copy import script_copy
from .serialization import ensure_enough_data
from .address import address_decode
from .symbols import ADDRESS_TYPE_P2PKH, ADDRESS_TYPE_P2SH

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


def make_txoutput_to_address(value, address):
    """
    Detects the address type (P2PKH, P2SH, etc) and generates a
    txoutput with the correct type of locking script so that
    currency gets paid to this address
    """
    validate_int64(value)
    (_, address_type, address_hash) = address_decode(address)

    if address_type == ADDRESS_TYPE_P2PKH:
        locking_script = make_p2pkh_locking_script(address_hash)
    elif address_type == ADDRESS_TYPE_P2SH:
        locking_script = make_p2sh_locking_script(address_hash)
    else:
        raise ValueError("Unknown address type: {0}".format(address_type))

    return make_txoutput(value, compile_script(locking_script))


def validate_txoutput(txoutput):
    assert type(txoutput) == dict, 'type of txoutput should be dict'
    assert set(txoutput.keys()) == {'value', 'locking_script'}, \
        'txoutput should have only `value` and `locking_script` keys'
    validate_int64(txoutput['value'])
    validate_script(txoutput['locking_script'])


def serialize_txoutput(txoutput):
    validate_txoutput(txoutput)
    return serialize_int64(txoutput['value']) + serialize_script(txoutput['locking_script'])


def deserialize_txoutput(data, pos=0):
    ensure_enough_data(data, pos, TXOUTPUT_SIZE_RANGE_IN_BYTES[0])
    (value, pos) = deserialize_int64(data, pos)
    (locking_script, pos) = deserialize_script(data, pos)
    return (make_txoutput(value, locking_script), pos)


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
