; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.


leaw $0, %A
movw (%A), %D
leaw $6, %A
movw %D, (%A)
leaw $3, %A
movw %D, (%A)

LOOP:
leaw $6, %A
movw (%A), %D
leaw $ZERO, %A
je
nop
decw %D
leaw $UM, %A
je
nop
leaw $3, %A
movw (%A), %D
leaw $0, %A
movw %D, (%A)
leaw $6, %A
movw (%A), %D
decw %D
leaw $1, %A
movw %D, (%A)
leaw $MULTIPLICA, %A
jmp
nop
QUASEUM:
leaw $6, %A
movw (%A), %D
decw %D
movw %D, (%A)
leaw $LOOP, %A
jmp
nop
ZERO:
leaw $1, %A
movw $1, (%A)
leaw $END2, %A
jmp
nop
UM:
leaw $1, %A
movw $1, (%A)
leaw $END2, %A
jmp
nop




MULTIPLICA:
leaw $3, %A
movw $0, (%A)
leaw $1, %A
movw (%A), %D
leaw $END, %A
je
nop
LOOP5:
leaw $0, %A
movw (%A), %D
leaw $3, %A
addw %D, (%A),%D
movw %D, (%A)
leaw $1, %A
movw (%A), %D
decw %D
movw %D, (%A)
leaw $LOOP5, %A
jg
nop
END:
leaw $QUASEUM, %A
jmp
nop



END2:
leaw $3, %A
movw (%A), %D
leaw $1, %A
movw %D, (%A)
leaw $IF ,%A
je
nop
leaw $END3, %A
jmp
nop

IF:
leaw $1, %A
movw %A, %D
movw %D, (%A)
END3:

