; Arquivo: Mod.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Divide o número posicionado na RAM[0] pelo número posicionado no RAM[1] e armazena a sobra na RAM[2].


; passa o valor de RAM[0] para RAM[3]
leaw $0, %A
movw (%A), %D
leaw $3, %A
movw %D, (%A)


; RAM[3] - RAM[1] ate RAM[3] <= 0

LOOP:

    ; verifica se RAM[3] <= 0
    leaw $3, %A
    movw (%A), %D
    leaw $END, %A
    jle %D
    nop

    ; subtrai RAM[1] do valor acumulado na RAM[3]
    leaw $1, %A
    movw (%A), %D
    leaw $3, %A
    subw (%A), %D, %D
    movw %D, (%A)


    leaw $LOOP, %A
    jmp nop

END:


leaw $FINAL, %A
je %D
nop

leaw $3, %A
movw (%A), %D
leaw $1, %A
addw (%A), %D , %D

FINAL:
    leaw $2, %A
    movw %D, (%A)
