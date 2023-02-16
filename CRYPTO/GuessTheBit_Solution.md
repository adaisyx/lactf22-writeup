### PROBLEM
```
I'm trying out for this new game show, but it doesn't seem that hard since there are only two choices? Regardless, I heard someone name Pollard could help me out with it?
``` 
https://github.com/uclaacm/lactf-archive/blob/main/2023/crypto/guess-the-bit/chall.py

### SOLUTION

Actually, I have no idea what this has to do with Pollard's theorem, despite the challenge implying it's relevant. (The official solve script does use it, using gcd and pows, but who knows how math works.)

Instead, I tried bruteforcing the solution with a lot of 50-50s (I got to 70 round cleared with 50% guesses!!) before finally figuring out all the edge cases needed to reliably get the answer. There's a lot of viable solutions if you just think about the math of how it was set up. 
&nbsp;  

So how does the challenge work? A bit is generated, either ```0 or 1```. A number from ```0-n``` (where n is really big) is then generated, ```c```. ```c``` is then squared. 
If the bit is 1, ```c``` is multiplied by ```6```. Else, ```c``` remains the same. The final ```c``` is then printed (let's call it ```final_c``` for clarity. )

Hence, we can deduce 4 scenarios:
1. If ```final_c``` > ```n**2```, ```c``` must logically have been multiplied by ```6```. The bit must be ```1```.
2. If ```final_c % 6 != 0``` (i.e. if ```final_c``` is not divisible by 6), there is no way that ```c``` was multplied by ```6```. The bit must be ```0```.
3. Ok, I had to get a little creative here. ```final_c // 6``` will give ```c**2``` if the bit was ```0```, and some random number that isn't very nice thanks to the ```6``` otherwise. We can make use of python's ```math.isqrt```, which rounds a root into an integer, to see if the square of the generated root is consistent with the actual base number. i.e. If ```math.isqrt(final_c // 6) ** 2 != final_c // 6```, the bit is ```1```.
4. If ```math.isqrt(final_c // 6) ** 2 == final_c // 6```, the bit is ```0```.

Technically, this could likely be shortened to the latter 2 scenarios, but I thought of the first 2 first and hoped that 50-50s would carry me the rest of the way. Unfortunately, I did have to use my brain more than that, but it worked out. 

Moral of the story: If you need to identify whether a number has been multiplied after squaring, you don't need pollard.

**Flag: lactf{sm4ll_pla1nt3xt_sp4ac3s_ar3n't_al4ways_e4sy}**


### ALTERNATE SOLUTIONS

I saw the official discord discussing how the factors of 2 could also have made a clear indication of whether or not the bit was 1.

This does make sense: Let us observe 4 cases again.
1. If 2<sup>n</sup> was an original factor of ```c```, and the bit is ```0```. After squaring, the new factor of 2 would be 2<sup>2n</sup>. ```2n``` must be even.
2. If 2<sup>n</sup> was an original factor of ```c```, and the bit is ```1```. After squaring and multiplying the new factor of 2 would be 2<sup>2n + 1</sup>, where ```2n + 1``` is definitely odd.
3. If 2<sup>n+1</sup> was an original factor of ```c``` (where n is even, and 1 is odd), and the bit is ```1```. After squaring and multiplying the new factor of 2 would be 2<sup>(2n + 2) + 1</sup>, where ```(2n + 2) + 1``` is definitely odd.

This is a susprisingly simple use of maths~

The official solution also uses the pollard theorem. Maybe someday we'll learn how to use it.
https://github.com/uclaacm/lactf-archive/blob/main/2023/crypto/guess-the-bit/solve.py