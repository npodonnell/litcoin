#!/usr/bin/env python3

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives.asymmetric.ec import SECP256K1
from cryptography.hazmat.primitives.asymmetric.ec import derive_private_key
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from litcoin.hashing import single_sha
from litcoin.binhex import b, x

PRIVKEY_SIZE_BYTES = 32
UNCOMPRESSED_PUBKEY_SIZE_BYTES = 65
COMPRESSED_PUBKEY_SIZE_BYTES = 33

def validate_privkey(privkey):
    assert type(privkey) == bytes, '`privkey` should be of type `bytes`'
    assert len(privkey) == PRIVKEY_SIZE_BYTES, '`privkey` should be of length {0}'.format(PRIVKEY_SIZE_BYTES)


def validate_pubkey(pubkey):
    assert type(pubkey) == bytes, '`pubkey` should be of type bytes'
    assert len(pubkey) == UNCOMPRESSED_PUBKEY_SIZE_BYTES or len(pubkey) == COMPRESSED_PUBKEY_SIZE_BYTES, \
        '`pubkey` should be of length {0} or {1} bytes' \
        .format(UNCOMPRESSED_PUBKEY_SIZE_BYTES, COMPRESSED_PUBKEY_SIZE_BYTES)

    if pubkey[0] == 0x04:
        assert len(pubkey) == UNCOMPRESSED_PUBKEY_SIZE_BYTES, \
            'Uncompressed `pubkey` should be of length {0}'.format(UNCOMPRESSED_PUBKEY_SIZE_BYTES)
    elif pubkey[0] == 0x02 or pubkey[0] == 0x03:
        assert len(pubkey) == COMPRESSED_PUBKEY_SIZE_BYTES, \
            'Compressed `pubkey` should be of length {0}'.format(COMPRESSED_PUBKEY_SIZE_BYTES)
    else:
        assert False, '`pubkey` should begin with 0x02, 0x03 or 0x04'

def make_privkey(passphrase=None):
    assert passphrase is None or type(passphrase) == str, 'Passphrase should be None or a string'

    if passphrase is not None:
        return single_sha(passphrase.encode('utf-8'))
    return os.urandom(PRIVKEY_SIZE_BYTES)


def derive_pubkey(privkey, compress=True):
    validate_privkey(privkey)
    assert type(compress) == bool, 'Compress should be of type bool'

    privkey_int = int.from_bytes(privkey, signed=False, byteorder='big')
    key = derive_private_key(privkey_int, SECP256K1(), default_backend())
    public_key = key.public_key()
    point = public_key.public_numbers()

    x_bytes = point.x.to_bytes(PRIVKEY_SIZE_BYTES, byteorder='big')

    if compress:
        # return a compressed pubkey
        prefix = b'\02' if point.y % 2 == 0 else b'\03'
        return prefix + x_bytes
    else:
        # return an uncompressed pubkey
        y_bytes = point.y.to_bytes(PRIVKEY_SIZE_BYTES, byteorder='big')
        return b'\04' + x_bytes + y_bytes


def sign_message(message, privkey):
    #TODO
    pass


def verify_signature(signature, message, pubkey):
    #TODO
    pass
