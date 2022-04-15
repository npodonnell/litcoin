from litcoin.ec import make_privkey
import unittest


class TestEc(unittest.TestCase):
    def test_make_privkey(self):
        rnd_privkey_1 = make_privkey()
        rnd_privkey_2 = make_privkey()
        assert type(rnd_privkey_1) is bytes
        assert type(rnd_privkey_2) is bytes
        assert len(rnd_privkey_1) == 32
        assert len(rnd_privkey_2) == 32
