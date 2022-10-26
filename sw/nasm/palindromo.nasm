; Arquivo: palindromo.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se uma palavra salva na memória
; é um palíndromo ou não. Se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.
; 
; A palavra possui tamanho fixo de 5 caracteres,
; começando no endereço 10 da RAM e terminando no
; endereço 14 da RAM. A palavra é codificado em
; ASCII.

; exemplo:
;  RAM[10] = a
;  RAM[11] = r
;  RAM[12] = a
;  RAM[13] = r
;  RAM[14] = a
; 


leaw $0, %A         ;A MIRA 0
movw %A, %D       ;COLOCO 0 EM RAM[0]

movw %D, (%A)
leaw $10, %A        ;A MIRA 10
movw (%A), %D       ;JOGO VALOR DE RAM[10] PARA D
leaw $14, %A        ;A MIRA 14
subw %D, (%A), %D   ;SUBTRAIO RAM[10] DE RAM[14]
leaw $IFPRIMEIROMAIOR, %A ;PREPARA O SALTO
jne                  ; D != 0? SE FOR, SALTA
nop
leaw $11, %A         ;A MIRA 11
movw (%A), %D        ;D = RAM[11]
leaw $13, %A         ;A MIRA RAM[13]
subw %D, (%A), %D    ;FAÇO RAM[11] - RAM[13]
leaw $IFSEGUNDOMAIOR, %A
jne               ;D != 0? SE FOR, SALTA
nop
leaw $1, %A           ;A MIRA 1
movw %A, %D           ;D = 1
leaw $0, %A           ;A MIRA 0 
movw %D, (%A)         ;RAM[0] = 1
IFSEGUNDOMAIOR:
IFPRIMEIROMAIOR:

