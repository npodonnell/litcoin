#!/usr/bin/env python3

from litcoin.hashing import double_sha
from litcoin.base58 import base58_encode, base58_decode

def base58check_encode(bin_data):
    checksum = double_sha(bin_data)[0:4]
    return base58_encode(bin_data + checksum)

def base58check_decode(b58_data):
    bin_data = base58_decode(b58_data)
    payload = bin_data[0:-4]

    bundled_checksum = bin_data[-4:]
    computed_checksum = double_sha(payload)[0:4]

    if bundled_checksum != computed_checksum:
        raise ValueError('Checksums do not match')
    
    return payload
