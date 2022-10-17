#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from myhdl import *
from ula import ula 
from components import *
from ula import *


@block
def toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, CLOCK_50, RESET_N):
    sw_s = [SW(i) for i in range(8)]
    key_s = [KEY(i) for i in range(10)]
    ledr_s = [Signal(bool(0)) for i in range(10)]
    x = Signal(intbv(0)[16:])
    y = Signal(intbv(0)[16:])

    #sw_s = [SW(i) for i in range(10)]
    #key_s = [KEY(i) for i in range(10)]
    ledr_s = [Signal(bool(0)) for i in range(10)]


    # B - Logica combinacional
    # bc0 = Signal(intbv(0)[4:])
    # bc1 = Signal(intbv(0)[4:])
    # hex0 = Signal(intbv(0)[7:])
    # hex1 = Signal(intbv(0)[7:])

    
    ula( x, y ,ledr_s ,sw_s, ledr_s[8], ledr_s[9])
    
    @always_comb
    def comb():
        for i in range(len(8)):
            LEDR[i].next = ledr_s[i]


    # ic1 = bin2bcd(SW, bc1, bc0)
    # ihex1 = bin2hex(hex1, bc1)
    # ihex0 = bin2hex(hex0, bc0)

    # C - ULA
    '''
    referencia do teste

    x = Signal(intbv(1)[16:])
    y = Signal(intbv(2)[16:])
    saida = Signal(intbv(0)[16:])
    control = Signal(intbv(0))
    zr = Signal(bool(0))
    ng = Signal(bool(0))
    ula_1 = ula(x, y, control, zr, ng, saida)
    '''
    x = Signal(intbv(1)[16:])
    y = Signal(intbv(2)[16:])
    saida = Signal(intbv(0)[16:])
    #control = Signal(intbv(0)[6:0])
    zr = Signal(bool(0))
    ng = Signal(bool(0))
    ula_1 = ula(x, y, SW, zr, ng, saida)



    # ---------------------------------------- #
    @always_comb
    def comb():
        for i in range(8):
            LEDR[i].next = saida[i]
        LEDR[8].next = zr
        LEDR[9].next = ng

    # ---------------------------------------- #
    # @always_comb
    # def comb():
    #     for i in range(len(ledr_s)):
    #         LEDR[i].next = ledr_s[i]

    return instances()


LEDR = Signal(intbv(0)[10:])
SW = Signal(intbv(0)[10:])
KEY = Signal(intbv(0)[4:])
HEX0 = Signal(intbv(1)[7:])
HEX1 = Signal(intbv(1)[7:])
HEX2 = Signal(intbv(1)[7:])
HEX3 = Signal(intbv(1)[7:])
HEX4 = Signal(intbv(1)[7:])
HEX5 = Signal(intbv(1)[7:])
CLOCK_50 = Signal(bool())
RESET_N = ResetSignal(0, active=0, isasync=True)

top = toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, CLOCK_50, RESET_N)
top.convert(hdl="VHDL")
