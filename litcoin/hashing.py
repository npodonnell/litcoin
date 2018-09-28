#!/usr/bin/env python3

import hashlib


def single_sha(data):
    return hashlib.sha256(data).digest()


def double_sha(data):
    return single_sha(single_sha(data))


def hash160(data):
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(data).digest())
    return h.digest()
