from litcoin.binhex import b, x
from litcoin.int32 import INT32_SIZE_IN_BYTES, validate_int32, serialize_int32, deserialize_int32
import unittest


class TestInt32(unittest.TestCase):
    def test_INT32_SIZE_IN_BYTES(self):
        assert INT32_SIZE_IN_BYTES == 4

    def test_validate_int32(self):
        validate_int32(0)
        validate_int32(0x7fffffff)
        validate_int32(-0x80000000)

        with self.assertRaises(AssertionError,
                               msg="should be raised because positive `n` argument is one too high"):
            validate_int32(0x80000000)
        with self.assertRaises(AssertionError,
                               msg="should be raised because negative `n` argument is one too low"):
            validate_int32(-0x80000001)
        with self.assertRaises(AssertionError, msg="should be raised because `n` argument is float"):
            validate_int32(0.0)
        with self.assertRaises(AssertionError, msg="should be raised because `n` argument is the wrong type"):
            validate_int32("wrong type")
        with self.assertRaises(TypeError, msg="should be raised because all arguments are missing"):
            validate_int32()

    def test_serialize_int32(self):
        assert serialize_int32(0) == b("00000000")
        assert serialize_int32(1) == b("01000000")
        assert serialize_int32(-1) == b("ffffffff")
        assert serialize_int32(2147483647) == b("ffffff7f")
        assert serialize_int32(-2147483648) == b("00000080")

        with self.assertRaises(AssertionError,
                               msg="should be raised because positive `n` argument is one too high"):
            serialize_int32(0x80000000)
        with self.assertRaises(AssertionError,
                               msg="should be raised because negative `n` argument is one too low"):
            serialize_int32(-0x80000001)
        with self.assertRaises(AssertionError, msg="should be raised because `n` argument is of the wrong type"):
            serialize_int32("wrong type")
        with self.assertRaises(TypeError, msg="should be raised because all arguments are missing"):
            serialize_int32()

    def test_deserialize_int32(self):
        assert deserialize_int32(b("00000000")) == (0, 4)
        assert deserialize_int32(b("01000000")) == (1, 4)
        assert deserialize_int32(b("ffffffff")) == (-1, 4)
        assert deserialize_int32(b("feffffff")) == (-2, 4)

        assert deserialize_int32(b("00000000"), 0) == (0, 4)
        assert deserialize_int32(b("01000000"), 0) == (1, 4)
        assert deserialize_int32(b("ffffffff"), 0) == (-1, 4)
        assert deserialize_int32(b("feffffff"), 0) == (-2, 4)

        assert deserialize_int32(b("00000000cc"), 0) == (0, 4)
        assert deserialize_int32(b("01000000cc"), 0) == (1, 4)
        assert deserialize_int32(b("ffffffffcc"), 0) == (-1, 4)
        assert deserialize_int32(b("feffffffcc"), 0) == (-2, 4)

        assert deserialize_int32(b("cc00000000"), 1) == (0, 5)
        assert deserialize_int32(b("cc01000000"), 1) == (1, 5)
        assert deserialize_int32(b("ccffffffff"), 1) == (-1, 5)
        assert deserialize_int32(b("ccfeffffff"), 1) == (-2, 5)

        assert deserialize_int32(b("cc00000000cc"), 1) == (0, 5)
        assert deserialize_int32(b("cc01000000cc"), 1) == (1, 5)
        assert deserialize_int32(b("ccffffffffcc"), 1) == (-1, 5)
        assert deserialize_int32(b("ccfeffffffcc"), 1) == (-2, 5)

        with self.assertRaises(AssertionError, msg="should be raised because `data` argument is 3 bytes long"):
            deserialize_int32(b("000000"))
        with self.assertRaises(AssertionError,
                               msg="should be raised because `i` argument is 0 when it should be 1 thus a different "
                                   "value is deserialized"):
            assert deserialize_int32(b("cc00000000"), 0) == 0
        with self.assertRaises(AssertionError,
                               msg="should be raised because `i` argument is 2 when it should be 1 thus there\"s an "
                                   "overflow"):
            deserialize_int32(b("cc00000000"), 2)
        with self.assertRaises(AssertionError, msg="should be raised because `data` argument is of the wrong type"):
            deserialize_int32("wrong type")
        with self.assertRaises(TypeError, msg="should be raised because all arguments are missing"):
            deserialize_int32()
