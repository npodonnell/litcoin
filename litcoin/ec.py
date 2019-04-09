#!/usr/bin/env python3

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives.asymmetric.ec import SECP256K1
from cryptography.hazmat.primitives.asymmetric.ec import ECDSA
from cryptography.hazmat.primitives.asymmetric.ec import derive_private_key
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.exceptions import InvalidSignature
from litcoin.hashing import single_sha
from litcoin.binhex import b

PRIVKEY_SIZE_BYTES = 32
UNCOMPRESSED_PUBKEY_SIZE_BYTES = 65
COMPRESSED_PUBKEY_SIZE_BYTES = 33
UNCOMPRESSED_PUBKEY_DER_PREFIX = b('3056301006072a8648ce3d020106052b8104000a034200')
COMPRESSED_PUBKEY_DER_PREFIX = b('3036301006072a8648ce3d020106052b8104000a032200')
SIGNATURE_ALGORITHM = ECDSA(Prehashed(SHA256()))


def _internal_key_from_bytes(privkey):
    """
    Gets an internal-form private key object for performing EC
    operations such as signing and verification
    """
    privkey_int = int.from_bytes(privkey, signed=False, byteorder='big')
    return derive_private_key(privkey_int, SECP256K1(), default_backend())


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
    assert type(compress) == bool, '`compress` should be of type bool'
    key = _internal_key_from_bytes(privkey)
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
    assert type(message) is bytes, "`message` should be of type `bytes`"
    validate_privkey(privkey)
    key = _internal_key_from_bytes(privkey)
    signature = key.sign(message, SIGNATURE_ALGORITHM)
    return signature


def verify_signature(signature, message, pubkey):
    assert type(signature) is bytes, "`signature` should be of type `bytes`"
    assert type(message) is bytes, "`message` should be of type `bytes`"
    validate_pubkey(pubkey)

    if len(pubkey) == UNCOMPRESSED_PUBKEY_SIZE_BYTES:
        der_pubkey = UNCOMPRESSED_PUBKEY_DER_PREFIX + pubkey
    else:
        der_pubkey = COMPRESSED_PUBKEY_DER_PREFIX + pubkey

    key = load_der_public_key(der_pubkey, default_backend())

    try:
        return key.verify(signature, message, SIGNATURE_ALGORITHM)
    except InvalidSignature:
        return False