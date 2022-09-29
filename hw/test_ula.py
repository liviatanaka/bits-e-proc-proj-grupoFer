#!/usr/bin/env python3
import random
from myhdl import block, instance, Signal, intbv, delay, bin
from .ula import *

random.seed(5)
randrange = random.randrange


def test_ula():
    x = Signal(intbv(1)[16:])
    y = Signal(intbv(2)[16:])
    saida = Signal(intbv(0)[16:])
    control = Signal(intbv(0))
    zr = Signal(bool(0))
    ng = Signal(bool(0))
    ula_1 = ula(x, y, control, zr, ng, saida)

    @instance
    def stimulus():
        control.next = 0b000010
        yield delay(10)
        assert saida == x + y

        control.next = 0b000000
        yield delay(10)
        assert saida == (x & y)

        control.next = 0b100010
        yield delay(10)
        assert saida == y

        control.next = 0b001010
        yield delay(10)
        assert saida == x

        control.next = 0b100110
        yield delay(10)
        assert saida == ~y

        control.next = 0b011010
        yield delay(10)
        assert saida == ~x

        control.next = 0b101010
        yield delay(10)
        assert saida == 0

        control.next = 0b101000
        yield delay(10)
        assert saida == 0

        control.next = 0b101001
        yield delay(10)
        assert saida == intbv(-1)[16:]

        # ------ zr ng --------#
        assert zr == 0 and ng == 1

        control.next = 0b101000
        yield delay(10)
        assert zr == 1 and ng == 0

        control.next = 0b000010
        yield delay(10)
        assert zr == 0 and ng == 0

    sim = Simulation(ula_1, stimulus)
    sim.run()


def test_zerador():
    z = Signal(bool(0))
    a = Signal(intbv(0))
    y = Signal(intbv(0))
    zerador_1 = zerador(z, a, y)

    @instance
    def stimulus():
        a.next = randrange(2**16 - 1)
        z.next = 0
        yield delay(10)
        assert y == a
        z.next = 1
        yield delay(10)
        assert y == 0

    sim = Simulation(zerador_1, stimulus)
    sim.run()


def test_comparador():
    a = Signal(intbv(0))
    ng = Signal(bool(0))
    zr = Signal(bool(0))
    comparador_1 = comparador(a, zr, ng, 16)

    @instance
    def stimulus():
        a.next = 0
        yield delay(10)
        assert ng == 0 or zr == 1
        a.next = 0xFFFF
        yield delay(10)
        assert ng == 1 or zr == 0
        a.next = 32
        yield delay(10)
        assert ng == 0 or zr == 0

    sim = Simulation(comparador_1, stimulus)
    sim.run()


def test_inversor():
    z = Signal(bool(0))
    a = Signal(intbv(0))
    y = Signal(intbv(0))

    inversor_1 = inversor(z, a, y)

    @instance
    def stimulus():
        for i in range(256):
            a.next = randrange(2**16 - 1)
            z.next = randrange(2)
            yield delay(1)
            if z == 0:
                assert a == y
            else:
                assert a == ~y

    sim = Simulation(inversor_1, stimulus)
    sim.run()


def test_inc():
    a = Signal(intbv(0))
    q = Signal(intbv(0))

    inc16_1 = inc(a, q)

    @instance
    def stimulus():
        for i in range(256):
            a.next = randrange(2**16 - 2)
            yield delay(1)
            assert q == a + 1

    sim = Simulation(inc16_1, stimulus)
    sim.run()


def test_add():
    a = Signal(intbv(0))
    b = Signal(intbv(0))
    q = Signal(intbv(0))

    add16_1 = add(a, b, q)

    @instance
    def stimulus():
        for i in range(256):
            a.next, b.next = [randrange(2**15 - 1) for i in range(2)]
            yield delay(1)
            assert q == a + b

    sim = Simulation(add16_1, stimulus)
    sim.run()

