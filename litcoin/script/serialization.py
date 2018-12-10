#!/usr/bin/env python3

from litcoin.script.validation import validate_script
from litcoin.script.constants import MAX_SCRIPT_SIZE


def serialize_script(script):
    validate_script(script)
    bin_script = b''

    #TODO

    assert len(bin_script) <= MAX_SCRIPT_SIZE
    return bin_script
