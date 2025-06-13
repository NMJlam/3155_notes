# Algorithms involving large integers 

## Integer Multiplication 

### Naive Method $O(N^2)$
To multiply 2 `d` digit numbers we use long multiplication this is a $O(D^2)$ time algorithm. This is 
because we have to multiply each digit from $num_1$ with each digit from $num_2$. 

### Karatsuba's Algorithm $O(N^{log_2(3)})$

- This is a divide and conquer algorithm. 


Assume that we have 2 2d-bit numbers: 
- Can pad these numbers to make them even length  

$$
u = 2^d * U_1 + U_0 
$$

$$
v = 2^d * V_1 + V_0 
$$

Therefore the product of $u * v$

$$
uv = 2^{2d} U_1 V_1 + 2^d(U_0 V_1 + U_1 V_0 ) + U_0 V_0  
$$

$$ 
= 2^{2d} U_1 V_1 + 2^d(U_0 V_1 + U_1 V_0 + U_0 V_0 - U_0 V_0 + U_1 V_1 - U_1 V_1) + U_0 V_0
$$

$$ 
= 2^{2d} U_1 V_1 + 2^d(U_1 V_1 - (U_1 - U_0)(V_1 - V_0) + U_0 V_0) + U_0 V_0
$$

$$
= (2^{2d} + 2^d)U_1 V_1 - 2^d (U_1 - U_0)(V_1 - V_0) + (2^d + 1) U_0 V_0
$$

This now means that we have 3 `d`-bit multiplications: 
1) $U_1V_1$
2) $(U_1 - U_0)(V_1 - V_0)$
3) $U_0V_0$

This motivates the thinking behind karatsuba's multiplication algorithm: 
1) Keep recursively splitting the 3 `d`-bit multiplications until numbers are small enough for direct 
multiplication (`d=1`)
2) Then propogate solution back up the recursive stack by substituiting the 3 multiplications into the 
final equation. 

## Modular Exponentiation 

### Divisibility & Divisors 

#### Division Theorem  
For any integer `a` and any positive integer `n`, there exists unique integers `q` (quotient) and 
`r` (remainder) such that `a = qn + r` where $0\leq r < n$

**Quotient:** $q = \lfloor \frac{a}{n} \rfloor$

**Remainder:** $a * mod(n) = r$

**Congruence Class:** 2 integers are in the same congruence class if they have the same remainder 
$$
a \equiv b \mod (n)
$$ 

$$ 
a \mod n = b \mod n 
$$

### Modular Exponentiation $a^b mod(n)$

#### Repeated Squaring 

1) Represent `b` in binary
![binary](./binary.png)

2) Use $x * y mod(z)= (x mod(z) * y mod (z))mod(z)$ to expand expression 
![Mod](./modexpression.png)

3) Evalute using $a^{i} \mod z= (a^{i-1}mod(z) * a^{i-1}mod(z))mod(z)$
![full](./fullcomp.png)

## Primality Testing 

#### Primality 
- A natural number greater than 1 that has: 
    - No positive divisors/factors other than 1 and itself 

**Asymptotic distribution of prime numbers:** $\pi(n) \approx \frac{n}{In(n)}$
- This means that the average probability that a randomly chosen large number near `n` is prime 
is approximately $\frac{1}{\ln(n)}$

#### Trial Division 
Test everything in range `n` to see if it can divide, if can't then it should be prime.
```
def naive_test(n): 
    for k in range(2, n): 
        if (n mod(k) == 0) return "Composite"
    return "Prime"
```

Complexity $O(\sqrt n * d^2)$ why?

If a number has a factor other than 1 or itself, at least one of those factors $\leq \sqrt n$

So...
1) $O(N)$ number of divisions 
2) For an interger division we have `d` bits representing the binary length 
3) $\rightarrow O(d^2 * N)$ - division is a quadratic operation 
4) If a number has a factor other than 1 or itself, at least one of those factors $\leq \sqrt n$
5) Therefore, `N` is bound by $\sqrt n$
6) $O(\sqrt n * d^2)$

### Fermats Little Theorem 

If `p` is prime, then for any integer `a`, $a^{p} - a$ is an integer multiple of `p`

Alternatively: 
$$
a^p \equiv a \mod(p)
$$
 And, if we divide by $a$
$$
a^{p-1} \equiv 1 \mod(p)
$$

**IMPORTANT:** This is a necessary test: 
- If fails then definately composite 
- Else probably prime 
    - If passes but not technically prime $\rightarrow$ **pseudo-primes**

### Miller Rabin 

The algorithm tests a series of values to determine if an $n$ is prime. 
This property is derived based on Fermats Theorem and Roots of Unity. 

#### Derivation 

If $n$ is an odd number then an even number $n-1$ can be written as: 

$$
n-1 = 2^s * t 
$$

Then 

$$
a^{n-1} = a^{2^s * t}
$$

$$
a^{n-1} \mod n  = a^{2^s * t} \mod n 
$$

$a$ is some variable and $n$ is the prime number we are verifying. 

Try to compute $a^{n-1} \mod n$ using modular exponentiation 

$$
x_{s} = a^{2^s * t} \mod n
$$

$$
x_{s-1} = a^{2^{s-1} * t} \mod n
$$

$$
\vdots
$$

$$
x_{0}
$$

See that we can use the following property 

$$
a^{i} \mod z= (a^{i-1}mod(z) * a^{i-1}mod(z))mod(z)
$$

Then 

$$
x_{s} = (x_{s-1})^2 \mod n 
$$

Then 
>By Fermats: 

$$
x_s = a^{2^s × t} \mod n = a^{n-1} \mod n
\\
a^{n-1} \equiv 1 \mod n
$$
Hence, $x_s = 1$


>By roots of unity: 

$$
x_{s} = (x_{s-1})^2 \mod n 
$$

$$ 
 (x_{s-1})^2 \equiv x_{s}  \mod n 
$$

$$
x_s = 1 
$$ 
AND 
$$
(x_{s-1})^2 \equiv 1 \mod n 
\\
(x_{s-1}) = \pm 1
$$
Where $n$ is a prime non-even number 

#### Explanation 

For each witness $a$:

If $x_s \not\equiv 1 \pmod{n}$ → Composite (Fermat failure)

If $x_s \equiv 1 \pmod{n}$ and $x_{s-1} \not\equiv \pm 1 \pmod{n}$ → Composite (Square roots failure)

If $x_s \equiv 1 \pmod{n}$ and $x_{s-1} \equiv -1 \pmod{n}$ → Pass (continue to next witness)

If all $x_j \equiv 1 \pmod{n}$ in sequence → Pass (continue to next witness)

If all $k$ witnesses pass → Probably prime
