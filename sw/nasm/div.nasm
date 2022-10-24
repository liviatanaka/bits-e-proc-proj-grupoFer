; Arquivo: Div.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Divide R0 por R1 e armazena o resultado em R2.
; (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
; divisao para numeros inteiros positivos

; passa o valor de RAM[0] para RAM[3]
leaw $0, %A
movw (%A), %D
leaw $3, %A
movw %D, (%A)



; RAM[3] - RAM[1] ate RAM[3] <= 0

LOOP:

    ; adiciona 1 do contador
    leaw $2, %A
    addw (%A), $1, %D
    movw %D, (%A)

    ; subtrai RAM[1] do valor acumulado na RAM[3]
    leaw $1, %A
    movw (%A), %D
    leaw $3, %A
    subw (%A), %D, %D

    ; verifica se o valor da subtracao eh menor ou igual a zero
    leaw $END, %A
    jle %D
    nop

    leaw $3, %A
    movw %D, (%A)

    leaw $LOOP, %A
    jmp nop

END:


leaw $FINAL, %A
je %D
nop

leaw $2, %A
subw (%A), $1, %D
movw %D, (%A)

FINAL: