#!/usr/bin/env python3

def validate_script(script):
    """
    Validate compiled script
    """
    assert type(script) == bytes
    # TODO - more validation