; Arquivo: SWeLED2.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
;
; Faça os LEDs exibirem 
; LED = SW[8] !SW[7] OFF ON ON RAM[5][3] ON SW[0] OFF
;
;                                ^            ^
;                                | TRUQUE!    | TRUQUE!
PREPARANDO:
    leaw $0, %A
    movw %A, %D
    movw %D, (%A)

    leaw $52, %A
    movw %A, %D

    leaw $21184, %A
    movw %D, (%A)

MOVENDO_SW:
    leaw $21185, %A
    movw (%A), %D
    leaw $1, %A
    andw %A, %D, %D

    leaw $SW1, %A
    je
    nop

    leaw $2, %A
    movw %A, %D
    leaw $21184, %A
    addw (%A), %D, %D
    movw %D, (%A)

    SW1:
    leaw $21185, %A
    movw (%A), %D
    leaw $128, %A
    andw %A, %D, %D

    leaw $SW2, %A
    jne
    nop

    leaw $128, %A
    movw %A, %D
    leaw $21184, %A
    addw (%A), %D, %D
    movw %D, (%A)

    SW2:
    leaw $21185, %A
    movw (%A), %D
    leaw $256, %A
    andw %A, %D, %D

    leaw $SW3, %A
    jne
    nop

    leaw $256, %A
    movw %A, %D
    leaw $21184, %A
    addw (%A), %D, %D
    movw %D, (%A)

    SW3:
    leaw $5, %A
    movw (%A), %D
    leaw $8, %A
    andw %A, %D, %D

    leaw $FINAL, %A
    je
    nop

    leaw $8, %A
    movw %A, %D
    leaw $21184, %A
    addw (%A), %D, %D
    movw %D, (%A)

    FINAL:
