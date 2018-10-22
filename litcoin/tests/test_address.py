#!/usr/bin/env python3

from litcoin.address import make_p2pkh_address, make_p2sh_address
import unittest


class TestAddress(unittest.TestCase):
    def test_make_p2pkh_address(self):
        actual = make_p2pkh_address(
            bytes.fromhex('02c6f60517274e72e8b870760c944fcc03f008b99d122486ffe9cbcb0d1101a307'), 
            network='bitcoin'
        )
        expected = '17asc93Zb1zbcgmtqPJYgu6fb7FcAXcrNp'
        assert actual == expected
        
        actual = make_p2pkh_address(
            bytes.fromhex('03005d7595ac49a190a0462b52d79f74aaa401543b59018dabc876900c2c20e825'), 
            network='bitcoin'
        )
        expected = '1LmcRYtKM7NGudXpWjueSbZ6TijvU8u7Qe'
        assert actual == expected
    
    def test_make_p2sh_address(self):
        pass
