#!/usr/bin/env python3

from operator import concat
from signal import Signals
from myhdl import *
# from .components import *


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
def addcla4(a, b, carry_entrada,  q, carry_saida):
    print(a[0])
    a_ = [a(i) for i in range(4)]
    b_ = [b(i) for i in range(4)]
    @always_comb
    def comb():
        k_list = [0 for i in range(4)]
        p_list = [0 for i in range(4)]
        g_list = [0 for i in range(4)]
        faList = [0 for i in range(4)]
        
        temp_carry = [0 for i in range(4)]


        for i in range(4):
            k_list[i] = int(bin((not a_[i]) and (not b_[i])))
            g_list[i] = int(bin(a_[i] and b_[i]))
            p_list[i] = int(bin(((not a_[i]) and b_[i]) or ((not b_[i]) and a_[i])))

        
        
        temp_carry[0] = int(bin(g_list[0] or (p_list[0] and carry_entrada)))
        temp_carry[1] = int(bin(
            g_list[1]
            or (p_list[1] and g_list[0])
            or (p_list[1] and p_list[0] and carry_entrada)
        ))
        
        temp_carry[2] = int(bin(
            g_list[2]
            or (p_list[2] and g_list[1])
            or (p_list[2] and p_list[1] and g_list[0])
            or (p_list[2] and p_list[1] and p_list[0] and carry_entrada)
        ))
        temp_carry[3] = int(bin(
            g_list[3]
            or (p_list[3] and g_list[2])
            or (p_list[3] and p_list[2] and g_list[1])
            or (p_list[3] and p_list[2] and p_list[1] and g_list[0])
            or (p_list[3] and p_list[2] and p_list[1] and p_list[0] and carry_entrada)
        ))
        q.next[0] = ((not p_list[0]) and (carry_entrada)) or (
                (p_list[0]) and (not carry_entrada)
            )

        for i in range(1,4):
            q.next[i] = ((not p_list[i]) and (temp_carry[i-1])) or (
                (p_list[i]) and (not temp_carry[i-1])
            )

        carry_saida.next = temp_carry[3]


    return instances()


@block
def addcla16(a, b, q):



    a_ = [a(i) for i in range(16)]
    b_ = [b(i) for i in range(16)]


    @always_comb
    def comb():
        k_list = [0 for i in range(4)]
        p_list = [0 for i in range(4)]
        g_list = [0 for i in range(4)]
        faList = [0 for i in range(16)]
        
        k_list1 = [0 for i in range(4)]
        p_list1 = [0 for i in range(4)]
        g_list1 = [0 for i in range(4)]

        k_list2 = [0 for i in range(4)]
        p_list2 = [0 for i in range(4)]
        g_list2 = [0 for i in range(4)]
        
        k_list3 = [0 for i in range(4)]
        p_list3 = [0 for i in range(4)]
        g_list3 = [0 for i in range(4)]
        temp_carry = [0 for i in range(16)]

        carry_entrada = 0
        for i in range(4):
            k_list[i] = int(bin((not a_[i]) and (not b_[i])))
            g_list[i] = int(bin(a_[i] and b_[i]))
            p_list[i] = int(bin(((not a_[i]) and b_[i]) or ((not b_[i]) and a_[i])))
            
            k_list1[i] = int(bin((not a_[i+4]) and (not b_[i+4])))
            g_list1[i] = int(bin(a_[i+4] and b_[i+4]))
            p_list1[i] = int(bin(((not a_[i+4]) and b_[i+4]) or ((not b_[i+4]) and a_[i+4])))

            k_list2[i] = int(bin((not a_[i+8]) and (not b_[i+8])))
            g_list2[i] = int(bin(a_[i+8] and b_[i+8]))
            p_list2[i] = int(bin(((not a_[i+8]) and b_[i+8]) or ((not b_[i+8]) and a_[i+8])))

            k_list3[i] = int(bin((not a_[i+12]) and (not b_[i+12])))
            g_list3[i] = int(bin(a_[i+12] and b_[i+12]))
            p_list3[i] = int(bin(((not a_[i+12]) and b_[i+12]) or ((not b_[i+12]) and a_[i+12])))




        
        temp_carry[0] = int(bin(g_list[0] or (p_list[0] and carry_entrada)))
        temp_carry[1] = int(bin(
            g_list[1]
            or (p_list[1] and g_list[0])
            or (p_list[1] and p_list[0] and carry_entrada)
        ))
        
        temp_carry[2] = int(bin(
            g_list[2]
            or (p_list[2] and g_list[1])
            or (p_list[2] and p_list[1] and g_list[0])
            or (p_list[2] and p_list[1] and p_list[0] and carry_entrada)
        ))
        temp_carry[3] = int(bin(
            g_list[3]
            or (p_list[3] and g_list[2])
            or (p_list[3] and p_list[2] and g_list[1])
            or (p_list[3] and p_list[2] and p_list[1] and g_list[0])
            or (p_list[3] and p_list[2] and p_list[1] and p_list[0] and carry_entrada)
        ))
        q.next[0] = ((not p_list[0]) and (carry_entrada)) or (
                (p_list[0]) and (not carry_entrada)
            )

        for i in range(1,4):
            q.next[i] = ((not p_list[i]) and (temp_carry[i-1])) or (
                (p_list[i]) and (not temp_carry[i-1])
            )

        carry_entrada2 = temp_carry[3]

###########################################################   somatorio 2

        temp_carry[4] = int(bin(g_list1[0] or (p_list1[0] and carry_entrada2)))
        temp_carry[5] = int(bin(
            g_list1[1]
            or (p_list1[1] and g_list1[0])
            or (p_list1[1] and p_list1[0] and carry_entrada2)
        ))
        
        temp_carry[6] = int(bin(
            g_list1[2]
            or (p_list1[2] and g_list1[1])
            or (p_list1[2] and p_list1[1] and g_list1[0])
            or (p_list1[2] and p_list1[1] and p_list1[0] and carry_entrada2)
        ))
        temp_carry[7] = int(bin(
            g_list1[3]
            or (p_list1[3] and g_list1[2])
            or (p_list1[3] and p_list1[2] and g_list1[1])
            or (p_list1[3] and p_list1[2] and p_list1[1] and g_list1[0])
            or (p_list1[3] and p_list1[2] and p_list1[1] and p_list1[0] and carry_entrada2)
        ))

        q.next[4] = ((not p_list1[0]) and (carry_entrada2)) or (
                (p_list1[0]) and (not carry_entrada2)
            )
       
        for i in range(5,8):
            q.next[i] = ((not p_list1[i-4]) and (temp_carry[i-1])) or (
                (p_list1[i-4]) and (not temp_carry[i-1])
            )

        carry_entrada3 = temp_carry[7]



        #####################################################################3 SOMATORIO 3

        temp_carry[8] = int(bin(g_list2[0] or (p_list2[0] and carry_entrada3)))
        temp_carry[9] = int(bin(
            g_list2[1]
            or (p_list2[1] and g_list2[0])
            or (p_list2[1] and p_list2[0] and carry_entrada3)
        ))
        
        temp_carry[10] = int(bin(
            g_list1[2]
            or (p_list2[2] and g_list2[1])
            or (p_list2[2] and p_list2[1] and g_list2[0])
            or (p_list2[2] and p_list2[1] and p_list2[0] and carry_entrada3)
        ))
        temp_carry[11] = int(bin(
            g_list2[3]
            or (p_list2[3] and g_list2[2])
            or (p_list2[3] and p_list2[2] and g_list2[1])
            or (p_list2[3] and p_list2[2] and p_list2[1] and g_list2[0])
            or (p_list2[3] and p_list2[2] and p_list2[1] and p_list2[0] and carry_entrada3)
        ))

        q.next[8] = ((not p_list2[0]) and (carry_entrada3)) or (
                (p_list2[0]) and (not carry_entrada3)
            )
      
        for i in range(9,12):
            q.next[i] = ((not p_list2[i-8]) and (temp_carry[i-1])) or (
                (p_list2[i-8]) and (not temp_carry[i-1])
            )

        carry_entrada4 = temp_carry[11]



################################### ultimo somador

        temp_carry[12] = int(bin(g_list3[0] or (p_list3[0] and carry_entrada4)))
        temp_carry[13] = int(bin(
            g_list2[1]
            or (p_list3[1] and g_list3[0])
            or (p_list3[1] and p_list3[0] and carry_entrada4)
        ))
        
        temp_carry[14] = int(bin(
            g_list3[2]
            or (p_list3[2] and g_list3[1])
            or (p_list3[2] and p_list3[1] and g_list3[0])
            or (p_list3[2] and p_list3[1] and p_list3[0] and carry_entrada4)
        ))
        temp_carry[15] = int(bin(
            g_list2[3]
            or (p_list3[3] and g_list3[2])
            or (p_list3[3] and p_list3[2] and g_list3[1])
            or (p_list3[3] and p_list3[2] and p_list3[1] and g_list3[0])
            or (p_list3[3] and p_list3[2] and p_list3[1] and p_list3[0] and carry_entrada4)
        ))

        q.next[12] = ((not p_list3[0]) and (carry_entrada4)) or (
                (p_list3[0]) and (not carry_entrada4)
            )
        
        for i in range(13,16):
            q.next[i] = ((not p_list3[i-12]) and (temp_carry[i-1])) or (
                (p_list3[i-12]) and (not temp_carry[i-1])
            )




    return instances()



# ----------------------------------------------
# Conceito A
# ----------------------------------------------


@block
def ula_new(x, y, c, zr, ng, sr, sf, m, saida, width=16):
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

    shifter_r = barrelShifter(x, 0, y, sr, shift_r_out)
    shifter_l = barrelShifter(shift_r_out, 1, y, sf, shift_l_out)

    # zeradores
    zerador_x = zerador(c_zx, shift_l_out, zx_out)
    zerador_y = zerador(c_zy, y, zy_out)

    # inversores
    inversor_x = inversor(c_nx, zx_out, nx_out)
    inversor_y = inversor(c_ny, zy_out, ny_out)

    # mux's
    adicao_normal = add(nx_out, ny_out, add_out)
    adicao_cla = addcla16(nx_out, ny_out, add_cla_out)
    xandy = x_and_y(nx_out, ny_out, and_out)
    x_xor_y = xor(nx_out, ny_out, xor_out)

    mux_final = mux4way(mux_final_out, add_out, add_cla_out, and_out, xor_out, m)

    # inversor final
    inversor_final = inversor(c_no, mux_final_out, no_out)

    #comparador
    comparador_ = comparador(no_out, zr, ng, width)

    
    @always_comb
    def comb():
        saida.next = no_out
    return instances()


DIG0 = tuple(i for i in range(10) for i in range(10))
DIG1 = tuple(i for i in range(10) for _ in range(10))


@block
def bcdAdder(x, y, z):
    @always_comb
    def comb():
        print(x)
        print(y)
        print(x+y)
        if x+y <9:
            z.next = x+y
        elif x+y >= 9:
            b = Signal(intbv(DIG0[int(x+y)]))
            a = Signal(intbv(DIG1[int(x+y)]))
            print(bin(a))

            z.next = concat(bin(a,4),bin(b,4))
    


    return instances()

@block
def xor(a, b, q):
    
    @always_comb
    def comb():
        
        q.next = a ^ b
    
    return instances()

