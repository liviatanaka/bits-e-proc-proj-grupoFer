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
    leaw $WHILE, %A
    jmp
    nop
END:
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