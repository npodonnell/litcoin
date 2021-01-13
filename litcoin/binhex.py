#!/usr/bin/env python3

import re


def b(hex_str):
    """
    Convenience function to convert even-length hex string (excluding 0x) to bytes object
    """
    assert type(hex_str) is str
    assert re.match('^([0-9a-fA-F]{2})*$', hex_str) is not None, 'Not a valid string of hex octets'
    return bytes.fromhex(hex_str)


def x(bytes_obj):
    """
    Convenience function to convert bytes object to even-length hex string (excluding 0x)
    """
    assert type(bytes_obj) is bytes
    return bytes_obj.hex()
