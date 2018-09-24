#!/usr/bin/env python3

import binascii

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_encode(data):
    bigint = int('0x0' + binascii.hexlify(data).decode('utf8'), 16)

    # TODO...
    

def base58_decode(data):
    pass
