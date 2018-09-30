#!/usr/bin/env python3

# Maximum number of bytes pushable to the stack
MAX_SCRIPT_ELEMENT_SIZE = 520

# Maximum number of non-push operations per script
MAX_OPS_PER_SCRIPT = 201

# Maximum number of public keys per multisig
MAX_PUBKEYS_PER_MULTISIG = 20

# Maximum script length in bytes
MAX_SCRIPT_SIZE = 10000

# Maximum number of values on script interpreter stack
MAX_STACK_SIZE = 1000

# Threshold for nLockTime: below this value it is interpreted as block number,
# otherwise as UNIX timestamp.
LOCKTIME_THRESHOLD = 500000000 # Tue Nov  5 00:53:20 1985 UTC
