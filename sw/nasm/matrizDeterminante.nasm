; Arquivo: matrizDeterminante.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 03/2019
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) e
;  salva seu resultado no endereço RAM[0]
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) na forma
; [ a0, a1 ]
; [ b0, b1 ]
;
; Salva o resultado no endereço RAM[0]
;
; A matriz é salva na memória da seguinte maneira:
; RAM[1000] = a0
; RAM[1001] = a1
; RAM[1003] = b0
; RAM[1004] = b1


PREPARANDO:
    leaw $2, %A
    movw $0, (%A)

WHILE:
    ; verifica se o contador zerou
    leaw $1004, %A
    movw (%A), %D
    leaw $END, %A
    je 
    nop

    ; soma RAM[1] + RAM[3] e guarda em RAM[3]

    leaw $1000, %A
    movw (%A), %D
    leaw $2, %A
    addw (%A), %D, %D
    movw %D, (%A)

    ; subtrai 1 da RAM[0] --> funciona como contador
    leaw $1004, %A
    subw (%A), $1, %D
    movw %D, (%A)

    leaw $WHILE, %A
    jmp
    nop
END:


PREPARANDO2:
    leaw $3, %A
    movw $0, (%A)

WHILE2:
    ; verifica se o contador zerou
    leaw $1003, %A
    movw (%A), %D
    leaw $END2, %A
    je 
    nop

    ; soma RAM[1] + RAM[3] e guarda em RAM[3]

    leaw $1001, %A
    movw (%A), %D
    leaw $3, %A
    addw (%A), %D, %D
    movw %D, (%A)

    ; subtrai 1 da RAM[0] --> funciona como contador
    leaw $1003, %A
    rsubw (%A), $1, %D
    movw %D, (%A)

    leaw $WHILE, %A
    jmp
    nop
END2:

leaw $3, %A
movw (%A), %D
notw %D
incw %D 
leaw $2, %A
addw (%A), %D, %D
                                 
leaw $0, %A
movw %D, (%A)

