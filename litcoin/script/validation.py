#!/usr/bin/env python3


def validate_script(script):
    assert type(script) == list, 'Argument `script` should be of type `list`'

    for item in script:
        assert type(item) == int or type(item) == bytes, 'All items in `script` should be of type `int` or `bytes`'

    # TODO - add more validation logic here
