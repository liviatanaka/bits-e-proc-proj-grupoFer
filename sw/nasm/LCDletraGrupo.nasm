; Arquivo: LCDletraGrupo.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Escreva no LCD a letra do grupo de vocês
;  - Valide no hardawre
;  - Bata uma foto!




leaw $17394, %A
movw $-1, (%A)
leaw $17395, %A
movw $-1, (%A)

leaw $17714, %A
movw $-1, (%A)
leaw $17715, %A
movw $-1, (%A)

leaw $17394, %A
movw $1, (%A)
leaw $17414, %A
movw $1, (%A)
leaw $17434, %A
movw $1, (%A)
leaw $17454, %A
movw $1, (%A)
leaw $17474, %A
movw $1, (%A)
leaw $17494, %A
movw $1, (%A)
leaw $17514, %A
movw $1, (%A)
leaw $17534, %A
movw $1, (%A)
leaw $17554, %A
movw $1, (%A)
leaw $17574, %A
movw $1, (%A)
leaw $17594, %A
movw $1, (%A)
leaw $17614, %A
movw $1, (%A)
leaw $17634, %A
movw $1, (%A)
leaw $17654, %A
movw $1, (%A)
leaw $17674, %A
movw $1, (%A)
leaw $17694, %A
movw $1, (%A)
leaw $17714, %A
movw $1, (%A)
leaw $17734, %A
movw $1, (%A)
leaw $17754, %A
movw $1, (%A)
leaw $17774, %A
movw $1, (%A)
leaw $17794, %A
movw $1, (%A)
leaw $17814, %A
movw $1, (%A)
leaw $17834, %A
movw $1, (%A)
leaw $17854, %A
movw $1, (%A)
leaw $17874, %A
movw $1, (%A)
leaw $17894, %A
movw $1, (%A)
leaw $17914, %A
movw $1, (%A)
leaw $17934, %A
movw $1, (%A)
leaw $17954, %A
movw $1, (%A)
leaw $17974, %A
movw $1, (%A)
leaw $17994, %A
movw $1, (%A)
leaw $18014, %A
movw $1, (%A)