from typing import Optional
from .secp256k1 import SECP256K1_ORDER, secp256k1_random_scalar, secp256k1_multiply, secp256k1_compute_ys
from .secp256k1_ecdsa import secp256k1_ecdsa_sign, secp256k1_ecdsa_verify
from .uint256 import uint256_from_bytes, uint256_to_bytes
from .hashing import single_sha
from .binhex import b, x
import os
from itertools import count


PRIVKEY_SIZE_BYTES = 32
UNCOMPRESSED_PUBKEY_SIZE_BYTES = 65
COMPRESSED_PUBKEY_SIZE_BYTES = 33

def _uint_size_in_bytes(x):
    """
    Computes the number of bytes needed to hold an unsigned integer of
    arbitrary length. 
    """
    assert type(x) is int, "`x` should be of type `int`"
    assert 0 <= x, "`x` should be >= 0"
    size = 0
    while True:
        x >>= 8
        size += 1
        if x == 0:
            return size  


def validate_privkey(privkey: bytes):
    assert type(privkey) is bytes, "privkey should be of type bytes"
    assert len(privkey) == PRIVKEY_SIZE_BYTES, f"privkey should be of length {PRIVKEY_SIZE_BYTES}"


def validate_pubkey(pubkey: bytes):
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


def make_privkey(passphrase: Optional[str] = None) -> bytes:
    if passphrase is not None:
        if type(passphrase) is not str:
            raise TypeError("passphrase should be a string")
        return single_sha(passphrase.encode("utf-8"))
    return uint256_to_bytes(secp256k1_random_scalar())


def derive_pubkey(privkey: bytes, compress: bool = True) -> bytes:
    validate_privkey(privkey)
    assert type(compress) is bool, '`compress` should be of type bool'
    return serialize_pubkey(secp256k1_multiply(uint256_from_bytes(privkey)), compress)


def parse_pubkey(pubkey: bytes) -> tuple[int, int]:
    validate_pubkey(pubkey)
    x: int = uint256_from_bytes(pubkey[1:33])
    if pubkey[0] == 4:
        y: int = uint256_from_bytes(pubkey[33:65])
    else:
        y: int = secp256k1_compute_ys(x)[pubkey[0] & 1]
    return x, y


def serialize_pubkey(pubkey: tuple[int, int], compress: bool = True) -> bytes:
    assert type(pubkey) is tuple
    assert type(compress) is bool, '`compress` should be of type bool'
    x, y = pubkey
    if compress:
        return (b"\x02" if (y % 2) == 0 else b"\x03") + uint256_to_bytes(x)
    else:
        return b"\x04" + uint256_to_bytes(x) + uint256_to_bytes(y)


def parse_der_ecdsa_signature(signature: bytes) -> tuple[int, int]:
    assert type(signature) is bytes
    assert len(signature) >= 8, "signature should be at least 8 bytes long"
    assert signature[0] == 0x30, f"first octet expected to be 0x30, but is 0x{signature[0]:02x}"
    assert signature[1] == len(signature) - 2, "incorrect total size"
    assert signature[2] == 0x02, f"third octet expected to be 0x02, but is 0x{signature[2]:02x}"
    r_len: int = signature[3]
    r: int = int.from_bytes(signature[4 : 4 + r_len], byteorder="big", signed=False)
    assert signature[4 + r_len] == 0x02, f"octet {4 + r_len} expected to be 0x02, but is 0x{signature[4 + r_len]:02x}"
    s_len: int = signature[4 + r_len + 1]
    s: int = int.from_bytes(signature[4 + r_len + 1 : 4 + r_len + 1 + s_len], byteorder="big", signed=False)
    return r, s


def sign_message(msg_hash: bytes, privkey: bytes) -> bytes:
    assert type(message) is bytes, "`message` should be of type `bytes`"
    validate_privkey(privkey)
    privkey_i: int = uint256_from_bytes(privkey)
    
    # In DER serialization, all values are interpreted as big-endian, signed integers. The highest bit in the integer indicates
    # its signed-ness; 0 is positive, 1 is negative. When the value is interpreted as a negative integer, it must be converted
    # to a positive value by prepending a 0x00 byte so that the highest bit is 0. We can avoid this prepending by ensuring that
    # our highest bit is always 0, and thus we must check that the first byte is less than 0x80.
    # See src/key.cpp - SigHasLowR function
    for counter in count(0):
        r, s = secp256k1_ecdsa_sign(privkey_i, msg_hash, counter)
        r_len: int = _uint_size_in_bytes(r)
        r_bytes: bytes = r.to_bytes(r_len, byteorder="big", signed=False)
        if r_bytes[0] < 0x80:
            break
    s_len: int = _uint_size_in_bytes(s)
    s_bytes: bytes = s.to_bytes(s_len, byteorder="big", signed=False)
    total_size: int = 4 + r_len + s_len
    total_size_bytes = total_size.to_bytes(1, byteorder="big", signed=False)
    r_len_bytes: int = r_len.to_bytes(1, byteorder="big", signed=False)
    s_len_bytes: int = s_len.to_bytes(1, byteorder="big", signed=False)

    # DER serialize.
    return b"\x30" + total_size_bytes + b"\x02" + r_len_bytes + r_bytes + b"\x02" + s_len_bytes + s_bytes


def valid_signature(signature: bytes, message: bytes, pubkey: bytes) -> bool:
    assert type(signature) is bytes, "`signature` should be of type `bytes`"
    assert type(message) is bytes, "`message` should be of type `bytes`"
    assert len(message) == 32, "`message` should be 32 bytes long"
    validate_pubkey(pubkey)
    return secp256k1_ecdsa_verify(parse_der_ecdsa_signature(signature), parse_pubkey(pubkey), message)
