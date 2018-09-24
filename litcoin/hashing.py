#!/usr/bin/env python3

import hashlib

def double_sha(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def hash160(data):
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(data).digest())
    return h.digest()
