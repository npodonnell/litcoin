from litcoin.ec import make_privkey, derive_pubkey, parse_pubkey
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
        pubkey_c_exp: bytes = b("02"
                                "b23790a42be63e1b251ad6c94fdef07271ec0aada31db6c3e8bd32043f8be384")
        pubkey_u_exp: bytes = b("04"
                                "b23790a42be63e1b251ad6c94fdef07271ec0aada31db6c3e8bd32043f8be384"
                                "fc6b694919d55edbe8d50f88aa81f94517f004f4149ecb58d10a473deb19880e")
        self.assertEqual(derive_pubkey(privkey), pubkey_c_exp)
        self.assertEqual(derive_pubkey(privkey, compress=False), pubkey_u_exp)

    def test_parse_pubkey(self):
        pubkey_c: bytes = b("02"
                            "ceb1b7f378a23b765728e7629bbd3283f7289123634994d742b8f4617c3663dd")
        pubkey_u: bytes = b("04"
                            "ceb1b7f378a23b765728e7629bbd3283f7289123634994d742b8f4617c3663dd"
                            "7f99ed8354f384b39724bd8d81159028e85f5af0e7471023bc94d96a9e72c4fc")
        pubkey_exp: tuple[int, int] = (
            93490448322171366308997730228944117434252538148664993621081956959551078425565,
            57715698625569537031334996032706854239943749628299835406117911428008835728636
        )
        self.assertEqual(parse_pubkey(pubkey_c), pubkey_exp)
        self.assertEqual(parse_pubkey(pubkey_u), pubkey_exp)