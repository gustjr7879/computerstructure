.text
.globl main

main :

    lui $v0, 0x2
    ori $v0, $v0, 0x2
    addu $v1, $a0, $v1
    bne $v1, $v0, L1
    addi $v1, $v1, -1
    lui $a0, 0x1002
    sw $v0, -8($sp)
    j L2
    addi $s0, $zero, 17