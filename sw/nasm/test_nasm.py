#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path
import math


def text_to_ram(text, offset=0):
    ram = {}
    for i in range(len(text)):
        ram[i + offset] = ord(text[i])
    return ram


def test_abs():
    ram = {1: -1}
    tst = {0: 1}
    assert nasm_test("abs.nasm", ram, tst)

    ram = {1: 35}
    tst = {0: 35}
    assert nasm_test("abs.nasm", ram, tst)


def test_max():
    ram = {0: 35, 1: 7}
    tst = {2: 35}
    assert nasm_test("max.nasm", ram, tst)

    ram = {0: 7, 1: 63}
    tst = {2: 63}
    assert nasm_test("max.nasm", ram, tst)


def test_mult():
    ram = {0: 3, 1: 2}
    tst = {3: 6}
    assert nasm_test("mult.nasm", ram, tst)

    ram = {0: 6, 1: 6}
    tst = {3: 36}
    assert nasm_test("mult.nasm", ram, tst, 100000)


def test_mod():
    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 32, 1: 5}
    tst = {2: 2}
    assert nasm_test("mod.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 1}
    assert nasm_test("mod.nasm", ram, tst, 10000)


def test_div():

    ram = {0: 0, 1: 0, 5: 5}
    tst = {5: 6}
    assert nasm_test("div.nasm", ram, tst)
  
    ram = {0: 1, 1: 0, 5: 5}
    tst = {5: 6}
    assert nasm_test("div.nasm", ram, tst)



    ram = {0: 3, 1: 0, 5: 5}
    tst = {5: 4}
    assert nasm_test("div.nasm", ram, tst)



    ram = {0: 0, 1: 1, 5: 5}
    tst = {5: 4}
    assert nasm_test("div.nasm", ram, tst)

def test_senha_certo():
    ram = {0: 9, 21184: 0, 21185: 9}
    tst = {21184: 1}
    assert nasm_test("div.nasm", ram, tst)

def text_to_ram(text, offset=0):
    ram = {}
    for i in range(len(text)):
        ram[i + offset] = ord(text[i])
    ram[1 + len(text)] = 0
    return ram



def test_uppercase_exemplo():
    ram = text_to_ram("Hello", 8)
    tst = text_to_ram("HELLO", 8)
    assert nasm_test("div.nasm", ram, tst, 4000)


def test_senha_errado():
    ram = {0: 9, 21184: 0, 21185: 2}
    tst = {21184: 6}
    assert nasm_test("div.nasm", ram, tst)


def test_isEven():
    ram = {0: 3, 5: 6}
    tst = {0: 1}
    assert nasm_test("isEven.nasm", ram, tst)

    ram = {0: 2, 5: 23}
    tst = {0: 0}
    assert nasm_test("isEven.nasm", ram, tst)


def test_pow():
    ram = {1: 2}
    tst = {0: 4}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 2}
    tst = {0: 4}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 16}
    tst = {0: 256}
    assert nasm_test("pow.nasm", ram, tst, 10000)


def test_stringLenght():
    ram = {}
    text = "oi tudo bem?"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)

    text = "o saci eh um ser muito especial"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)


def test_palindromo():
    ram = text_to_ram("ararr", 10)
    ram[0] = 2
    tst = {0: 0}
    print('deu ruim aqui entao')
    assert nasm_test("palindromo.nasm", ram, tst, 10000)

    ram = text_to_ram("arara", 10)
    ram[0] = 2
    tst = {0: 1}
    print(ram)
    print('deu ruim aqui?')
    assert nasm_test("palindromo.nasm", ram, tst, 10000)



def test_factorial():


    ram = {0: 3}
    tst = {1: 6}
    assert nasm_test("factorial.nasm", ram, tst, 10000)


def test_matriz():
    ram = {1000: 2, 1001: 1, 1003: 1, 1004: 2, 0: 3}
    tst = {0: 3}
    assert nasm_test("matrizDeterminante.nasm", ram, tst, 10000)

def test_vectorMean():
    ram = {4: 4, 5:1, 6:2, 7:1, 8:4}
    tst = {0: 2, 1:8}
    assert nasm_test("vectorMean.nasm", ram, tst, 10000)

    ram = {1:0, 4:3, 5:1, 6:1, 7:1}
    tst = {0: 1, 1:3}
    assert nasm_test("vectorMean.nasm", ram, tst, 100000)

    ram = {1:0, 4:3, 5:4, 6:1, 7:1}
    tst = {0: 2, 1:6}
    assert nasm_test("vectorMean.nasm", ram, tst, 100000)


def test_sweled():
    ram = {21185: 14}
    tst = {21185: 14, 21184: 496}
    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 6}
    tst = {21185: 6, 21184: 504}
    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 2}
    tst = {21185: 2, 21184: 508}
    assert nasm_test("SWeLED.nasm", ram, tst, 10000)


def test_multiploDois():
    ram = {0: 2, 5: -64}
    tst = {0: 1}
    assert nasm_test("multiploDeDois.nasm", ram, tst)

    ram = {0: 2, 5: 1023}
    tst = {0: 0}
    assert nasm_test("multiploDeDois.nasm", ram, tst)

    ram = {0: 2, 5: -1023}
    tst = {0: 0}
    assert nasm_test("multiploDeDois.nasm", ram, tst)


def test_sweled2():
    ram = {0: 0}
    tst = {21184: 436}
    assert nasm_test("SWeLED2.nasm", ram, tst, 100000)

    ram = {5: 8}
    tst = {21184:444}
    assert nasm_test("SWeLED2.nasm", ram, tst, 100000)
