#!/usr/bin/env python3

from .ASMparser import Parser


def test_advanced():
    fnasm = open('test_assets/mult.nasm', 'r')
    ptest = Parser(fnasm)

    assert ptest.advanced() is True
    assert ptest.command() == ['leaw', '$3', '%A']

    assert ptest.advanced() is True
    assert ptest.command() == ['movw', '$0', '(%A)']

    assert ptest.advanced() is True
    assert ptest.command() == ['loop:']

    assert ptest.advanced() is True
    assert ptest.command() == ['leaw', '$0', '%A']

    assert ptest.advanced() is True
    assert ptest.command() == ['movw', '(%A)', '%D']

    assert ptest.advanced() is True
    assert ptest.command() == ['end:']

    assert ptest.advanced() is False


def test_commandType():
    fnasm = open('test_assets/mult.nasm', 'r')
    ptest = Parser(fnasm)

    assert ptest.advanced() is True
    assert ptest.commandType() == ptest.CommandType['A']

    assert ptest.advanced() is True
    assert ptest.commandType() == ptest.CommandType['C']

    assert ptest.advanced() is True
    assert ptest.commandType() == ptest.CommandType['L']

    assert ptest.advanced() is True
    assert ptest.commandType() == ptest.CommandType['A']

    assert ptest.advanced() is True
    assert ptest.commandType() == ptest.CommandType['C']

    assert ptest.advanced() is True
    assert ptest.commandType() == ptest.CommandType['L']

    assert ptest.advanced() is False


def test_symbol():
    fnasm = open('test_assets/symbol.nasm', 'r')
    ptest = Parser(fnasm)

    assert ptest.advanced() is True
    assert ptest.symbol() == '1'

    assert ptest.advanced() is True
    assert ptest.symbol() == '3'

    assert ptest.advanced() is True
    assert ptest.symbol() == '45'

    assert ptest.advanced() is False


def test_labol():
    fnasm = open('test_assets/labol.nasm', 'r')
    ptest = Parser(fnasm)

    assert ptest.advanced() is True
    assert ptest.label() == 'OI'

    assert ptest.advanced() is True
    assert ptest.advanced() is True
    assert ptest.label() == 'END'

    assert ptest.advanced() is True

    assert ptest.advanced() is True
    assert ptest.label() == 'WHILE_1'

    assert ptest.advanced() is True
    assert ptest.advanced() is False
