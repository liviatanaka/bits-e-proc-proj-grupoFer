
leaw $1, %A 
movw $0, (%A) 

leaw $0, %A
movw (%A), %D
leaw $CASOZERO, %A
je %D 
nop 

leaw $0, %A
movw (%A), %D
leaw $R5, %A 
movw %D, (%A)
leaw $2, %A 
movw %D, (%A)
leaw $R5, %A 
movw (%A), %D
subw %D, $1, (%A)

WHILE:

leaw $2, %A
movw (%A), %D
subw %D, $1, (%A) 
leaw $2, %A
movw (%A), %D
leaw $END, %A 
jle %D
nop

leaw $0, %A
movw (%A), %D
leaw $1, %A
addw (%A), %D, %D 
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
leaw $2, %A
movw %D, (%A)

leaw $ENDD, %A
jle %D
nop

leaw $WHILEE, %A
jmp
nop

ENDD:
