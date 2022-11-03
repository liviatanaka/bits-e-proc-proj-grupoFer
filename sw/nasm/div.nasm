leaw $8, %A
movw %A, %D
leaw $1, %A
movw %D, (%A) ; RAM[1] = 8

WHILE:
leaw $1, %A
movw (%A), %D
movw %D, %A
movw (%A), %D
leaw $97, %A
subw %D, %A, %D   ; D = RAM[8] - 97
leaw $IF, %A
jge
nop
leaw $1, %A
movw (%A), %D
incw %D
movw %D, (%A)
movw %D, %A
movw (%A), %D
leaw $END, %A
je
nop
leaw $WHILE, %A
jmp
nop


IF:
leaw $1, %A
movw (%A), %D
movw %D, %A
movw (%A), %D
leaw $32, %A
subw %D, %A, %D
leaw $2, %A
movw %D, (%A) ; RAM[2] = RAM[8] - 32

leaw $2, %A
movw (%A), %D
leaw $1, %A
movw (%A), %A
movw %D, (%A) ; RAM[8] = RAM[2]
leaw $1, %A
movw (%A), %D
incw %D
movw %D, (%A)
movw %D, %A
movw (%A), %D
leaw $WHILE, %A
jne
nop
END:
