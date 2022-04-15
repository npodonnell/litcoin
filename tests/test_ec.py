from litcoin.ec import make_privkey, derive_pubkey
from litcoin.binhex import b, x
import unittest


class TestEc(unittest.TestCase):
    def test_make_privkey(self):
        rnd_privkey_1 = make_privkey()
        rnd_privkey_2 = make_privkey()
        det_privkey_1 = make_privkey("bitcoin")
        det_privkey_2 = make_privkey("bitcoin")
        det_privkey_3 = make_privkey("hello")
        self.assertIs(type(rnd_privkey_1), bytes)
        self.assertIs(type(rnd_privkey_2), bytes)
        self.assertIs(type(det_privkey_1), bytes)
        self.assertIs(type(det_privkey_2), bytes)
        self.assertIs(type(det_privkey_3), bytes)
        self.assertEqual(len(rnd_privkey_1), 32)
        self.assertEqual(len(rnd_privkey_2), 32)
        self.assertEqual(len(det_privkey_1), 32)
        self.assertEqual(len(det_privkey_2), 32)
        self.assertEqual(len(det_privkey_3), 32)
        self.assertNotEqual(rnd_privkey_1, rnd_privkey_2)
        self.assertNotEqual(rnd_privkey_1, det_privkey_1)
        self.assertEqual(det_privkey_1, det_privkey_2)
        self.assertNotEqual(det_privkey_1, det_privkey_3)

        with self.assertRaises(TypeError):
            make_privkey(4)
    
    def test_derive_pubkey(self):
        privkey: bytes = b("8000000000000000000000000000000000000000000000000000000000000000")
        pubkey_c: bytes = derive_pubkey(privkey)
        pubkey_u: bytes = derive_pubkey(privkey, compress=False)
        self.assertEqual(pubkey_c, b("02b23790a42be63e1b251ad6c94fdef07271ec0aada31db6c3e8bd32043f8be384"))
        self.assertEqual(pubkey_u, b("04"
                                     "b23790a42be63e1b251ad6c94fdef07271ec0aada31db6c3e8bd32043f8be384"
                                     "fc6b694919d55edbe8d50f88aa81f94517f004f4149ecb58d10a473deb19880e"))
