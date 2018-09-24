#!/usr/bin/env python3

import binascii

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_encode(data):
    enc = ''

    if len(data) == 0:
        return enc
    
    n = int(data.hex(), 16)
    
    while n != 0:
        r = n % 58
        n = n // 58
        enc = BASE58_ALPHABET[r] + enc
    
    for b in data:
        if b == 0x00:
            enc = '1' + enc

    return enc

def base58_decode(data):
    pass
