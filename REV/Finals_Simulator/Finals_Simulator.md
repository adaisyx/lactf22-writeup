## Finals Simulator 

#### TL;DR
Binary asks a bunch of questions -- enter the correct answer and you will get the flag. 

#### Decompilation 
The binary was decompiled using Ghidra: 
```C
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  int local_11c;
  char local_118 [264];
  char *local_10;
  
  puts("Welcome to Finals Simulator 2023: Math Edition!");
  printf("Question #1: What is sin(x)/n? ");
  fflush(stdout);
  fgets(local_118,0x100,stdin);
  sVar2 = strcspn(local_118,"\n");
  local_118[sVar2] = '\0';
  iVar1 = strcmp(local_118,"six");
  if (iVar1 == 0) {
    printf("Question #2: What\'s the prettiest number? ");
    fflush(stdout);
    __isoc99_scanf(&DAT_001020c3,&local_11c);
    if ((local_11c + 0x58) * 0x2a == 0x2179556a) {
      printf("Question #3: What\'s the integral of 1/cabin dcabin? ");
      fflush(stdout);
      getchar();
      fgets(local_118,0x100,stdin);
      sVar2 = strcspn(local_118,"\n");
      local_118[sVar2] = '\0';
      for (local_10 = local_118; *local_10 != '\0'; local_10 = local_10 + 1) {
        *local_10 = (char)((*local_10 * 0x11) % mod);
      }
      putchar(10);
      iVar1 = strcmp(local_118,enc);
      if (iVar1 == 0) {
        puts("Wow! A 100%! You must be really good at math! Here, have a flag as a reward.");
        print_flag();
      }
      else {
        puts("Wrong! You failed.");
      }
    }
    else {
      puts("Wrong! You failed.");
    }
  }
  else {
    puts("Wrong! You failed.");
  }
  return 0;
}
```

To answer the first question, the binary checks if the input is the string "six", and if so, proceeds to the second question. 

To answer the second question, the binary does a bunch of math. The solution, x, has to satisfy the equation (x + 0x58) * 0x2a == 0x2179556a. Doing some math, x = 13371337. 

To answer the third question, we need to do more math. The binary takes each character of your input and performs the following operations: 
1. Multiply by 0x11
2. Mod by 0xfd

The binary then compares the resultant with a byte string stored in memory that can be dumped. 

To determine the input that would give us the desired byte string, I used the following script: 
```python
enc = b"\x0e\xc9\x9d\xb8\x26\x83\x26\x41\x74\xe9\x26\xa5\x83\x94\x0e\x63\x37\x37\x37\x00"
result = {}
solution = []

for i in range(256):
        thing = i * 0x11
        thing = thing % 0xfd
        result[thing] = i

for i in enc:
        solution.append(chr(result[i]))

print("".join(solution))
```
The answer to this question is "it's a log cabin!!!". 

<img src="https://github.com/adaisyx/lactf22-writeup/blob/main/REV/Finals_Simulator/finals_sim_solve.png">