def test_xor():
    q, a, b = [Signal(intbv(0)) for i in range(3)]
    xor16_1 = xor(a, b, q)

    @instance
    def stimulus():
        for i in range(0, 4):
            a.next = randrange(2**16 - 1)
            b.next = randrange(2**16 - 1)
            yield delay(1)
            assert q.val == (a ^ b)

    sim = Simulation(xor16_1, stimulus)
    sim.run()

def test_new_ula():
    x = Signal(intbv(1)[16:])
    y = Signal(intbv(2)[16:])
    saida = Signal(intbv(0)[16:])
    control = Signal(intbv(0))
    zr = Signal(bool(0))
    ng = Signal(bool(0))

    sr = Signal(intbv(0))
    sf = Signal(intbv(0))
    m = Signal(intbv(0))
    ula_1 = ula_new(x, y, control, zr, ng, sr, sf, m, saida, width=16)
    # (x, y, c, zr, ng, sr, sf, m, saida, width=16)

    @instance
    def stimulus():
    
        control.next = 0b001010
        sf.next = 0
        sr.next= 1
        m.next = 0
        
        yield delay(10)
        assert saida == x << y

        control.next = 0b001010

        sf.next = 0b1
        sr.next= 0b0
        m.next = 0b00
        
        yield delay(10)
        assert saida == x >> y

        control.next = 0b000000

        sf.next = 0
        sr.next= 0
        m.next = 3
        
        yield delay(10)
        assert saida == x ^ y


        
    sim = Simulation(ula_1, stimulus)
    sim.run()

@block
def test_bcdAdder():
    a = Signal(intbv(0)[4:])
    b = Signal(intbv(0)[4:])
    z = Signal(intbv(0)[9:])
 
    addcla4_1 = bcdAdder(a, b,z)
 
    @instance
    def stimulus():
        a.next = 3
        b.next = 7
       
        yield delay(1)
        # assert int(bin(z, 8)[7:4:-1]) + int(bin(z, 8)[3:0:-1])*10 == int(bin(a + b, 4)[-4:])
        if a+b <9:
            assert (bin(z, 4)[-4:]) == (bin(a + b, 4)[-4:])
        else:
            assert int(z[7:4:-1])*10 + int(z[3:0:-1]) == (a + b)
 
    sim = Simulation(addcla4_1, stimulus)
    sim.run()
    return addcla4_1, stimulus


@block
def test_addcla4():
    a = Signal(intbv(0)[4:])
    b = Signal(intbv(0)[4:])
    q = Signal(intbv(0)[4:])
    carry_saida = Signal(bool(0))
    carry_entrada = Signal(bool(0))
    addcla4_1 = addcla4(a, b,carry_entrada, q, carry_saida)

    @instance
    def stimulus():
        for i in range(256):
            a.next = randrange(2**4 - 1)

            b.next = randrange(2**4 - 1)
            carry_entrada.next = 0
        
        yield delay(1)
        print("%s %s %s" % (bin(a, 4), bin(b, 4), bin(q, 4)))
        assert bin(q, 4)[-4:] == bin(a + b, 4)[-4:]

    sim = Simulation(addcla4_1, stimulus)
    sim.run()
    return addcla4_1, stimulus

@block
def test_addcla16():
    a = Signal(intbv(0)[16:])
    b = Signal(intbv(0)[16:])
    q = Signal(intbv(0)[16:])

    addcla16_1 = addcla16(a, b, q)

    @instance
    def stimulus():
        for i in range(256):
            a.next = randrange(2**16 - 1)
        
            b.next = randrange(2**16 - 1)
            
        
        yield delay(1)
        print("%s %s %s" % (bin(a, 16), bin(b, 16), bin(q, 16)))
        assert bin(q, 16)[-16:] == bin(a + b, 16)[-16:]

    sim = Simulation(addcla16_1, stimulus)
    sim.run()
    return addcla16_1, stimulus
