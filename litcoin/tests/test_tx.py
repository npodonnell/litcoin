#!/usr/bin/env python3

import unittest
from litcoin.tx import CURRENT_TX_VERSION, make_tx

class TestTx(unittest.TestCase):
    def test_make_tx(self):
        actual = make_tx()
        expected = {
            'version': CURRENT_TX_VERSION,
            'lock_time': 0,
            'inputs': [],
            'outputs': []
        }
        assert actual == expected