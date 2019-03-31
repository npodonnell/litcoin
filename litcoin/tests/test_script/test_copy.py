#!/usr/bin/env python3

import unittest
from litcoin.script.compiler import compile_script
from litcoin.script.operations import OP_2, OP_3, OP_5, OP_EQUAL
from litcoin.script.copy import script_copy


class TestScriptCopy(unittest.TestCase):
    def test_script_copy(self):
        script = compile_script([OP_2, OP_3, OP_5, OP_EQUAL])
        actual = script_copy(script)
        expected = script
        assert actual == expected
