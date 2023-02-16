## CHALLENGE 1: Chinese-lazy-theorem-1

### Problem
```
I heard about this cool theorem called the Chinese Remainder Theorem, but, uh... I'm feeling kinda tired right now.

nc lac.tf 31110
```
With the following file:


### Solution
Despite the name, there is no need for the Chinese Remainder Theorem.
The problem provides us with two variable ```p``` and ```q```, generates a hidden target ```0 <= target < p*q```. It also provides the result for ```target % input``` 
which is the modulus of the target with any given input number. Since this modulus is unbounded, we can rely on basic math:
``` a % b = a, for all values of a and b if b > a```
Thus, we enter ```input = p*q + 1``` and the code provides us with the output ``` target % input = target```.
Note here you may choose to write a script for this, but because it's very simple I just put the p and q through a large number multiplier website such as this one:
```https://www.dcode.fr/big-numbers-multiplication```

**Flag: lactf{too_lazy_to_bound_the_modulus}**


## CHALLENGE 2: Chinese-lazy-theorem-2

### Problem
```
Ok I'm a little less lazy now but you're still not getting much from me.

nc lac.tf 31111
```

### Solution
This time the modulus is bounded, as ```input <= max(p, q)```. I'm afraid we'll have to learn the Chinese Remainder Theorem after all.
Helpful Resources:
1. http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/chinese_remainder.pdf
2. https://www.youtube.com/watch?v=e8DtzQkjOMQ
3. https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html

#### Theory
```
Given 2 coprime numbers p and q, where
x = a (mod p) and y = b (mod q)
[1] x' = xy/x and y' = xy/x
[2] z1 * x' ≡ 1 (mod x) and z2 * y' ≡ 1 (mod y)
[3] w1 ≡ z1 * x' (mod pq) and w2 ≡ z2 * y' (mod pq)

x = a*w1 + b*w2 (mod pq)
```
In our case, p and q are both prime numbers, hence they're coprime. Our target is the x stated above. We can write a script to find the solution:


**Flag: lactf{n0t_$o_l@a@AzY_aNYm0Re}**

### Comments
Admittedly I don't fully understand the theory. The final result ```x = value (mod pq)``` should mean that ```x % pq = value``` so I believe 
``` x = value +/- n(pq), n is an integer``` but that didn't work so I tried the hail mary seen in the code ``` x = (value % pq) +/- n(pq)```.
I'm still not sure how this worked out but... guess it did.