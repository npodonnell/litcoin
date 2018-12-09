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
OP_NOP = ScriptOp(b('61'))
OP_VER = ScriptOp(b('62'))
OP_IF = ScriptOp(b('63'))
OP_NOTIF = ScriptOp(b('64'))
OP_VERIF = ScriptOp(b('65'))
OP_VERNOTIF = ScriptOp(b('66'))
OP_ELSE = ScriptOp(b('67'))
OP_ENDIF = ScriptOp(b('68'))
OP_VERIFY = ScriptOp(b('69'))
OP_RETURN = ScriptOp(b('6a'))

# stack ops
OP_TOALTSTACK = ScriptOp(b('6b'))
OP_FROMALTSTACK = ScriptOp(b('6c'))
OP_2DROP = ScriptOp(b('6d'))
OP_2DUP = ScriptOp(b('6e'))
OP_3DUP = ScriptOp(b('6f'))
OP_2OVER = ScriptOp(b('70'))
OP_2ROT = ScriptOp(b('71'))
OP_2SWAP = ScriptOp(b('72'))
OP_IFDUP = ScriptOp(b('73'))
OP_DEPTH = ScriptOp(b('74'))
OP_DROP = ScriptOp(b('75'))
OP_DUP = ScriptOp(b('76'))
OP_NIP = ScriptOp(b('77'))
OP_OVER = ScriptOp(b('78'))
OP_PICK = ScriptOp(b('79'))
OP_ROLL = ScriptOp(b('7a'))
OP_ROT = ScriptOp(b('7b'))
OP_SWAP = ScriptOp(b('7c'))
OP_TUCK = ScriptOp(b('7d'))

# splice ops
OP_CAT = ScriptOp(b('7e'))
OP_SUBSTR = ScriptOp(b('7f'))
OP_LEFT = ScriptOp(b('80'))
OP_RIGHT = ScriptOp(b('81'))
OP_SIZE = ScriptOp(b('82'))

# bit logic
OP_INVERT = ScriptOp(b('83'))
OP_AND = ScriptOp(b('84'))
OP_OR = ScriptOp(b('85'))
OP_XOR = ScriptOp(b('86'))
OP_EQUAL = ScriptOp(b('87'))
OP_EQUALVERIFY = ScriptOp(b('88'))
OP_RESERVED1 = ScriptOp(b('89'))
OP_RESERVED2 = ScriptOp(b('8a'))

# numeric
OP_1ADD = ScriptOp(b('8b'))
OP_1SUB = ScriptOp(b('8c'))
OP_2MUL = ScriptOp(b('8d'))
OP_2DIV = ScriptOp(b('8e'))
OP_NEGATE = ScriptOp(b('8f'))
OP_ABS = ScriptOp(b('90'))
OP_NOT = ScriptOp(b('91'))
OP_0NOTEQUAL = ScriptOp(b('92'))

OP_ADD = ScriptOp(b('93'))
OP_SUB = ScriptOp(b('94'))
OP_MUL = ScriptOp(b('95'))
OP_DIV = ScriptOp(b('96'))
OP_MOD = ScriptOp(b('97'))
OP_LSHIFT = ScriptOp(b('98'))
OP_RSHIFT = ScriptOp(b('99'))

OP_BOOLAND = ScriptOp(b('9a'))
OP_BOOLOR = ScriptOp(b('9b'))
OP_NUMEQUAL = ScriptOp(b('9c'))
OP_NUMEQUALVERIFY = ScriptOp(b('9d'))
OP_NUMNOTEQUAL = ScriptOp(b('9e'))
OP_LESSTHAN = ScriptOp(b('9f'))
OP_GREATERTHAN = ScriptOp(b('a0'))
OP_LESSTHANOREQUAL = ScriptOp(b('a1'))
OP_GREATERTHANOREQUAL = ScriptOp(b('a2'))
OP_MIN = ScriptOp(b('a3'))
OP_MAX = ScriptOp(b('a4'))

OP_WITHIN = ScriptOp(b('a5'))

# crypto
OP_RIPEMD160 = ScriptOp(b('a6'))
OP_SHA1 = ScriptOp(b('a7'))
OP_SHA256 = ScriptOp(b('a8'))
OP_HASH160 = ScriptOp(b('a9'))
OP_HASH256 = ScriptOp(b('aa'))
OP_CODESEPARATOR = ScriptOp(b('ab'))
OP_CHECKSIG = ScriptOp(b('ac'))
OP_CHECKSIGVERIFY = ScriptOp(b('ad'))
OP_CHECKMULTISIG = ScriptOp(b('ae'))
OP_CHECKMULTISIGVERIFY = ScriptOp(b('af'))

# expansion
OP_NOP1 = ScriptOp(b('b0'))
OP_CHECKLOCKTIMEVERIFY = ScriptOp(b('b1'))
OP_NOP2 = ScriptOp(b('b1'))
OP_CHECKSEQUENCEVERIFY = ScriptOp(b('b2'))
OP_NOP3 = ScriptOp(b('b2'))
OP_NOP4 = ScriptOp(b('b3'))
OP_NOP5 = ScriptOp(b('b4'))
OP_NOP6 = ScriptOp(b('b5'))
OP_NOP7 = ScriptOp(b('b6'))
OP_NOP8 = ScriptOp(b('b7'))
OP_NOP9 = ScriptOp(b('b8'))
OP_NOP10 = ScriptOp(b('b9'))

OP_INVALIDOPCODE = ScriptOp(b('ff'))
