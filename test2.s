.data 0x10002000

a: 
    .word 1
    .word 2
    .word 3
    .word 4
    .word 5
.text
.globl main

main: 
    la $4, a
    lw $5, 0($4)
    lw $6, 4($4)
    add $7, $5, $6
    sw $7, 8($4)