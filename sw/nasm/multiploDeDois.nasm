; Arquivo: multiploDeDois.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; multiplo de dois, se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.

LOOP:
leaw $5, %A
movw (%A), %D
subw %D, $2, %D
movw %D, (%A)
$LOOP, %A
jg
nop
leaw $IFZERO, %A
je
nop
leaw $0, %A
movw $0, (%A)
leaw $END, %A
jmp
nop
IFZERO:
leaw $0, %A
movw $1, (%A)
leaw $END, %A
jmp
nop
END:

