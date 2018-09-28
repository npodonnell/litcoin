#!/usr/bin/env python3

import os
from litcoin.hashing import single_sha

KEY_SIZE_BYTES = 32

def make_privkey(**kwargs):
    if 'passphrase' in kwargs:
        return single_sha(kwargs['passphrase'].encode('utf-8'))
    return os.urandom(KEY_SIZE_BYTES)

def derive_pubkey(privkey):
    pass
