; Arquivo: SWeLED.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Faça os LEDs exibirem 
; LED = ON ON ON ON ON !SW3 !SW2 !SW1 0


leaw $0, %A
movw %A, %D
movw %D, (%A)

leaw $496, %A
movw %A, %D

leaw $21184, %A
movw %D, (%A)

leaw $21185, %A
movw (%A), %D
leaw $2, %A
andw %A, %D, %D

leaw $SW1, %A
jne
nop

leaw $2, %A
movw %A, %D
leaw $21184, %A
addw (%A), %D, %D
movw %D, (%A)

SW1:
leaw $21185, %A
movw (%A), %D
leaw $4, %A
andw %A, %D, %D

leaw $SW2, %A
jne
nop

leaw $4, %A
movw %A, %D
leaw $21184, %A
addw (%A), %D, %D
movw %D, (%A)

SW2:
leaw $21185, %A
movw (%A), %D
leaw $8, %A
andw %A, %D, %D

leaw $SW3, %A
jne
nop

leaw $8, %A
movw %A, %D
leaw $21184, %A
addw (%A), %D, %D
movw %D, (%A)

SW3: