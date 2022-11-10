#!/usr/bin/env python3
#

from .ASMcode import Code


def erroMsg(tst, result):
    return "Test fail: {} | code result: {}".format(tst, result)


def test_dest():
    
    test_vector = [
        [["movw", "%A", "%D"], "010"],
        [["movw", "%A", "(%A)"], "100"],
        [["movw", "%A", "%D", "(%A)"], "110"],
        [["movw", "(%A)", "%D"], "010"],
        [["addw", "(%A)", "%D", "%D"], "010"],
        [["incw", "%A"], "001"],
        [["incw", "%D"], "010"],
        [["incw", "(%A)"], "100"],
        [["nop"], "000"],
        [["subw", "%D", "(%A)", "%A"], "001"],
        [["rsubw", "%D", "(%A)", "%A"], "001"],
        [["decw", "%A"], "001"],
        [["decw", "%D"], "010"],
        [["notw", "%A"], "001"],
        [["notw", "%D"], "010"],
        [["negw", "%A"], "001"],
        [["negw", "%D"], "010"],
        [["andw", "(%A)", "%D", "%D"], "010"],
        [["andw", "%D", "%A", "%A"], "001"],
        [["orw", "(%A)", "%D", "%D"], "010"],
        [["orw", "%D", "%A", "%A"], "001"],
        [["jmp"], "000"],
        [["je"], "000"],
        [["jne"], "000"],
        [["jg"], "000"],
        [["jge"], "000"],
        [["jl"], "000"],
        [["jle"], "000"],
    ]

    code = Code()
    for t in test_vector:
        result = code.dest(t[0])
        assert result == t[1], erroMsg(t, result)


def test_comp():
    test_vector = [
        [["movw", "%A", "%D"], "0110000"],
        [["movw", "%D", "%A"], "0001100"],
        [["movw", "%D", "(%A)"], "0001100"],
        [["movw", "(%A)", "%A"], "1110000"],
        [["movw", "%A", "(%A)"], "0110000"],
        [["movw", "$1", "%D"], "0111111"],
        [["addw", "%A", "%D", "%D"], "0000010"],
        [["addw", "(%A)", "%D", "%D"], "1000010"],
        [["addw", "$1", "(%A)", "%D"], "1110111"],
        [["incw", "%A"], "0110111"],
        [["incw", "%D"], "0011111"],
        [["incw", "(%A)"], "1110111"],
        [["movw", "(%A)", "%D"], "1110000"],
        [["addw", "(%A)", "%D", "%D"], "1000010"],
        [["subw", "%D", "(%A)", "%A"], "1010011"],
        [["rsubw", "%D", "(%A)", "%A"], "1000111"],
        [["decw", "%A"], "0110010"],
        [["decw", "%D"], "0001110"],
        [["notw", "%A"], "0110001"],
        [["notw", "%D"], "0001101"],
        [["negw", "%A"], "0110011"],
        [["negw", "%D"], "0001111"],
        [["andw", "(%A)", "%D", "%D"], "1000000"],
        [["andw", "%D", "%A", "%A"], "0000000"],
        [["orw", "(%A)", "%D", "%D"], "1010101"],
        [["orw", "%D", "%A", "%A"], "0010101"],
        [["subw", "(%A)", "$1", "%A"], "1110010"],
        [["jmp"], "0001100"],
        [["je"], "0001100"],
        [["jne"], "0001100"],
        [["jg"], "0001100"],
        [["jge"], "0001100"],
        [["jl"], "0001100"],
        [["jle"], "0001100"],
    ]

    code = Code()
    for t in test_vector:
        result = code.comp(t[0])
        assert result == t[1], erroMsg(t, result)


def test_jump():
    test_vector = [

        [["jmp"], "111"],
        [["je"], "010"],
        [["jne"], "101"],
        [["jg"], "001"],
        [["jge"], "011"],
        [["jl"], "100"],
        [["jle"], "110"],
    ]
    code = Code()
    for t in test_vector:
        result = code.jump(t[0])
        assert result == t[1], erroMsg(t, result)


def test_toBinary():
    test_vector = [
        ["0", "0000000000000000"],
        ["1", "0000000000000001"],
        ["10", "0000000000001010"],
        ["100", "0000000001100100"],
        ["1000", "0000001111101000"],
        ["21845", "0101010101010101"],
        ["32767", "0111111111111111"],
        ["32767", "0111111111111111"],
        ["65535", "1111111111111111"],
        ["-10", "1111111111110110"],
    ]
    code = Code()
    for t in test_vector:
        result = code.toBinary(t[0])
        assert result == t[1], erroMsg(t, result)
