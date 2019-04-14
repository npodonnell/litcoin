#!/usr/bin/env python3

import hashlib


SHA_LENGTH_IN_BYTES = 32
HASH160_LENGTH_IN_BYTES = 20

def validate_sha(h):
    """
    Validates that a hash at least looks like a valid SHA image
    """
    assert type(h) is bytes, "`data` should be of type `bytes`"
    assert len(h) == SHA_LENGTH_IN_BYTES, "`data` should be of length {0}".format(SHA_LENGTH_IN_BYTES)


def validate_hash160(h):
    """
    Validates that a hash at least looks like a valid Ripemd160 image
    """
    assert type(h) is bytes, "`data` should be of type `bytes`"
    assert len(h) == HASH160_LENGTH_IN_BYTES, "`data` should be of length {0}".format(HASH160_LENGTH_IN_BYTES)


def single_sha(data):
    return hashlib.sha256(data).digest()


def double_sha(data):
    return single_sha(single_sha(data))


def hash160(data):
    h = hashlib.new('ripemd160')
    h.update(single_sha(data))
    return h.digest()
