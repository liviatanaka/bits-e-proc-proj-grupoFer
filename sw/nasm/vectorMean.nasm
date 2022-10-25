; ------------------------------------
; Calcule a média dos valores de um vetor
; que possui inicio em RAM[5] e tamanho
; defindo em RAM[4],
;
; 1. Salve a soma em RAM[1]
; 2. Salve a média em RAM[0]
; 
; ------------------------------------
; antes       | depois
;             |
; RAM[0]:     | RAM[0]:  2  : média 
; RAM[1]:     | RAM[1]:  8  : soma
; RAM[2]:     | RAM[2]:  
; RAM[3]:     | RAM[3]:  
; RAM[4]:  4  | RAM[4]:  4 
; RAM[5]:  1  | RAM[5]:  1 - 
; RAM[6]:  2  | RAM[6]:  2 | vetor
; RAM[7]:  1  | RAM[7]:  1 |
; RAM[8]:  4  | RAM[8]:  4 -
; ------------------------------------


SOMA:
    ; zera o valor de RAM[1]
    leaw $0, %A
    movw %A, %D
    leaw $1, %A
    movw %D, (%A)

    leaw $5, %A
    movw %A, %D
    leaw $2, %A ; contador
    movw %D, (%A)

    leaw $4, %A
    movw (%A), %D
    leaw $3, %A ; indices da ram
    movw %D, (%A)

    LoopSoma:

        

        ; soma 
        leaw $2, %A
        movw (%A), %D   ; D = RAM[2]
        movw %D, %A
        movw (%A), %D   ; D = RAM[RAM[2]]
        leaw $1, %A
        addw (%A), %D, %D ; D = RAM[0] + D
        movw %D, (%A)

        ; subtrai 1 do contador
        leaw $3, %A
        subw (%A), $1, %D
        movw %D, (%A)

        ; adiciona 1 do contador
        leaw $2, %A
        addw (%A), $1, %D
        movw %D, (%A)

        ; verifica se o contador zerou
        leaw $3, %A
        movw (%A), %D
        leaw $LoopDiv, %A
        je 
        nop

        leaw $LoopSoma, %A
        jmp
        nop

    LoopDiv:

        ; passa o valor de RAM[1] para RAM[3]
        leaw $1, %A
        movw (%A), %D
        leaw $3, %A
        movw %D, (%A)


        ; RAM[3] - RAM[4] ate RAM[3] <= 0

        LOOP:

            ; adiciona 1 do contador
            leaw $0, %A
            addw (%A), $1, %D
            movw %D, (%A)

            ; subtrai RAM[4] do valor acumulado na RAM[3]
            leaw $4, %A
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
            jmp 
            nop

        END: