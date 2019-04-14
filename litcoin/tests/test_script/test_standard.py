#!/usr/bin/env python3

import unittest
from litcoin.script.standard import make_p2pkh_locking_script, make_p2sh_locking_script
from litcoin.script.operations import OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_EQUAL, OP_CHECKSIG
from litcoin.binhex import b

class TestScriptStandard(unittest.TestCase):
    def test_make_p2pkh_locking_script(self):
        pubkey_hash = b("a7ead10f72ddee539382f2cfff6e523a8eab3608")
        actual = make_p2pkh_locking_script(pubkey_hash)
        expected = [OP_DUP, OP_HASH160, pubkey_hash, OP_EQUALVERIFY, OP_CHECKSIG]
        assert actual == expected

    def test_make_p2sh_locking_script(self):
        script_hash = b("c9910198e241c31634785e88b869c4db6414d962")
        actual = make_p2sh_locking_script(script_hash)
        expected = [OP_HASH160, script_hash, OP_EQUAL]
        assert actual == expected

