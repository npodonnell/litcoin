#!/usr/bin/env python3


from .binhex import b, x
from .serialization import validate_data

TXID_SIZE_IN_BYTES = 32


def make_txid(input):
    """
    Make a txid from a bytes, string or int
    """
    if type(input) is bytes:
        txid = input
    elif type(input) is str:
        try:
            txid = b(input)
        except:
            raise ValueError("Unparsable txid: {0}".format(input))
    elif type(input) is int:
        try:
            txid = int.to_bytes(input, TXID_SIZE_IN_BYTES, byteorder='big', signed=False)
        except:
            raise ValueError("Cannot convert integer {0} to txid".format(input))
    else:
        raise TypeError("Cannot make txid from type: {0}".format(type(input)))
    
    if len(txid) != TXID_SIZE_IN_BYTES:
        raise ValueError("txid should be {0} bytes long, not {1}".format(TXID_SIZE_IN_BYTES, len(txid)))
    
    validate_txid(txid)
    return txid


def validate_txid(txid):
    assert type(txid) is bytes, "`txid` should be of type `bytes`"
    assert len(txid) == TXID_SIZE_IN_BYTES, "txid should be {0} bytes long, not {1}".format(TXID_SIZE_IN_BYTES, len(txid))


def serialize_txid(txid):
    validate_txid(txid)
    return txid


def deserialize_txid(data, i=0):
    validate_data(data, i, TXID_SIZE_IN_BYTES)
    return data[i : i + TXID_SIZE_IN_BYTES]


def txid_to_human_readable(txid):
    return x(txid)
