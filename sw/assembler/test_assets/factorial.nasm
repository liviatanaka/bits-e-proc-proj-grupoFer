; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.


constant $DOIS, 2

leaw $1, %A
movw $0, (%A) ;ter certeza que a RAM[1] começa com 0.

leaw $0, %A
movw (%A), %D
leaw $CASOZERO, %A
je %D ; conferir se a RAM[0] = 0, se for, fatorial de 0 é 1.
nop ; irá pular para o caso zero e fazer isso.

leaw $0, %A
movw (%A), %D
leaw $R5, %A ; salvando o que está em RAM[0] no contador externo.
movw %D, (%A)
leaw $DOIS, %A ; passando o que está em RAM[0] para o RAM[2] que vai ser o contador interno.
movw %D, (%A)
leaw $R5, %A ; o contador externo necessariamente já começa com um a menos.
movw (%A), %D
subw %D, $1, (%A)

WHILE:

leaw $DOIS, %A
movw (%A), %D
subw %D, $1, (%A) ;diminuindo o contador interno toda vez que passa por ele.
leaw $DOIS, %A
movw (%A), %D
leaw $END, %A ; já verificando se o contador <= 0, se for vai para o END e depois parte para o segundo loop.
jle %D
nop

leaw $0, %A
movw (%A), %D
leaw $1, %A
addw (%A), %D, %D ; RAM[1]+=RAM[0];
movw %D, (%A)

leaw $WHILE, %A
jmp
nop

WHILEE:

leaw $1, %A
movw (%A), %D
leaw $0, %A
movw %D, (%A)

leaw $WHILE, %A
jmp
nop

CASOZERO:
leaw $1, %A
movw %A, (%A)

END:

leaw $R5, %A
movw (%A), %D
decw %D
movw %D, (%A)
leaw $DOIS, %A
movw %D, (%A)

leaw $ENDD, %A
jle %D
nop

leaw $WHILEE, %A
jmp
nop

ENDD: