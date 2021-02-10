from litcoin.serialization import ensure_enough_data

INT64_SIZE_IN_BYTES = 8


def validate_int64(n):
    assert type(n) == int, "type of `n` should be int"
    assert -0x8000000000000000 <= n <= 0x7fffffffffffffff, "`n` must fit within 64 bits"


def serialize_int64(n):
    validate_int64(n)
    return int.to_bytes(n, INT64_SIZE_IN_BYTES, byteorder="little", signed=True)


def deserialize_int64(data, pos=0):
    ensure_enough_data(data, pos, INT64_SIZE_IN_BYTES)
    next_pos = pos + INT64_SIZE_IN_BYTES
    res = int.from_bytes(data[pos : next_pos], byteorder="little", signed=True)
    return res, next_pos
