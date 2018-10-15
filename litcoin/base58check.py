#!/usr/bin/env python3

from litcoin.hashing import double_sha

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def base58check_encode(data):
    assert type(data) == bytes

    data = data + double_sha(data)[0:4]
    n = int.from_bytes(data, byteorder='big', signed=False)
    enc = ''

    while n != 0:
        r = n % 58
        n = n // 58
        enc = BASE58_ALPHABET[r] + enc
    
    for b in data:
        if b == 0x00:
            enc = '1' + enc
            continue
        break

    return enc


def base58check_decode(b58str):
    assert type(b58str) == str
    
    n = 0
    p = 0
    dec = bytes()

    for digit in reversed(b58str):
        n += BASE58_ALPHABET.index(digit) * (58 ** p)
        p += 1

    while n != 0:
        r = n % 256
        n = n // 256
        dec = bytes([r]) + dec

    for c in b58str:
        if c == '1':
            dec = bytes([0x00]) + dec
            continue
        break
    
    payload = dec[0:-4]
    bundled_checksum = dec[-4:]
    computed_checksum = double_sha(payload)[0:4]

    if bundled_checksum != computed_checksum:
        raise ValueError('Checksums do not match')
    
    return payload
