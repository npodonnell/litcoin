#!/usr/bin/env python3

from litcoin.address import make_p2pkh_address, make_p2sh_address
from litcoin.binhex import b
import unittest


class TestAddress(unittest.TestCase):
    def test_make_p2pkh_address(self):
        actual = make_p2pkh_address(
            b('02218ad6cdc632e7ae7d04472374311cebbbbf0ab540d2d08c3400bb844c654231'), 
            'bitcoin'
        )
        expected = '18VkRiDhFu2Z17AvtpU3vL2LbTXDzCvDVo'
        assert actual == expected
        
        actual = make_p2pkh_address(
            b('03d18ae1a973b3977cd652b34f5d0f86bda0e0b164d4f19074e73aba11aed6a47c'), 
            'litecoin'
        )
        expected = 'LZDjqaThptiYJ3E6G4rwdbaKxBcT1oZJKt'
        assert actual == expected

    
    def test_make_p2sh_address(self):
        actual = make_p2sh_address(
            b('0460ae0a00b1752103da79c329cf1a92a6cb172118027fb49ed93352ad40990331442350d809d7fbd1ac'), 
            'bitcoin'
        )
        expected = '34mPLwgbsDFaUqKyuLwJdZz3uJJUKJ1DYE'
        assert actual == expected
        
        actual = make_p2sh_address(
            b('0460ae0a00b1752103da79c329cf1a92a6cb172118027fb49ed93352ad40990331442350d809d7fbd1ac'), 
            'litecoin'
        )
        expected = '34mPLwgbsDFaUqKyuLwJdZz3uJJUKJ1DYE'
        assert actual == expected

    