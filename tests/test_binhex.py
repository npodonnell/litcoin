from litcoin.binhex import b, x
import unittest


class TestBinHex(unittest.TestCase):
    def test_b(self):
        assert b('') == b''
        assert b('00') == b'\x00'
        assert b('01') == b'\x01'
        assert b('fe') == b'\xfe'
        assert b('ff') == b'\xff'
        assert b('0000') == b'\x00\x00'
        assert b('0001') == b'\x00\x01'
        assert b('0100') == b'\x01\x00'
        assert b('ffff') == b'\xff\xff'
        assert b('fffe') == b'\xff\xfe'
        assert b('feff') == b'\xfe\xff'
        assert b('000000') == b'\x00\x00\x00'
        assert b('000001') == b'\x00\x00\x01'
        assert b('010000') == b'\x01\x00\x00'
        assert b('ffffff') == b'\xff\xff\xff'
        assert b('fffffe') == b'\xff\xff\xfe'
        assert b('feffff') == b'\xfe\xff\xff'
        assert b('42' * 1000) == b'\x42' * 1000
        assert b('cC') == b'\xcc'

        with self.assertRaises(TypeError):
            b()
        with self.assertRaises(AssertionError):
            b(['wrong', 'type'])
    
    def test_x(self):
        assert x(b'') == ''
        assert x(b'\x00') == '00'
        assert x(b'\x01') == '01'
        assert x(b'\xfe') == 'fe'
        assert x(b'\xff') == 'ff'
        assert x(b'\x00\x00') == '0000'
        assert x(b'\x00\x01') == '0001'
        assert x(b'\x01\x00') == '0100'
        assert x(b'\xff\xff') == 'ffff'
        assert x(b'\xff\xfe') == 'fffe'
        assert x(b'\xfe\xff') == 'feff'
        assert x(b'\x00\x00\x00') == '000000'
        assert x(b'\x00\x00\x01') == '000001'
        assert x(b'\x01\x00\x00') == '010000'
        assert x(b'\xff\xff\xff') == 'ffffff'
        assert x(b'\xff\xff\xfe') == 'fffffe'
        assert x(b'\xfe\xff\xff') == 'feffff'
        assert x(b'\x42' * 1000) == '42' * 1000
        assert x(b'\xcC') == 'cc'

        with self.assertRaises(TypeError):
            x()
        with self.assertRaises(AssertionError):
            x(['wrong', 'type'])
