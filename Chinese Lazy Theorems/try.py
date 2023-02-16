#!/bin/python3

from pwn import *
import time

############################

# runs chinese remainder theorem
def crt(p, q, a1, a2):
    p = p #z2
    q = q #z1
    z = p*q
    zbig = z*2*3*5 #upper-bound for target

    a1 = a1
    a2 = a2

    y1 = pow(q, -1, p) #calculates inverse modulo (q % p = y1)
    y2 = pow(p, -1, q)

    w1 = y1*q
    w2 = y2*p

    soln = (w1*a1 + w2*a2)%z
    solnsmall = soln
    solns = []
    
    while soln < zbig: # list possible larger solutions
    	solns.append(soln)
    	soln+=z
    while solnsmall >0 and len(solns)<30: # list possible smaller solutions
    	solns.append(solnsmall)
    	solnsmall-=z
    return solns

##########################

context.log_level='debug'

proc = remote("lac.tf", 31111)

# collect values of p and q
p = proc.recvuntil(b'\n')
pint = int(bytes.decode(p))

q = proc.recvuntil(b'\n')
qint = int(bytes.decode(q))

print('p = ', pint)
print('q = ', qint)

# collect results of target modulo p and q

proc.recvuntil(b'Exit\n')
proc.sendline(b"1")
proc.recvuntil(b'here:')
proc.send(p)

a1 = int(bytes.decode(proc.recvuntil(b'\n')))

proc.recvuntil(b'Exit\n')
proc.sendline(b"1")
proc.recvuntil(b'here: ')
proc.send(q)

a2 = int(bytes.decode(proc.recvuntil(b'\n')))

# derive possible solutions for target
solns = crt(pint, qint, a1, a2)
print(len(solns))

proc.recvuntil(b'Exit\n')
proc.sendline(b"2")

# test all target solutions derived
for soln in solns:    
    proc.recvuntil(b'here: ')
    proc.sendline(str(soln).encode())
    proc.recvuntil(b'\n')


