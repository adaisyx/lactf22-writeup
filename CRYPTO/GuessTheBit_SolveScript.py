from pwn import *
import math

proc = remote("lac.tf", 31190)

#actually can just set n from source code but was getting used to recvuntil
n = int(proc.recvuntil(b"a =")[5:-4])
print(n)
n_sq = n ** 2
a = 6

for i in range(150):
    print("COUNT:", i)
    proc.recvuntil(b"c =  ")
    #receive and format c from server
    c = proc.recvline()
    c = int(bytes.decode(c))
    print(c)

    if c > n_sq:
        #bit is definitely 1 since c**2*6 > n**2
        proc.sendline(b"1")
    else:
        if c % 6 == 0 and c > 6:
            # smaller than n**2 and divisible by 6 has 2 cases 
            # c is either number ** 2 * 6 or just number ** 2 
            checking = c // 6
            #isqrt returns an integer from rooting a number.
            int_sqrt = math.isqrt(checking)

            if int_sqrt ** 2 != checking:
                #if squared isqrt is equal to original, 
                # number is an integer
                print("bit 0 maybe")
                proc.sendline(b"0")
                
            else:
                #if squared isqrt is not equal to original, 
                # number is not an integer
                # hence was probably * 6
                print("bit 1 maybe")
                proc.sendline(b"1")
                
        # if not divisible by 6, bit is definitely 0   
        else:
            proc.sendline(b"0")
 

print(proc.recvline())
print(proc.recvline())
print(proc.recvline())