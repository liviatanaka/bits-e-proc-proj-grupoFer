; Arquivo: Mod.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Divide o número posicionado na RAM[0] pelo número posicionado no RAM[1] e armazena a sobra na RAM[2].

LOOP:
leaw $0, %A
movw (%A), %D
leaw $1, %A
subw %D,(%A), %D
leaw $0, %A
movw %D, (%A)
leaw $LOOP, %A
jg
nop
leaw $MENOR, %A
jl
nop
leaw $2, %A
movw $0, (%A)
leaw $END, %A
jmp
nop
MENOR:
leaw $0, %A
movw (%A), %D
leaw $2, %A
movw %D, (%A)
END:
