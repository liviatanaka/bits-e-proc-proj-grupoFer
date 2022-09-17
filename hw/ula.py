#!/usr/bin/env python3

from signal import Signals
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

    # zeradores
    zerador_x = zerador(c_zx, x, zx_out)
    zerador_y = zerador(c_zy, y,zy_out)

    # inversores
    inversor_x = inversor(c_nx, zx_out, nx_out)
    inversor_y = inversor(c_ny, zy_out, ny_out)

    breakpoint()

    # mux
    print(f'nx-{nx_out}, ny{ny_out}' )
    adicao = add(nx_out, ny_out, add_out)
    
    print(f'nx-{nx_out}, ny{ny_out}, {add_out}' )
    xandy = x_and_y(nx_out, ny_out, and_out)
    mux = mux2way(mux_out, and_out, add_out, c_f)
    # def mux2way(q, a, b, sel):


    # inversor final
    inversor_final = inversor(c_no, mux_out, no_out)

    #comparador
    comparador_ = comparador(no_out, zr, ng, width)

    
    @always_comb
    def comb():
        saida.next = no_out
        

    return instances()


# -z faz complemento de dois
# ~z inverte bit a bit
@block
def inversor(z, a, y):
    z = Signal(bool(0))

    @always_comb
    def comb():
        if z == 1:
            y.next = ~a
        elif z == 0:
            y.next = a
           

    return instances()


@block
def comparador(a, zr, ng, width):
    # width insica o tamanho do vetor a
    @always_comb
    def comb():
        if a == 0:
            zr.next = 1
            ng.next = 0
        elif a < 0:
            zr.next = 0
            ng.next = 1
        else:
            zr.next = 0
            ng.next = 0
            
    return instances()


@block
def zerador(z, a, y):
    @always_comb
    def comb():
        if z:
            y.next = a
        else:
            y.next = 0
        

    return instances()


@block
def add(a, b, q):
    @always_comb
    def comb():

        q.next = a or b

    return instances()


@block
def inc(a, q):
    @always_comb
    def comb():
        q.next = add(1, a)

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

    haList[0] = halfAdder(a, b, s[0], s[1])  # 2
    haList[1] = halfAdder(c, s[0], soma, s[2])  # 3

    @always_comb
    def comb():
        carry.next = s[1] | s[2]  # 4

    return instances()


@block
def addcla4(a, b, q):
    @always_comb
    def comb():
        pass

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
