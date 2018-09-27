#!/usr/bin/env python3

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
        else:
            break

    return enc

def base58_decode(data):
    dec = bytes()
    n = 0
    p = 0

    for digit in reversed(data):
        n += BASE58_ALPHABET.index(digit) * (58 ** p)
        p += 1

    while n != 0:
        r = n % 256
        n = n // 256
        dec = bytes([r]) + dec

    for c in data:
        if c == '1':
            dec = bytes([0x00]) + dec
        else:
            break

    return dec

