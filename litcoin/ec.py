#!/usr/bin/env python3

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives.asymmetric.ec import SECP256K1
from cryptography.hazmat.primitives.asymmetric.ec import derive_private_key
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from litcoin.hashing import single_sha

KEY_SIZE_BYTES = 32


def validate_privkey(privkey):
    assert type(privkey) == bytes, 'privkey should be of type bytes'
    assert len(privkey) == KEY_SIZE_BYTES, 'privkey should be of length {0}'.format(KEY_SIZE_BYTES)


def compress_ec_point(x, y):
    x_bytes = x.to_bytes(KEY_SIZE_BYTES, byteorder='big')
    prefix = b'\02' if y % 2 == 0 else b'\03'
    return prefix + x_bytes


def make_privkey(**kwargs):
    if 'passphrase' in kwargs:
        return single_sha(kwargs['passphrase'].encode('utf-8'))
    return os.urandom(KEY_SIZE_BYTES)


def derive_pubkey(privkey):
    privkey_int = int.from_bytes(privkey, signed=False, byteorder='big')
    key = derive_private_key(privkey_int, SECP256K1(), default_backend())
    public_key = key.public_key()
    point = public_key.public_numbers()
    return compress_ec_point(point.x, point.y)


def sign_message(message, privkey):
    #TODO
    pass


def verify_signature(signature, message, pubkey):
    #TODO
    pass
