#!/usr/bin/env python3

from myhdl import *


@block
def ula(x, y, c, zr, ng, saida, width=16):

    zx_out = Signal(intbv(0)[width:])
    nx_out = Signal(intbv(0)[width:])
    zy_out = Signal(intbv(0)[width:])
    ny_out = Signal(intbv(0)[width:])
    and_out = Signal(intbv(0)[width:])
    add_out = Signal(intbv(0)[width:])
    mux_out = Signal(intbv(0)[width:])
    no_out = Signal(intbv(0)[width:])

    c_zx = c(5)
    c_nx = c(4)
    c_zy = c(3)
    c_ny = c(2)
    c_f = c(1)
    c_no = c(0)

    @always_comb
    def comb():
        pass

    return instances()


# -z faz complemento de dois
# ~z inverte bit a bit
@block
def inversor(z, a, y):
    @always_comb
    def comb():
        pass

    return instances()


@block
def comparador(a, zr, ng, width):
    # width insica o tamanho do vetor a
    @always_comb
    def comb():
        pass

    return instances()


@block
def zerador(z, a, y):
    @always_comb
    def comb():
        pass

    return instances()


@block
def add(a, b, q):
    @always_comb
    def comb():
        q.next = a+b

    return instances()


@block
def inc(a, q):
    @always_comb
    def comb():
        pass

    return instances()


# ----------------------------------------------
# Conceito B
# ----------------------------------------------


@block
def halfAdder(a, b, soma, carry):
    s = Signal(bool())
    c = Signal(bool())

    @always_comb
    def comb():
        s = a ^ b
        c = a & b

        soma.next = s
        carry.next = c

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]  


    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()

@block
def adder(x, y, soma, carry):
    n = len(x)
    temp = [Signal(bool(0)) for i in range(n)]
    faList = [None for i in range(n)]
    faList[0] = halfAdder(x[0],y[0],soma[0], temp[0])
    for i in range(1,n):
        faList[i] = fullAdder(x[i], y[i], temp[i-1], soma[i],temp[i])


    @always_comb
    def comb():
        carry.next = temp[n-1]
        faList = [None for i in range(4)]

    return instances()

@block
def addcla4(a, b, q):
    a_ = [a(i) for i in range(4)]
    b_ = [b(i) for i in range(4)]
   
    temp_carry = [Signal(bool(0)) for i in range(5)]
    
    k_list = [Signal(bool(0)) for i in range(4)]
    p_list = [Signal(bool(0)) for i in range(4)]
    g_list = [Signal(bool(0)) for i in range(4)]
    faList = [None for i in range(4)] 
    guarda_carry_full = [None for i in range(4)]
    
    for i in range(4):
        faList[i] = fullAdder(a_[i], b_[i], temp_carry[i], q[i], guarda_carry_full[i])

    @always_comb
    def comb():
        # q.next = a+b
        for i in range(4):
            k_list[i] = (not a_[i]) and (not b_[i])
            g_list[i] = a_[i] and b_[i]
            p_list[i] = ((not a_[i]) and b_[i]) and ((not b_[i]) and a_[i])

        temp_carry[0] = 0
        temp_carry[1] = g_list[0] or (p_list[0] and temp_carry[0])
        temp_carry[2] = g_list[1] or (p_list[1] and g_list[0]) or (p_list[1] and p_list[0] and temp_carry[0])
        temp_carry[3] = g_list[2] or (p_list[2] and g_list[1]) or (p_list[2] and p_list[1] and g_list[0]) or (p_list[2] and p_list[1] and p_list[0] and temp_carry[0])
        temp_carry[4] = g_list[3] or (p_list[3] and g_list[2]) or (p_list[3] and p_list[2] and g_list[1]) or (p_list[3] and p_list[2] and p_list[1] and g_list[0]) or (p_list[3] and p_list[2] and p_list[1] and p_list[0] and temp_carry[0])

        



    return instances()

@block
def addcla16(a, b, q):
    @always_comb
    def comb():
        pass

    return instances()


# ----------------------------------------------
# Conceito A
# ----------------------------------------------


@block
def ula_new(x, y, c, zr, ng, sr, sf, bcd, saida, width=16):
    pass


@block
def bcdAdder(x, y, z):
    pass
