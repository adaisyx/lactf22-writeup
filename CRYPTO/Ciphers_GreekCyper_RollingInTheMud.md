## CHALLENGE 1: rolling in the mud

### PROBLEM
```
uugh, these pigs in my pen are making a complete mess! They're rolling all over the place!

Anyway, can you decode this cipher they gave me, almost throwing it at me while rolling around?

Answer in lowercase with symbols. In the image, { and } are characters that should appear in your flag, and replace spaces with _.

``` 
<img src="https://github.com/uclaacm/lactf-archive/blob/main/2023/crypto/rolling-in-the-mud/cipher.png">


### SOLUTION
The description contains 2 keywords that tell you all you need to know: "pigs... pen" and "rolling". If the former isn't familiar, you can look up common symbol ciphers at ```https://www.dcode.fr/symbols-ciphers```.

So we know that a **pigpen cipher** is being used, and that rolling is involved. Knowing that the flag format is ```lactf{...}```, and that the image has 5 characters only at the bottom right of the code, the lactf must be there. 

(At first, I thought the flag had been written in reverse, but...) We must now **roll the image 180 degrees** to get the correct pigpen code to translate. Afterwards, I manually typed in the code on ```https://www.dcode.fr/pigpen-cipher```.

**Flag: lactf{rolling_and_rolling_and_rolling_until_the_pigs_go_home}**

&nbsp;  

## CHALLENGE 2: greek cipher 

### PROBLEM

```
You think you've seen all of the "classic" ciphers? Instead of your standard cipher, I've created my own cipher: the monoalphagreek cipher!

Answer with just the flag in lowercase with symbols left in.
```

### SOLUTION

This is a simple substitution cipher. I guessed it from the phrase ```monoalphagreek cipher```, implying a one-for-one substitution.

My personal method for solving this was to use ```https://www.dcode.fr/substitution-cipher```, enter the substitutions for "lactf" since those were part of the flag format, then assume substitutions based on common looking words ("and", "you", "that", etc. )

However, some may find this time consuming. After the ctf ended, I found a writeup that mentioned ```http://quipqiup.com/```, an automated cryptogram solver which is objectively faster. A useful resource in a crunch. 

Full decrypted text:
```
DID YOU KNOW TΗAT JULIUS CAESAR WAS NOT TΗE FIRST PERSON IN ΗISTORY SUSPECTED OF USING ENCRYPTION? ME NEITΗER. DID YOU KNOW TΗAT JULIUS CAESAR WAS PROBABLY FLUENT IN GREEK? ME NEITΗER. I LIKE ΗOW GREEK CΗARACTER LOOK TΗOUGΗ, EVEN IF I CAN'T READ TΗEM
```
**Flag: lactf{i_guess_using_many_greek_characters_didn't_stop_you._well_played_i_must_say.congrats!}**