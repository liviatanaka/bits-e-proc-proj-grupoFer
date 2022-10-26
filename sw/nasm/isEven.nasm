; Arquivo: isEven.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; par. Se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.
<<<<<<< HEAD
=======

>>>>>>> 12aca06d9cc46c1e81a8d9367f349f92de0ccff6
leaw $5, %A
movw (%A), %D
leaw $1, %A
andw %A, %D, %D
<<<<<<< HEAD
leaw $IF, %A
je
nop
leaw $1, %A
movw %A, %D
leaw $0, %A
movw %D, (%A)
leaw $END, %A
jmp
nop
IF:
leaw $0, %A
movw %A, %D
movw %D, (%A)
leaw $END, %A
jmp
nop
=======

leaw $ELSE, %A
je
nop

leaw $0, %A
movw $0, (%A)

leaw $END, %A
jmp 
nop

ELSE:
    leaw $0, %A
    movw $1, (%A)

>>>>>>> 12aca06d9cc46c1e81a8d9367f349f92de0ccff6
END: