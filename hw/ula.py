#!/usr/bin/env python3

from myhdl import *

@block
def mux2way(q, a, b, sel):
   """
   q: 16 bits
   a: 16 bits
   b: 16 bits
   sel: 2 bits
 
   Mux entre a e b, sel é o seletor
   """
   foo = Signal(intbv(0))
 
   @always_comb
   def comb():
       lista = [a,b]
       q.next = lista[sel]
 
   return comb

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
# -z faz complemento de dois
# ~z inverte bit a bit
@block
def inversor(z, a, y):
    # z = Signal(bool(0))

    @always_comb
    def comb():
        if z == 1:
            y.next = ~a
        else:
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
            y.next = 0
        else:
            y.next = a
        

    return instances()


@block
def add(a, b, q):

    soma = Signal(intbv(0))

    @always_comb
    def comb():
 
        print('adicao')
        print(a)
        print(int(b))
        soma = a + b
        q.next = soma
    
    print(soma)


    return instances()


@block
def inc(a, q):
    @always_comb
    def comb():
        q.next = a +1
        print('pelo visto sim')

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

        
        print(p_list, 'AAaaa P LISTTTT TEJA CERTO')
        
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



















    # faList = [0 for i in range(4)]
    # temp_carry = [0 for i in range(4)]
    # a1_ = [a(i) for i in range(3,-1,-1)]
    # a1 = ConcatSignal(*a1_)
    # a2_ = [a(i) for i in range(7,3,-1)]
    # a2 = ConcatSignal(*a2_)
    # a3_ = [a(i) for i in range(11,7,-1)]
    # a3 = ConcatSignal(*a3_)
    # a4_ = [a(i) for i in range(15,11,-1)]
    # a4 = ConcatSignal(*a4_)
    # # siggg = sig(left, right)
    # b1_ = [b(i) for i in range(3,-1,-1)]
    # b1 = ConcatSignal(*b1_)
    # b2_ = [a(i) for i in range(7,3,-1)]
    # b2 = ConcatSignal(*b2_)
    # b3_ = [b(i) for i in range(11,7,-1)]
    # b3 = ConcatSignal(*b3_)
    # b4_ = [b(i) for i in range(15,11,-1)]
    # b4 = ConcatSignal(*b4_)
    # x = [0 for i in range(4)]
    # y = [0 for i in range(4)]
    # c = [0 for i in range(4)]
    # d = [0 for i in range(4)]
    
    
    # @always_comb
    # def comb():

        
    #     faList[0] = addcla4(a1, b1,0,x,temp_carry[0])
        
    #     faList[1] = addcla4(a2, b2,temp_carry[0], y, temp_carry[1])
    #     print(x, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOXOXOXOXOXOXOXOXOXOOXOXXOXOOXXOXOXOXOXOXOXOOXXOXOXOX')

    #     faList[2] = addcla4(a3, b3,temp_carry[1], c, temp_carry[2])
    #     faList[3] = addcla4(a4, b4,temp_carry[2], d, temp_carry[3])

    #     for i in range(4):
    #         q.next[i] = x[i]
        
    #     for i in range(4,8):
    #         q.next[i] = y[i-4]

    #     for i in range(8,12):
    #         q.next[i] = c[i-8]
    #     for i in range(12,16):
    #         q.next[i] = d[i-12]

    # return instances()


# ----------------------------------------------
# Conceito A
# ----------------------------------------------


@block
def ula_new(x, y, c, zr, ng, sr, sf, bcd, saida, width=16):
    pass


@block
def bcdAdder(x, y, z):
    pass


