#!/usr/bin/env python3

from litcoin.hashing import hash160

def make_address(pubkey):
    pubkey_hash = hash160(pubkey)