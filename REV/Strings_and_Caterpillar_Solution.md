## CHALLENGE: string-cheese

### PROBLEM
```I'm something of a cheese connoisseur myself. If you can guess my favorite flavor of string cheese, I'll even give you a flag. Of course, since I'm lazy and socially inept, I slapped together a program to do the verification for me.```

### SOLUTION

See that the problem has ```strings``` in its name. Run ```strings``` on the binary. See a suspicious part that says something like "How did you know? Guess i'll give you the flag!" preceded by "blueberry". Feed blueberries to the server.

This challenge had the third most solves in the entire ctf...

**Flag: lactf{d0n7_m4k3_fun_0f_my_t4st3_1n_ch33s3}**

## CHALLENGE: caterpillar

### PROBLEM
```-~-~-~-~[]? -~-~-~-~[].```

### SOLUTION

-~-~-~-~[]! When solving this challenge, I didn't know how Javascript was turning these caterpillars into numbers and indexes, but just knew that that was what it was doing: Checking if each character of the flag at each index was equal to A Caterpillar Generated Number.

Hence, I edited around the code such that instead of ```if (char @ index == flagChar) && ... ```, it became ``` "replace char @ index to be flagChar")```

i.e. I used this code from the internet to build up a string that had all the required characters.
```
String.prototype.replaceAt = function(index, replacement) {
    return this.substring(0, index) + replacement + this.substring(index + replacement.length);
}
```

Example of a line of code: 
```
var flag = flag.replaceAt(-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~[], String.fromCharCode( -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~[]));
```

**Flag: lactf{th3_hungry_l1ttl3_c4t3rp1ll4r_at3_th3_fl4g_4g41n}**