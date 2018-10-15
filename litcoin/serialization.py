#!/usr/bin/env python3


def validate_data(data, i, min_size):
    assert type(data) == bytes
    assert type(i) == int
    assert type(min_size) == int
    assert 0 <= i
    assert i + min_size <= len(data)
