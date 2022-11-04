<<<<<<< HEAD
PREPARANDOFATORIAL:
    leaw $0, %A
    movw (%A), %D        ;D = ram[0]
    leaw $1, %A
    movw %D, (%A)         ;RAM[1] = RAM[0]
    leaw $1, %A 
    movw (%A), %D
    decw %D
                    ;RAM[2] = RAM[0] - 1
    leaw $2, %A
    movw %D, (%A)          ;ok ate aqui
WHILE2:
    ; verifica se o contador zerou , contador do fatorial   
    leaw $2, %A         ;A = 0
    movw (%A), %D       ;D = ram[2]
    leaw $ENDFATORIAL, %A       ;PREPARA O SALTO
    je                  ;D = 0? se for salta, ou SEJA, O VALOR DA RAM[2] É 0? SE FOR SALTA, SE NAO CONTINUA
    nop                 
;AQUI MULTIPLICA RAM1 POR RAM0 E GUARDA EM RAM3, TENHO QUE FAZER RAM2 X RAM1 E GUARDAR EM RAM1, INICIALMENTE EU GUARDO EM RAM5
PREPARANDO:
    leaw $5, %A         ;A = 5          
    movw $0, (%A)       ;ram[5] = 0
WHILE:
    ; verifica se o contador zerou    
    leaw $1, %A         ;A = 1
    movw (%A), %D       ;D = ram[1]
    leaw $END, %A       ;PREPARA O SALTO
    je                  ;D = 0? se for salta
    nop                 ;VERIFIQUEI SEM O VALOR NA RAM[1] É 0
    ; soma RAM[1] + RAM[3] e guarda em RAM[3]
    leaw $2, %A         ;A = 2
    movw (%A), %D       ;D = ram[2]
    leaw $5, %A         ;A = 5
    addw (%A), %D, %D   ;Somo valor ram[5] + ram[1] 
    movw %D, (%A)       ;
    ; subtrai 1 da RAM[1] --> funciona como contador
    leaw $1, %A
    movw (%A), %D
    decw %D
    movw %D, (%A)
=======
; Arquivo: matrizDeterminante.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 03/2019
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) e
;  salva seu resultado no endereço RAM[0]
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) na forma
; [ a0, a1 ]
; [ b0, b1 ]
;
; Salva o resultado no endereço RAM[0]
;
; A matriz é salva na memória da seguinte maneira:
; RAM[1000] = a0
; RAM[1001] = a1
; RAM[1003] = b0
; RAM[1004] = b1


PREPARANDO:
    leaw $2, %A
    movw $0, (%A)

WHILE:
    ; verifica se o contador zerou
    leaw $1004, %A
    movw (%A), %D
    leaw $END, %A
    je 
    nop

    ; soma RAM[1] + RAM[3] e guarda em RAM[3]

    leaw $1000, %A
    movw (%A), %D
    leaw $2, %A
    addw (%A), %D, %D
    movw %D, (%A)

    ; subtrai 1 da RAM[0] --> funciona como contador
    leaw $1004, %A
    subw (%A), $1, %D
    movw %D, (%A)

>>>>>>> 12aca06d9cc46c1e81a8d9367f349f92de0ccff6
    leaw $WHILE, %A
    jmp
    nop
END:
<<<<<<< HEAD
    leaw $5, %A      ;como havia guardado em 5, mandando de volta para 1
    movw (%A), %D
    leaw $1, %A
    movw %D, (%A)
    leaw $2, %A
    movw (%A), %D
    decw %D
    movw %D, (%A)
    leaw $WHILE2, %A
    jmp
    nop
ENDFATORIAL:
=======


PREPARANDO2:
    leaw $3, %A
    movw $0, (%A)

WHILE2:
    ; verifica se o contador zerou
    leaw $1003, %A
    movw (%A), %D
    leaw $END2, %A
    je 
    nop

    ; soma RAM[1] + RAM[3] e guarda em RAM[3]

    leaw $1001, %A
    movw (%A), %D
    leaw $3, %A
    addw (%A), %D, %D
    movw %D, (%A)

    ; subtrai 1 da RAM[0] --> funciona como contador
    leaw $1003, %A
    rsubw (%A), $1, %D
    movw %D, (%A)

    leaw $WHILE, %A
    jmp
    nop
END2:

leaw $3, %A
movw (%A), %D
notw %D
incw %D 
leaw $2, %A
addw (%A), %D, %D
                                 
leaw $0, %A
movw %D, (%A)

>>>>>>> 12aca06d9cc46c1e81a8d9367f349f92de0ccff6
