#!/usr/bin/env python3

from myhdl import *
from .components import *


@block
def ram(dout, din, addr, we, clk, rst, width, depth):
    loads = [Signal(bool(0)) for i in range(depth)]
    outputs = [Signal(modbv(0)[width:]) for i in range(depth)]
    registersList = [None for i in range(depth)]
    for i in range(depth):
        registersList[i] = registerN(din, loads[i], outputs[i], width, clk, rst)
    
    @always_comb
    def comb():        
        for i in range(depth):
            if i == addr:
                if we == 1 :
                    loads[addr].next = 1
                else:
                    loads[addr].next = 0
            else:
                loads[i].next = 0
        dout.next = outputs[addr]
    return instances()


@block
def inc(q, a):
  
    @always_comb
    def comb():
        q.next = a + 1

    return instances()

@block
def pc(increment, load, i, output, width, clk, rst):
    regIn = Signal(modbv(0)[width:])
    regOut = Signal(modbv(0)[width:])
    regLoad = Signal(bool(0))
    incOut = Signal(modbv(0)[width:])
    muxOut1 = Signal(modbv(0)[width:])
    muxOut2 = Signal(modbv(0)[width:])

    inc16 = inc(incOut, regOut)
    
    mux1 = mux2way(muxOut1, regOut, incOut, increment)
    mux2 = mux2way(muxOut2, muxOut1, False, rst)
    mux3 = mux2way(regIn, muxOut2, i, load)


    registrador = registerN(regIn, regLoad, regOut, width, clk, rst)

    @always_comb
    def comb():
        regLoad.next = increment or rst or load
        output.next = regOut
    

    return instances()


@block
def registerN(i, load, output, width, clk, rst):
    binaryDigitList = [None for n in range(width)]
    outputs = [Signal(bool(0)) for n in range(width)]
 
    for j in range(width):
        binaryDigitList[j] = binaryDigit(i(j) , load, outputs[j], clk, rst)
 
    @always_comb
    def comb():
        output.next = ConcatSignal(*reversed(outputs))
 
    return instances()
 
 
@block
def register8(i, load, output, clk, rst):
    binaryDigitList = [None for n in range(8)]
    output_n = [Signal(bool(0)) for n in range(8)]
    for j in range(8):
        binaryDigitList[j] = binaryDigit(i(j), load, output_n[j], clk, rst)
 
    @always_comb
    def comb():
            output.next  = ConcatSignal(*reversed(output_n))
    return instances()


@block
def binaryDigit(i, load, output, clk, rst):

    q, d, clear, presset,aux = [Signal(bool(0)) for i in range(5)]
    df = dff(q,aux,clear,presset,clk,rst)

    @always_comb
    def comb():
        if load == 0:
            aux.next = q
        else:
            aux.next = i
        output.next = q
        
        
    return instances()


@block
def dff(q, d, clear, presset, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def logic():
        if clear:
            q.next = 0
        elif presset:
            q.next = 1
        else:
            q.next = d

    return instances()