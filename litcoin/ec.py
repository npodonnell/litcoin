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
from litcoin.binhex import b, x

PRIVKEY_SIZE_BYTES = 32
UNCOMPRESSED_PUBKEY_SIZE_BYTES = 65
COMPRESSED_PUBKEY_SIZE_BYTES = 33
UNCOMPRESSED_PUBKEY_DER_PREFIX = b('3056301006072a8648ce3d020106052b8104000a034200')
COMPRESSED_PUBKEY_DER_PREFIX = b('3036301006072a8648ce3d020106052b8104000a032200')
SIGNATURE_ALGORITHM = ECDSA(Prehashed(SHA256()))
SECP256K1_CURVE_ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
SECP256K1_CURVE_ORDER_HALVED = SECP256K1_CURVE_ORDER >> 1

def _uint_size_in_bytes(x):
    """
    Compute the number of bytes needed to hold an unsigned integer of
    arbitrary length. Needed for DER re-encoding 
    """
    assert type(x) is int, "`x` should be of type `int`"
    assert 0 <= x, "`x` should be >= 0"
    size = 0
    while True:
        x >>= 8
        size += 1
        if x == 0:
            return size

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
    r_pos = 4

    # In DER serialization, all values are interpreted as big-endian, signed integers. The highest bit in the integer indicates
    # its signed-ness; 0 is positive, 1 is negative. When the value is interpreted as a negative integer, it must be converted
    # to a positive value by prepending a 0x00 byte so that the highest bit is 0. We can avoid this prepending by ensuring that
    # our highest bit is always 0, and thus we must check that the first byte is less than 0x80.
    # See src/key.cpp - SigHasLowR function
    while True:
        signature = key.sign(message, SIGNATURE_ALGORITHM)
        if signature[r_pos] != 0x00:
            break
    
    r_len_pos = 3
    r_len = int.from_bytes(signature[r_len_pos : r_len_pos + 1], byteorder='big', signed=False)
    s_len_pos = 5 + r_len
    s_pos = s_len_pos + 1
    s_len = int.from_bytes(signature[s_len_pos : s_len_pos + 1], byteorder='big', signed=False)
    s = int.from_bytes(signature[s_pos : s_pos + s_len], byteorder='big', signed=False)

    # To help with non-malleability of transactions, We want a low S value.
    # See https://github.com/bitcoin/bips/blob/master/bip-0062.mediawiki#Low_S_values_in_signatures
    if SECP256K1_CURVE_ORDER_HALVED < s:
        s = SECP256K1_CURVE_ORDER - s
        s_len = _uint_size_in_bytes(s)
        total_size = 4 + r_len + s_len
        # Rebuild signature
        total_size_bytes = int.to_bytes(total_size, 1, byteorder='big', signed=False)
        r_len_bytes = signature[r_len_pos : r_len_pos + 1]
        r_bytes = signature[r_pos : r_pos + r_len]
        s_len_bytes = int.to_bytes(s_len, 1, byteorder='big', signed=False)
        s_bytes = int.to_bytes(s, s_len, byteorder='big', signed=False)
        signature = b'\x30' + total_size_bytes + b'\x02' + r_len_bytes + r_bytes + b'\x02' + s_len_bytes + s_bytes
    return signature


def valid_signature(signature, message, pubkey):
    assert type(signature) is bytes, "`signature` should be of type `bytes`"
    assert type(message) is bytes, "`message` should be of type `bytes`"
    validate_pubkey(pubkey)

    if len(pubkey) == UNCOMPRESSED_PUBKEY_SIZE_BYTES:
        der_pubkey = UNCOMPRESSED_PUBKEY_DER_PREFIX + pubkey
    else:
        der_pubkey = COMPRESSED_PUBKEY_DER_PREFIX + pubkey

    key = load_der_public_key(der_pubkey, default_backend())

    try:
        key.verify(signature, message, SIGNATURE_ALGORITHM)
        return True
    except InvalidSignature:
        return False
