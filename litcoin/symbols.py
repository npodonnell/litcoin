#!/usr/bin/env python3

# Address types
ADDRESS_TYPE_P2PKH = "ADDRESS_TYPE_P2PKH"
ADDRESS_TYPE_P2SH = "ADDRESS_TYPE_P2SH"


# Sighash types
# See script/interpreter.h
SIGHASH_ALL = 1
SIGHASH_NONE = 2
SIGHASH_SINGLE = 3
SIGHASH_ANYONECANPAY = 0x80


# Sigversions
# See script/interpreter.h
SIGVERSION_BASE = 0
SIGVERSION_WITNESS_V0 = 1
