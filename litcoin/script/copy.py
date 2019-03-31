#!/usr/bin/env python3

from .validator import validate_script

def script_copy(script):
    """
    Performs a deep-copy of a script
    """
    validate_script(script)

    # bytes objects are immutable so just return `script`
    # this is python-specific and may not work in other
    # languages!
    return script
