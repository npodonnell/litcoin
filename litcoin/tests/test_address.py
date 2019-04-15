#!/usr/bin/env python3

from litcoin.address import ADDRESS_DECODED_EXPECTED_LENGTH_IN_BYTES, ADDRESS_TYPE_P2PKH, \
    ADDRESS_TYPE_P2SH, make_p2pkh_address, make_p2sh_address, address_decode
from litcoin.hashing import hash160
from litcoin.binhex import b
import unittest


class TestAddress(unittest.TestCase):
    def test_ADDRESS_DECODED_EXPECTED_LENGTH_IN_BYTES(self):
        assert ADDRESS_DECODED_EXPECTED_LENGTH_IN_BYTES == 21

    def test_ADDRESS_TYPE_P2PKH(self):
        assert ADDRESS_TYPE_P2PKH == "ADDRESS_TYPE_P2PKH"

    def test_ADDRESS_TYPE_P2SH(self):
        assert ADDRESS_TYPE_P2SH == "ADDRESS_TYPE_P2SH"

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
        expected = 'MAyXeq6ZpL71HLbt1DveTDETDztvLUdZvT'
        assert actual == expected

    def test_address_decode(self):
        actual = address_decode("18VkRiDhFu2Z17AvtpU3vL2LbTXDzCvDVo")
        expected = ("bitcoin", ADDRESS_TYPE_P2PKH, hash160(b("02218ad6cdc632e7ae7d04472374311cebbbbf0ab540d2d08c3400bb844c654231")))
        assert actual == expected

        actual = address_decode("LZDjqaThptiYJ3E6G4rwdbaKxBcT1oZJKt")
        expected = ("litecoin", ADDRESS_TYPE_P2PKH, hash160(b("03d18ae1a973b3977cd652b34f5d0f86bda0e0b164d4f19074e73aba11aed6a47c")))
        assert actual == expected

        actual = address_decode("34mPLwgbsDFaUqKyuLwJdZz3uJJUKJ1DYE")
        expected = ("bitcoin", ADDRESS_TYPE_P2SH, hash160(b("0460ae0a00b1752103da79c329cf1a92a6cb172118027fb49ed93352ad40990331442350d809d7fbd1ac")))
        assert actual == expected

        actual = address_decode("MAyXeq6ZpL71HLbt1DveTDETDztvLUdZvT")
        expected = ("litecoin", ADDRESS_TYPE_P2SH, hash160(b("0460ae0a00b1752103da79c329cf1a92a6cb172118027fb49ed93352ad40990331442350d809d7fbd1ac")))
        assert actual == expected