## ctfd_plus

#### TL;DR
The binary takes a 4 byte (let's call it a) "key" (probably just normal integers tbh) and does a bunch of math on it to generate a character of the flag. It then compares your input with that character, and if they are the same, it moves on to the next character until the entire flag has been checked. 

#### Decompilation
Decompiling the main function, we see that it is taking our input, running some function, and comparing each character of our input with the value returned by the function. If they are the same, the check is passed. 
Important parts of the main function: 
```C
  puts("Enter the flag:");
  fgets(local_108,0x100,stdin);
  sVar2 = strcspn(local_108,"\n");
  lVar3 = 0;
  puVar4 = &DAT_00104060;
  local_108[sVar2] = '\0';
  do {
    cVar1 = FUN_00101230(puVar4[lVar3]);
    if (cVar1 != local_108[lVar3]) {
      puts("Incorrect flag.");
      return 0;
    }
    lVar3 = lVar3 + 1;
  } while (lVar3 != 0x2f);
  puts("You got the flag! Unfortunately we don\'t exactly have a database to store the solve in...")
  ;
```

Let's take a look at the function used to generate the flag: 
```C

int FUN_00101230(uint param_1)

{
  byte bVar1;
  uint uVar2;
  int iVar3;
  
  uVar2 = 0;
  iVar3 = 0;
  do {
    bVar1 = (byte)iVar3 & 0x1f;
    iVar3 = iVar3 + 1;
    param_1 = (param_1 * param_1 >> bVar1 | param_1 * param_1 << 0x20 - bVar1) * 0x1337 + 0x4201337
              ^ uVar2;
    uVar2 = uVar2 + 0x13371337;
  } while (iVar3 != 0x20);
  return (param_1 >> 8) + (param_1 >> 0x10) + param_1 + (param_1 >> 0x18);
}
```

As you can see, it does a bunch of math on each characters. I actually found the Ghidra decompilation of the rotate right quite whacky so let's take a look at the disassembly instead: 
```asm
[0x7f3580bda9c0]> pdf @fcn.5620949b1230
            ; CALL XREF from main @ 0x5620949b1106
┌ 60: fcn.5620949b1230 (int64_t arg1);
│           ; arg int64_t arg1 @ rdi
│           0x5620949b1230      31c0           xor eax, eax
│           0x5620949b1232      31c9           xor ecx, ecx
│           0x5620949b1234      0f1f4000       nop dword [rax]
│       ┌─> 0x5620949b1238      0fafff         imul edi, edi
│       ╎   0x5620949b123b      d3cf           ror edi, cl
│       ╎   0x5620949b123d      83c101         add ecx, 1
│       ╎   0x5620949b1240      69ff37130000   imul edi, edi, 0x1337
│       ╎   0x5620949b1246      81c737132004   add edi, 0x4201337      ; arg1
│       ╎   0x5620949b124c      31c7           xor edi, eax            ; arg1
│       ╎   0x5620949b124e      0537133713     add eax, 0x13371337
│       ╎   0x5620949b1253      83f920         cmp ecx, 0x20           ; 32
│       └─< 0x5620949b1256      75e0           jne 0x5620949b1238
│           0x5620949b1258      89f8           mov eax, edi            ; arg1
│           0x5620949b125a      89fa           mov edx, edi            ; arg1
│           0x5620949b125c      c1e808         shr eax, 8
│           0x5620949b125f      c1ea10         shr edx, 0x10
│           0x5620949b1262      01d0           add eax, edx
│           0x5620949b1264      01f8           add eax, edi            ; arg1
│           0x5620949b1266      c1ef18         shr edi, 0x18           ; arg1
│           0x5620949b1269      01f8           add eax, edi            ; arg1
└           0x5620949b126b      c3             ret
```

We can now see all the mathematical operations performed. There are 2 ways to solve this challenge: 1. Dump the bytes from memory and recreate this part in python to generate the flag, or 2. Write a script using r2pipe (someone in the Discord had a really cool script for this!) to basically just run r2 commands and dump each character of the flag from the registers. 

I wrote a python script to recreate this (warning: crappy code): 
```python
INT_BITS = 32

def ror(n, d): ## rotate n by d bits
    return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF
   
def byte_proc(n):
    bla = hex(n)
    if "x" not in bla[-8:]:
        bla_want = bla[-8:]
        bla_no = int(bla_want, 16)
        return bla_no
    else:
        return n

thing = "74 92 7f 9c e9 0c bb c2 29 19 9b 40 d7 6e 3d be 04 e1 83 4f 83 d4 85 91 af 70 5d fd f1 7f c4 88 71 fa 78 e6 0d df cb 72 a7 3d b6 f4 3d 9e 29 54 f4 7b 05 aa a3 4d 14 14 3c 02 c6 e1 39 b5 b9 74 0f d8 5f 54 29 73 7a 04 3f d9 41 ad d0 bc 16 96 50 62 59 76 0f ec a7 aa 2f f2 b1 21 7e b3 80 87 15 14 8d 76 60 ad f3 56 4d 6f 84 2c 3e 57 38 15 9e 7b 95 6a 70 08 03 aa bc bf c7 27 4d 88 2e 47 71 09 34 bc 94 c0 70 95 ea 21 55 d6 be 14 84 86 8d ec f7 ff ff 65 14 aa a7 6a d1 21 0c c1 97 84 f7 d2 3a 51 ca bb 11 62 e5 c8 99 87 bd fc 37 b5 ed 29 cc 44 5d d9 8a 40 b1 02 09 2d"
thing_arr = thing.split()
chall = []
soln = []

x = 0
while x < len(thing_arr):
    result = thing_arr[x+3] + thing_arr[x+2] + thing_arr[x+1] + thing_arr[x] 
    chall.append(int(result, 16))
    x = x+4
    
for no in chall: 
    count = 0
    eax = 0
    res = no
    while count < 0x20: 
        res = res * res
        res = byte_proc(res)
        res = ror(res, count)
        res = byte_proc(res)
        count = count + 1
        res = res * 0x1337
        res = byte_proc(res)
        res = res + 0x4201337
        res = byte_proc(res)
        res = res ^ eax
        res = byte_proc(res)
        #print(hex(res))
        eax = eax + 0x13371337
        #print("---")
    res = byte_proc(res)
    #print(hex(res))
    fin = (res >> 8) + (res >> 0x10)
    fin = byte_proc(fin)
    fin = res + fin
    fin = byte_proc(fin)
    fin = fin + (res >> 0x18)
    fin = byte_proc(fin)
    whee = hex(fin)
    soln.append(chr(int(whee[-2:],16)))

print("".join(soln))
```

The flag is lactf{m4yb3_th3r3_1s_s0m3_m3r1t_t0_us1ng_4_db}.
