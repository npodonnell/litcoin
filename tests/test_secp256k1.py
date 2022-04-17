from litcoin.secp256k1 import POINT_AT_INFINITY, SECP256K1_GENERATOR, SECP256K1_ORDER, \
    secp256k1_random_scalar, secp256k1_add, secp256k1_multiply
import unittest


class TestSecp256k1(unittest.TestCase):
    def test_secp256k1_random_scalar(self):
        scalar_1: int = secp256k1_random_scalar()
        scalar_2: int = secp256k1_random_scalar()
        assert scalar_1 != scalar_2
        assert 1 <= scalar_1 <= SECP256K1_ORDER - 1
        assert 1 <= scalar_2 <= SECP256K1_ORDER - 1

    def test_secp256k1_add(self):
        self.assertEqual(POINT_AT_INFINITY, secp256k1_add(POINT_AT_INFINITY, POINT_AT_INFINITY))
        self.assertEqual(SECP256K1_GENERATOR, secp256k1_add(SECP256K1_GENERATOR, POINT_AT_INFINITY))
        self.assertEqual(SECP256K1_GENERATOR, secp256k1_add(POINT_AT_INFINITY, SECP256K1_GENERATOR))
        # TODO: more tests

    def test_secp256k1_multiply(self):
        self.assertEqual(POINT_AT_INFINITY, secp256k1_multiply(0))
        self.assertEqual(SECP256K1_GENERATOR, secp256k1_multiply(1))
        self.assertEqual(SECP256K1_GENERATOR, secp256k1_multiply(1, SECP256K1_GENERATOR))
        self.assertEqual(POINT_AT_INFINITY, secp256k1_multiply(SECP256K1_ORDER, SECP256K1_GENERATOR))
        self.assertEqual(POINT_AT_INFINITY, secp256k1_multiply(0, POINT_AT_INFINITY))
        self.assertEqual(POINT_AT_INFINITY, secp256k1_multiply(1, POINT_AT_INFINITY))
        self.assertEqual(POINT_AT_INFINITY, secp256k1_multiply(2, POINT_AT_INFINITY))
        # TODO: more tests