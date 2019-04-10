#!/usr/bin/env python3


def ensure_enough_data(data, pos, min_size):
    """
    Ensure there's enough bytes in `data` starting at position `pos` to
    read in an item of at least `min_size` bytes.
    """
    assert type(data) == bytes
    assert type(pos) == int
    assert type(min_size) == int
    assert 0 <= pos
    assert pos + min_size <= len(data)
