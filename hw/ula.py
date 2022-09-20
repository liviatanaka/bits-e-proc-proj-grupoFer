#!/usr/bin/env python3

from operator import concat
from signal import Signals
from myhdl import *
from .components import *

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

    # mux
    adicao = add(nx_out, ny_out, add_out)
    xandy = x_and_y(nx_out, ny_out, and_out)

    mux = mux2way(mux_out, and_out, add_out, c_f)

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
    

    @always_comb
    def comb():
        if z == 1:
            y.next = ~a
        else:
            y.next = a
           

    return instances()


@block
def comparador(a, zr, ng, width=16):
    # width insica o tamanho do vetor a
    
    @always_comb
    def comb():
        if a == 0:
            zr.next = 1
            ng.next = 0
        elif a > 32767:
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
            y.next = 0
        else:
            y.next = a


    return instances()


@block
def add(a, b, q, width=16):
    #soma = Signal(intbv(0))
    soma = Signal(intbv(0)[width:])

    @always_comb
    def comb():
        soma = a + b
        if soma > 65535:
            q.next = 65535
        else:
            q.next = soma
    


    return instances()


@block
def inc(a, q):
    
    @always_comb
    def comb():
        q.next = a + 1
    return instances()


@block
def x_and_y(a, b, q):
    @always_comb
    def comb():
        q.next = a & b

    return instances()

# ----------------------------------------------
# Conceito B
# ----------------------------------------------


@block
def halfAdder(a, b, soma, carry):
    s = Signal(bool(0))
    c = Signal(bool(0))

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
def ula_new(x, y, c, zr, ng, sr, sf, m, bcd, saida, width=16):
    zx_out = Signal(intbv(0)[width:])
    nx_out = Signal(intbv(0)[width:])
    zy_out = Signal(intbv(0)[width:])
    ny_out = Signal(intbv(0)[width:])
    and_out = Signal(intbv(0)[width:])
    add_out = Signal(intbv(0)[width:])
    mux_out = Signal(intbv(0)[width:])
    no_out = Signal(intbv(0)[width:])

    # novos
    shift_r_out = Signal(intbv(0)[width:])
    shift_l_out = Signal(intbv(0)[width:])
    add_cla_out = Signal(intbv(0)[width:])
    xor_out = Signal(intbv(0)[width:])
    mux2_out = Signal(intbv(0)[width:])
    mux_final_out = Signal(intbv(0)[width:])


    c_zx = c(5)
    c_nx = c(4)
    c_zy = c(3)
    c_ny = c(2)
    c_f = c(1)
    c_no = c(0)

    # shifta
    if sr == 1:
        shifter_r = barrelShifter(x, 0, y, shift_r_out)
    
    if sf == 1:
        shifter_l = barrelShifter(shift_r_out, 1, y, shift_l_out)
    

    # zeradores
    zerador_x = zerador(c_zx, shift_l_out, zx_out)
    zerador_y = zerador(c_zy, y,zy_out)

    # inversores
    inversor_x = inversor(c_nx, zx_out, nx_out)
    inversor_y = inversor(c_ny, zy_out, ny_out)

    # mux's

    adicao_normal = add(nx_out, ny_out, add_out)
    adicao_cla = addcla16(nx_out, ny_out, add_cla_out)
    
    xandy = x_and_y(nx_out, ny_out, and_out)
    x_xor_y = xor(nx_out, ny_out, xor_out)

    mux1 = mux2way(mux_out, and_out, add_out, c_f)
    mux2 = mux2way(mux2_out, xor_out, add_cla_out, c_f)

    mux_final = mux2way(mux_final_out, mux_out, mux_out, m)

    # inversor final
    inversor_final = inversor(c_no, mux_final_out, no_out)

    #comparador
    comparador_ = comparador(no_out, zr, ng, width)

    
    @always_comb
    def comb():
        saida.next = no_out

    return instances()

@block
def xor(a, b, q):
    
    @always_comb
    def comb():
        q.next = a ^ b
    
    return instances()









