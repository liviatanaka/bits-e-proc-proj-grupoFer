; Arquivo: Abs.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Multiplica o valor de RAM[1] com RAM[0] salvando em RAM[3]
; Assuma valores inteiros

PREPARANDO:
    leaw $3, %A
    movw $0, (%A)

WHILE:

    ; verifica se o contador zerou
    leaw $0, %A
    movw (%A), %D
    leaw $END, %A
    je 
    nop

    ; soma RAM[1] + RAM[3] e guarda em RAM[3]

    leaw $1, %A
    movw (%A), %D
    leaw $3, %A
    addw (%A), %D, %D
    movw %D, (%A)

    leaw $0, %A
    subw (%A), $1, %D
    movw %D, (%A)

    leaw $WHILE, %A
    jmp
    nop

END:
