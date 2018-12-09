#!/usr/bin/env python3

from litcoin.binhex import b

class ScriptOp(object):
    def __init__(self, opcode, name):
        self.opcode = opcode
        self.name = name

    def __str__(self):
        return 'OP_' + self.name


# push value
OP_0 = ScriptOp(b('00'), '0')
OP_FALSE = ScriptOp(b('00'), 'FALSE')
OP_PUSHDATA1 = ScriptOp(b('4c'), 'PUSHDATA1')
OP_PUSHDATA2 = ScriptOp(b('4d'), 'PUSHDATA2')
OP_PUSHDATA4 = ScriptOp(b('4e'), 'PUSHDATA4')
OP_1NEGATE = ScriptOp(b('4f'), '1NEGATE')
OP_RESERVED = ScriptOp(b('50'), 'RESERVED')
OP_1 = ScriptOp(b('51'), '1')
OP_TRUE = ScriptOp(b('51'), 'TRUE')
OP_2 = ScriptOp(b('52'), '2')
OP_3 = ScriptOp(b('53'), '3')
OP_4 = ScriptOp(b('54'), '4')
OP_5 = ScriptOp(b('55'), '5')
OP_6 = ScriptOp(b('56'), '6')
OP_7 = ScriptOp(b('57'), '7')
OP_8 = ScriptOp(b('58'), '8')
OP_9 = ScriptOp(b('59'), '9')
OP_10 = ScriptOp(b('5a'), '10')
OP_11 = ScriptOp(b('5b'), '11')
OP_12 = ScriptOp(b('5c'), '12')
OP_13 = ScriptOp(b('5d'), '13')
OP_14 = ScriptOp(b('5e'), '14')
OP_15 = ScriptOp(b('5f'), '15')
OP_16 = ScriptOp(b('60'), '16')

# control
OP_NOP = ScriptOp(0x61)
OP_VER = ScriptOp(0x62)
OP_IF = ScriptOp(0x63)
OP_NOTIF = ScriptOp(0x64)
OP_VERIF = ScriptOp(0x65)
OP_VERNOTIF = ScriptOp(0x66)
OP_ELSE = ScriptOp(0x67)
OP_ENDIF = ScriptOp(0x68)
OP_VERIFY = ScriptOp(0x69)
OP_RETURN = ScriptOp(0x6a)

# stack ops
OP_TOALTSTACK = ScriptOp(0x6b)
OP_FROMALTSTACK = ScriptOp(0x6c)
OP_2DROP = ScriptOp(0x6d)
OP_2DUP = ScriptOp(0x6e)
OP_3DUP = ScriptOp(0x6f)
OP_2OVER = ScriptOp(0x70)
OP_2ROT = ScriptOp(0x71)
OP_2SWAP = ScriptOp(0x72)
OP_IFDUP = ScriptOp(0x73)
OP_DEPTH = ScriptOp(0x74)
OP_DROP = ScriptOp(0x75)
OP_DUP = ScriptOp(0x76)
OP_NIP = ScriptOp(0x77)
OP_OVER = ScriptOp(0x78)
OP_PICK = ScriptOp(0x79)
OP_ROLL = ScriptOp(0x7a)
OP_ROT = ScriptOp(0x7b)
OP_SWAP = ScriptOp(0x7c)
OP_TUCK = ScriptOp(0x7d)

# splice ops
OP_CAT = ScriptOp(0x7e)
OP_SUBSTR = ScriptOp(0x7f)
OP_LEFT = ScriptOp(0x80)
OP_RIGHT = ScriptOp(0x81)
OP_SIZE = ScriptOp(0x82)

# bit logic
OP_INVERT = ScriptOp(0x83)
OP_AND = ScriptOp(0x84)
OP_OR = ScriptOp(0x85)
OP_XOR = ScriptOp(0x86)
OP_EQUAL = ScriptOp(0x87)
OP_EQUALVERIFY = ScriptOp(0x88)
OP_RESERVED1 = ScriptOp(0x89)
OP_RESERVED2 = ScriptOp(0x8a)

# numeric
OP_1ADD = ScriptOp(0x8b)
OP_1SUB = ScriptOp(0x8c)
OP_2MUL = ScriptOp(0x8d)
OP_2DIV = ScriptOp(0x8e)
OP_NEGATE = ScriptOp(0x8f)
OP_ABS = ScriptOp(0x90)
OP_NOT = ScriptOp(0x91)
OP_0NOTEQUAL = ScriptOp(0x92)

OP_ADD = ScriptOp(0x93)
OP_SUB = ScriptOp(0x94)
OP_MUL = ScriptOp(0x95)
OP_DIV = ScriptOp(0x96)
OP_MOD = ScriptOp(0x97)
OP_LSHIFT = ScriptOp(0x98)
OP_RSHIFT = ScriptOp(0x99)

OP_BOOLAND = ScriptOp(0x9a)
OP_BOOLOR = ScriptOp(0x9b)
OP_NUMEQUAL = ScriptOp(0x9c)
OP_NUMEQUALVERIFY = ScriptOp(0x9d)
OP_NUMNOTEQUAL = ScriptOp(0x9e)
OP_LESSTHAN = ScriptOp(0x9f)
OP_GREATERTHAN = ScriptOp(0xa0)
OP_LESSTHANOREQUAL = ScriptOp(0xa1)
OP_GREATERTHANOREQUAL = ScriptOp(0xa2)
OP_MIN = ScriptOp(0xa3)
OP_MAX = ScriptOp(0xa4)

OP_WITHIN = ScriptOp(0xa5)

# crypto
OP_RIPEMD160 = ScriptOp(0xa6)
OP_SHA1 = ScriptOp(0xa7)
OP_SHA256 = ScriptOp(0xa8)
OP_HASH160 = ScriptOp(0xa9)
OP_HASH256 = ScriptOp(0xaa)
OP_CODESEPARATOR = ScriptOp(0xab)
OP_CHECKSIG = ScriptOp(0xac)
OP_CHECKSIGVERIFY = ScriptOp(0xad)
OP_CHECKMULTISIG = ScriptOp(0xae)
OP_CHECKMULTISIGVERIFY = ScriptOp(0xaf)

# expansion
OP_NOP1 = ScriptOp(0xb0)
OP_CHECKLOCKTIMEVERIFY = ScriptOp(0xb1)
OP_NOP2 = ScriptOp(0xb1)
OP_CHECKSEQUENCEVERIFY = ScriptOp(0xb2)
OP_NOP3 = ScriptOp(0xb2)
OP_NOP4 = ScriptOp(0xb3)
OP_NOP5 = ScriptOp(0xb4)
OP_NOP6 = ScriptOp(0xb5)
OP_NOP7 = ScriptOp(0xb6)
OP_NOP8 = ScriptOp(0xb7)
OP_NOP9 = ScriptOp(0xb8)
OP_NOP10 = ScriptOp(0xb9)

OP_INVALIDOPCODE = ScriptOp(0xff)

