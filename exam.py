import sys

a = str('0x'+input()) #16진수
a10 = int(a,16)
b = bin(a10)[2:].zfill(32) #32비트 2진수
print(b)
opcode = int(b[:6],2)
if opcode != 0:
    
    print('opcode : ',opcode)
    if opcode == 2 or 3:
        print('J format')
        rest = b[6:]
        rest10 = int(rest,2)
        rest16 = b[6:]
        print(rest16)
    else:
        print('I format')

        print('rs :',b[6:11])
        print('rt :',b[11:16])
        print('constant or address offset :',b[16:])
        print(opcode, '$',int(b[11:16],2), ',$',int(b[6:11],2),',',int(b[16:],2))
        # op $rt , $rs, constant
else:
    print('R format')
    opcode = int(b[26:],2)
    print('opcode : ',int(b[26:],2))

    print('rs :',b[6:11]) # first
    print('rt :',b[11:16]) # second
    print('rd :',b[16:21]) #destination
    print('shamt :',b[21:26])
    if opcode == 8:
        print(opcode,'$',int(b[16:21],2))
    else:

        print(int(b[26:],2), '$',int(b[16:21],2),',$',int(b[6:11],2),',$',int(b[11:16],2))
    #표현식 funct $rd, $rs ,$rt
