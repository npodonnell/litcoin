#!/usr/bin/env python3

from litcoin.binhex import b

class ScriptOp(object):
    def __init__(self, opcode, name):
        self.opcode = opcode
        self.name = name

    def __str__(self):
        return 'OP_' + self.name

    def __repr__(self):
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
OP_NOP = ScriptOp(b('61'), 'NOP')
OP_VER = ScriptOp(b('62'), 'VER')
OP_IF = ScriptOp(b('63'), 'IF')
OP_NOTIF = ScriptOp(b('64'), 'NOTIF')
OP_VERIF = ScriptOp(b('65'), 'VERIF')
OP_VERNOTIF = ScriptOp(b('66'), 'VERNOTIF')
OP_ELSE = ScriptOp(b('67'), 'ELSE')
OP_ENDIF = ScriptOp(b('68'), 'ENDIF')
OP_VERIFY = ScriptOp(b('69'), 'VERIFY')
OP_RETURN = ScriptOp(b('6a'), 'RETURN')

# stack ops
OP_TOALTSTACK = ScriptOp(b('6b'), 'TOALTSTACK')
OP_FROMALTSTACK = ScriptOp(b('6c'), 'FROMALTSTACK')
OP_2DROP = ScriptOp(b('6d'), '2DROP')
OP_2DUP = ScriptOp(b('6e'), '2DUP')
OP_3DUP = ScriptOp(b('6f'), '3DUP')
OP_2OVER = ScriptOp(b('70'), '2OVER')
OP_2ROT = ScriptOp(b('71'), '2ROT')
OP_2SWAP = ScriptOp(b('72'), '2SWAP')
OP_IFDUP = ScriptOp(b('73'), 'IFDUP')
OP_DEPTH = ScriptOp(b('74'), 'DEPTH')
OP_DROP = ScriptOp(b('75'), 'DROP')
OP_DUP = ScriptOp(b('76'), 'DUP')
OP_NIP = ScriptOp(b('77'), 'NIP')
OP_OVER = ScriptOp(b('78'), 'OVER')
OP_PICK = ScriptOp(b('79'), 'PICK')
OP_ROLL = ScriptOp(b('7a'), 'ROLL')
OP_ROT = ScriptOp(b('7b'), 'ROT')
OP_SWAP = ScriptOp(b('7c'), 'SWAP')
OP_TUCK = ScriptOp(b('7d'), 'TUCK')

# splice ops
OP_CAT = ScriptOp(b('7e'), 'CAT')
OP_SUBSTR = ScriptOp(b('7f'), 'SUBSTR')
OP_LEFT = ScriptOp(b('80'), 'LEFT')
OP_RIGHT = ScriptOp(b('81'), 'RIGHT')
OP_SIZE = ScriptOp(b('82'), 'SIZE')

# bit logic
OP_INVERT = ScriptOp(b('83'), 'INVERT')
OP_AND = ScriptOp(b('84'), 'AND')
OP_OR = ScriptOp(b('85'), 'OR')
OP_XOR = ScriptOp(b('86'), 'XOR')
OP_EQUAL = ScriptOp(b('87'), 'EQUAL')
OP_EQUALVERIFY = ScriptOp(b('88'), 'EQUALVERIFY')
OP_RESERVED1 = ScriptOp(b('89'), 'RESERVED1')
OP_RESERVED2 = ScriptOp(b('8a'), 'RESERVED2')

# numeric
OP_1ADD = ScriptOp(b('8b'), '1ADD')
OP_1SUB = ScriptOp(b('8c'), '1SUB')
OP_2MUL = ScriptOp(b('8d'), '2MUL')
OP_2DIV = ScriptOp(b('8e'), '2DIV')
OP_NEGATE = ScriptOp(b('8f'), 'NEGATE')
OP_ABS = ScriptOp(b('90'), 'ABS')
OP_NOT = ScriptOp(b('91'), 'NOT')
OP_0NOTEQUAL = ScriptOp(b('92'), '0NOTEQUAL')

OP_ADD = ScriptOp(b('93'), 'ADD')
OP_SUB = ScriptOp(b('94'), 'SUB')
OP_MUL = ScriptOp(b('95'), 'MUL')
OP_DIV = ScriptOp(b('96'), 'DIV')
OP_MOD = ScriptOp(b('97'), 'MOD')
OP_LSHIFT = ScriptOp(b('98'), 'LSHIFT')
OP_RSHIFT = ScriptOp(b('99'), 'RSHIFT')

OP_BOOLAND = ScriptOp(b('9a'), 'BOOLAND')
OP_BOOLOR = ScriptOp(b('9b'), 'BOOLOR')
OP_NUMEQUAL = ScriptOp(b('9c'), 'NUMEQUAL')
OP_NUMEQUALVERIFY = ScriptOp(b('9d'), 'NUMEQUALVERIFY')
OP_NUMNOTEQUAL = ScriptOp(b('9e'), 'NUMNOTEQUAL')
OP_LESSTHAN = ScriptOp(b('9f'), 'LESSTHAN')
OP_GREATERTHAN = ScriptOp(b('a0'), 'GREATERTHAN')
OP_LESSTHANOREQUAL = ScriptOp(b('a1'), 'LESSTHANOREQUAL')
OP_GREATERTHANOREQUAL = ScriptOp(b('a2'), 'GREATERTHANOREQUAL')
OP_MIN = ScriptOp(b('a3'), 'MIN')
OP_MAX = ScriptOp(b('a4'), 'MAX')

OP_WITHIN = ScriptOp(b('a5'), 'WITHIN')

# crypto
OP_RIPEMD160 = ScriptOp(b('a6'), 'RIPEMD160')
OP_SHA1 = ScriptOp(b('a7'), 'SHA1')
OP_SHA256 = ScriptOp(b('a8'), 'SHA256')
OP_HASH160 = ScriptOp(b('a9'), 'HASH160')
OP_HASH256 = ScriptOp(b('aa'), 'HASH256')
OP_CODESEPARATOR = ScriptOp(b('ab'), 'CODESEPARATOR')
OP_CHECKSIG = ScriptOp(b('ac'), 'CHECKSIG')
OP_CHECKSIGVERIFY = ScriptOp(b('ad'), 'CHECKSIGVERIFY')
OP_CHECKMULTISIG = ScriptOp(b('ae'), 'CHECKMULTISIG')
OP_CHECKMULTISIGVERIFY = ScriptOp(b('af'), 'CHECKMULTISIGVERIFY')

# expansion
OP_NOP1 = ScriptOp(b('b0'), 'NOP1')
OP_CHECKLOCKTIMEVERIFY = ScriptOp(b('b1'), 'CHECKLOCKTIMEVERIFY')
OP_NOP2 = ScriptOp(b('b1'), 'NOP2')
OP_CHECKSEQUENCEVERIFY = ScriptOp(b('b2'), 'CHECKSEQUENCEVERIFY')
OP_NOP3 = ScriptOp(b('b2'), 'NOP3')
OP_NOP4 = ScriptOp(b('b3'), 'NOP4')
OP_NOP5 = ScriptOp(b('b4'), 'NOP5')
OP_NOP6 = ScriptOp(b('b5'), 'NOP6')
OP_NOP7 = ScriptOp(b('b6'), 'NOP7')
OP_NOP8 = ScriptOp(b('b7'), 'NOP8')
OP_NOP9 = ScriptOp(b('b8'), 'NOP9')
OP_NOP10 = ScriptOp(b('b9'), 'NOP10')

OP_INVALIDOPCODE = ScriptOp(b('ff'), 'INVALIDOPCODE')
