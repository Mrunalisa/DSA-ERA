# Logic Building: All Questions with Definition, Example, Logic, Code and Output

> Language: Python. Every output below was produced by actually running the code.

> Method for every problem: **Understand → Example on paper → Logic → Code → Dry run → Edge cases**.

> Part K (Stack, Queue, Linked List, Greedy, DP, Trees, Graphs) belongs to DSA, which is your next stage.

## Contents
- PART A: Basic Programming Logic
- PART B: Number-Based Problems
- PART C: String Problems
- PART D: Array Problems (Basic)
- PART E: Array Problems (Medium)
- PART F: Array Problems (Advanced)
- PART G: 2D Array / Matrix Problems
- PART H: Searching and Sorting
- PART I: Recursion Problems
- PART J: Bit Manipulation, Maths and Puzzles

Total problems: **170**


---

# PART A: Basic Programming Logic


## 1. Swap Two Numbers

**Definition:** Exchange the values stored in two variables.

**Example:** a = 5, b = 10  →  a = 10, b = 5

**Logic:** Use a temporary variable, or arithmetic (+ and -), or Python tuple swap.

```python
a, b = 5, 10
temp = a; a = b; b = temp
print("With temp   :", a, b)
a, b = 5, 10
a = a + b; b = a - b; a = a - b
print("Without temp:", a, b)
```

**Output:**
```
With temp   : 10 5
Without temp: 10 5
```


## 2. Check Even or Odd

**Definition:** Even number is divisible by 2 (remainder 0). Odd number leaves remainder 1.

**Example:** 8 → Even, 7 → Odd

**Logic:** Use the modulus operator `n % 2`.

```python
for n in (8, 7):
    print(n, "Even" if n % 2 == 0 else "Odd")
```

**Output:**
```
8 Even
7 Odd
```


## 3. Largest of Three Numbers

**Definition:** Find the biggest among three given numbers.

**Example:** 12, 45, 30 → 45

**Logic:** Compare a with b and c, otherwise compare b with c.

```python
a, b, c = 12, 45, 30
if a >= b and a >= c: print(a)
elif b >= c: print(b)
else: print(c)
```

**Output:**
```
45
```


## 4. Leap Year Check

**Definition:** A year is a leap year if divisible by 4 but not by 100, or divisible by 400.

**Example:** 2024 → Leap, 1900 → Not Leap, 2000 → Leap

**Logic:** `(y % 4 == 0 and y % 100 != 0) or y % 400 == 0`

```python
for y in (2024, 1900, 2000, 2023):
    leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    print(y, "Leap" if leap else "Not Leap")
```

**Output:**
```
2024 Leap
1900 Not Leap
2000 Leap
2023 Not Leap
```


## 5. Sum of First N Natural Numbers

**Definition:** Natural numbers are 1, 2, 3, ... Add them up to N.

**Example:** N = 10 → 55

**Logic:** Loop and add, or use formula `n*(n+1)/2`.

```python
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(total, n * (n + 1) // 2)
```

**Output:**
```
55 55
```


## 6. Factorial of a Number

**Definition:** n! is the product of all integers from 1 to n. 0! = 1.

**Example:** 5! = 5 x 4 x 3 x 2 x 1 = 120

**Logic:** Start with result = 1 and multiply by each number up to n.

```python
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! =", fact)
```

**Output:**
```
5! = 120
```


## 7. Multiplication Table

**Definition:** Print n x 1 to n x 10.

**Example:** n = 7 → 7 x 1 = 7 ... 7 x 10 = 70

**Logic:** One loop from 1 to 10.

```python
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**Output:**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```


## 8. Positive, Negative or Zero

**Definition:** Classify a number by its sign.

**Example:** -5 → Negative, 0 → Zero, 8 → Positive

**Logic:** if / elif / else.

```python
for n in (-5, 0, 8):
    print(n, "Positive" if n > 0 else "Negative" if n < 0 else "Zero")
```

**Output:**
```
-5 Negative
0 Zero
8 Positive
```


## 9. Simple and Compound Interest

**Definition:** SI = P x R x T / 100. CI = P x (1 + R/100)^T - P.

**Example:** P = 1000, R = 5, T = 2 → SI = 100, CI = 102.5

**Logic:** Apply the formulas directly.

```python
P, R, T = 1000, 5, 2
print("SI:", P * R * T / 100)
print("CI:", round(P * (1 + R / 100) ** T - P, 2))
```

**Output:**
```
SI: 100.0
CI: 102.5
```


## 10. Calculator using Switch-Case

**Definition:** Perform + - * / % based on an operator character.

**Example:** 10 and 5 with `*` → 50

**Logic:** if/elif chain (or `match` in Python 3.10+), handle divide-by-zero.

```python
a, b = 10, 5
for op in "+-*/%":
    if op == "+": r = a + b
    elif op == "-": r = a - b
    elif op == "*": r = a * b
    elif op == "/": r = a / b if b else "Error"
    else: r = a % b
    print(a, op, b, "=", r)
```

**Output:**
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 % 5 = 0
```


---

# PART B: Number-Based Problems


## 11. Reverse a Number

**Definition:** Write the digits in opposite order.

**Example:** 1234 → 4321

**Logic:** Take last digit with `%10`, build `rev = rev*10 + digit`, drop last digit with `//10`.

```python
n, rev = 1234, 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
```

**Output:**
```
4321
```


## 12. Palindrome Number

**Definition:** A number that reads the same forwards and backwards.

**Example:** 121 → Palindrome, 123 → Not

**Logic:** Reverse the number and compare with the original.

```python
for n in (121, 123, 1331):
    t, rev = n, 0
    while t > 0:
        rev = rev * 10 + t % 10
        t //= 10
    print(n, "Palindrome" if rev == n else "Not Palindrome")
```

**Output:**
```
121 Palindrome
123 Not Palindrome
1331 Palindrome
```


## 13. Count Digits

**Definition:** How many digits a number has.

**Example:** 98765 → 5

**Logic:** Divide by 10 until the number becomes 0 and count the steps.

```python
n, count = 98765, 0
while n > 0:
    count += 1
    n //= 10
print(count)
```

**Output:**
```
5
```


## 14. Sum of Digits

**Definition:** Add all digits of a number.

**Example:** 1234 → 1+2+3+4 = 10

**Logic:** Add `n % 10`, then `n //= 10`.

```python
n, s = 1234, 0
while n > 0:
    s += n % 10
    n //= 10
print(s)
```

**Output:**
```
10
```


## 15. Armstrong Number (single and range)

**Definition:** A number equal to the sum of its digits each raised to the power of the digit count.

**Example:** 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

**Logic:** Count digits p, sum `d**p`, compare with the number.

```python
def armstrong(n):
    p = len(str(n))
    return n == sum(int(d) ** p for d in str(n))
print(armstrong(153), armstrong(123))
print([x for x in range(100, 1000) if armstrong(x)])
```

**Output:**
```
True False
[153, 370, 371, 407]
```


## 16. Prime Number Check

**Definition:** A number greater than 1 with exactly two factors: 1 and itself.

**Example:** 7 → Prime (only 1, 7). 12 → Not prime (1,2,3,4,6,12). 1 is NOT prime.

**Logic:** Try dividing by 2 up to √n. If any divides, not prime.

```python
def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
for n in (1, 2, 7, 12, 29, 97):
    print(n, "Prime" if is_prime(n) else "Not Prime")
```

**Output:**
```
1 Not Prime
2 Prime
7 Prime
12 Not Prime
29 Prime
97 Prime
```


## 17. Prime Numbers in a Range

**Definition:** Print every prime between two numbers.

**Example:** 1 to 50 → 2 3 5 7 11 ...

**Logic:** Run the prime check for every number in the range.

```python
def is_prime(n):
    if n < 2: return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))
print([n for n in range(1, 51) if is_prime(n)])
```

**Output:**
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```


## 18. Perfect Number

**Definition:** A number equal to the sum of its proper divisors (all divisors except itself).

**Example:** 28 = 1 + 2 + 4 + 7 + 14

**Logic:** Add every `i` from 1 to n/2 that divides n.

```python
for n in (6, 28, 12, 496):
    s = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    print(n, "Perfect" if s == n else "Not Perfect")
```

**Output:**
```
6 Perfect
28 Perfect
12 Not Perfect
496 Perfect
```


## 19. Strong Number

**Definition:** Sum of factorials of digits equals the number.

**Example:** 145 = 1! + 4! + 5! = 1 + 24 + 120

**Logic:** Factorial of each digit, then add.

```python
from math import factorial
for n in (145, 123, 40585):
    s = sum(factorial(int(d)) for d in str(n))
    print(n, "Strong" if s == n else "Not Strong")
```

**Output:**
```
145 Strong
123 Not Strong
40585 Strong
```


## 20. Krishnamurthy Number

**Definition:** Another name for the Strong number (sum of digit factorials equals the number).

**Example:** 1, 2, 145, 40585 are Krishnamurthy numbers

**Logic:** Same as Strong number.

```python
from math import factorial
print([n for n in range(1, 50000) if sum(factorial(int(d)) for d in str(n)) == n])
```

**Output:**
```
[1, 2, 145, 40585]
```


## 21. Automorphic Number

**Definition:** A number whose square ends with the number itself.

**Example:** 25² = 625 (ends in 25), 76² = 5776

**Logic:** Check `str(n*n).endswith(str(n))`.

```python
for n in (5, 6, 25, 76, 12):
    print(n, "Automorphic" if str(n * n).endswith(str(n)) else "Not")
```

**Output:**
```
5 Automorphic
6 Automorphic
25 Automorphic
76 Automorphic
12 Not
```


## 22. Neon Number

**Definition:** A number whose digit sum of its square equals the number.

**Example:** 9² = 81 → 8 + 1 = 9

**Logic:** Square it, add its digits, compare.

```python
for n in (0, 1, 9, 8):
    print(n, "Neon" if sum(int(d) for d in str(n * n)) == n else "Not")
```

**Output:**
```
0 Neon
1 Neon
9 Neon
8 Not
```


## 23. Harshad (Niven) Number

**Definition:** A number divisible by the sum of its own digits.

**Example:** 18 → digit sum 9, 18 % 9 = 0 ✔

**Logic:** `n % digit_sum == 0`

```python
for n in (18, 21, 19, 156):
    s = sum(int(d) for d in str(n))
    print(n, "Harshad" if n % s == 0 else "Not")
```

**Output:**
```
18 Harshad
21 Harshad
19 Not
156 Harshad
```


## 24. Happy Number

**Definition:** Repeatedly replace the number by the sum of squares of its digits; if it reaches 1 it is happy, else it loops forever.

**Example:** 19 → 82 → 68 → 100 → 1 (Happy)

**Logic:** Keep a set of seen numbers to detect a cycle.

```python
def happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
for n in (19, 7, 4, 20):
    print(n, "Happy" if happy(n) else "Not Happy")
```

**Output:**
```
19 Happy
7 Happy
4 Not Happy
20 Not Happy
```


## 25. Magic Number

**Definition:** Keep adding the digits until a single digit remains; if it is 1, the number is magic.

**Example:** 19 → 10 → 1 (Magic)

**Logic:** Loop until `n < 10`.

```python
def magic(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n == 1
for n in (19, 1234, 55):
    print(n, "Magic" if magic(n) else "Not Magic")
```

**Output:**
```
19 Magic
1234 Magic
55 Magic
```


## 26. Spy Number

**Definition:** Sum of digits equals product of digits.

**Example:** 1124 → sum 8, product 8 ✔

**Logic:** Compute both and compare.

```python
from math import prod
for n in (1124, 123, 22):
    d = [int(x) for x in str(n)]
    print(n, "Spy" if sum(d) == prod(d) else "Not Spy")
```

**Output:**
```
1124 Spy
123 Spy
22 Spy
```


## 27. Disarium Number

**Definition:** Sum of each digit raised to its position equals the number.

**Example:** 175 = 1¹ + 7² + 5³ = 1 + 49 + 125

**Logic:** Use `enumerate` starting from position 1.

```python
for n in (175, 89, 135, 12):
    s = sum(int(d) ** i for i, d in enumerate(str(n), 1))
    print(n, "Disarium" if s == n else "Not")
```

**Output:**
```
175 Disarium
89 Disarium
135 Disarium
12 Not
```


## 28. Duck Number

**Definition:** A number that contains the digit 0 but does not start with 0.

**Example:** 3210 → Duck, 0123 is not valid, 1234 → not duck

**Logic:** Check `'0' in str(n)`.

```python
for n in (3210, 1234, 7007):
    print(n, "Duck" if "0" in str(n) else "Not Duck")
```

**Output:**
```
3210 Duck
1234 Not Duck
7007 Duck
```


## 29. Buzz Number

**Definition:** A number that ends with 7 or is divisible by 7.

**Example:** 63 (divisible), 17 (ends with 7), 20 (not buzz)

**Logic:** `n % 10 == 7 or n % 7 == 0`

```python
for n in (63, 17, 20):
    print(n, "Buzz" if n % 10 == 7 or n % 7 == 0 else "Not Buzz")
```

**Output:**
```
63 Buzz
17 Buzz
20 Not Buzz
```


## 30. GCD (HCF) and LCM

**Definition:** GCD = largest number dividing both. LCM = smallest number divisible by both.

**Example:** 12 and 18 → GCD 6, LCM 36

**Logic:** Euclid: `gcd(a, b) = gcd(b, a % b)`. LCM = a x b / GCD.

```python
a, b = 12, 18
x, y = a, b
while y:
    x, y = y, x % y
print("GCD:", x, "LCM:", a * b // x)
```

**Output:**
```
GCD: 6 LCM: 36
```


## 31. Prime Factorization

**Definition:** Break a number into a product of primes.

**Example:** 360 = 2³ x 3² x 5

**Logic:** Divide by 2, then 3, ... while divisible; count each divisor.

```python
n, i, parts = 360, 2, []
while i * i <= n:
    c = 0
    while n % i == 0:
        n //= i; c += 1
    if c: parts.append(f"{i}^{c}")
    i += 1
if n > 1: parts.append(f"{n}^1")
print(" x ".join(parts))
```

**Output:**
```
2^3 x 3^2 x 5^1
```


## 32. Fibonacci Series (loop)

**Definition:** Each term is the sum of the previous two, starting 0, 1.

**Example:** First 10 → 0 1 1 2 3 5 8 13 21 34

**Logic:** Keep two variables a, b and move them forward.

```python
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
```

**Output:**
```
0 1 1 2 3 5 8 13 21 34
```


## 33. Fibonacci Series (recursion)

**Definition:** Same series using `fib(n) = fib(n-1) + fib(n-2)`.

**Example:** fib(7) → 13

**Logic:** Base cases fib(0)=0, fib(1)=1. (Slow for big n, see memoization later.)

```python
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)
print([fib(i) for i in range(10)])
```

**Output:**
```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```


## 34. Check if a Number is Fibonacci

**Definition:** A number is Fibonacci if `5n²+4` or `5n²-4` is a perfect square.

**Example:** 21 → Yes, 22 → No

**Logic:** Use the math test, no loop needed.

```python
from math import isqrt
def sq(x): return isqrt(x) ** 2 == x
for n in (21, 22, 55, 10):
    print(n, "Fibonacci" if sq(5*n*n + 4) or sq(5*n*n - 4) else "Not")
```

**Output:**
```
21 Fibonacci
22 Not
55 Fibonacci
10 Not
```


## 35. Power of a Number (without pow)

**Definition:** Compute base^exp using only loops / multiplication.

**Example:** 2^10 → 1024

**Logic:** Fast exponentiation: square the base, halve the exponent.

```python
def power(b, e):
    res = 1
    while e > 0:
        if e & 1: res *= b
        b *= b
        e >>= 1
    return res
print(power(2, 10), power(3, 5))
```

**Output:**
```
1024 243
```


## 36. Number to Words

**Definition:** Convert digits into English words.

**Example:** 12345 → twelve thousand three hundred forty five

**Logic:** Split into thousands, hundreds, tens, ones and recurse.

```python
ones = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def w(n):
    if n < 20: return ones[n]
    if n < 100: return tens[n // 10] + (" " + ones[n % 10] if n % 10 else "")
    if n < 1000: return ones[n // 100] + " hundred" + (" " + w(n % 100) if n % 100 else "")
    return w(n // 1000) + " thousand" + (" " + w(n % 1000) if n % 1000 else "")
for n in (7, 42, 305, 12345):
    print(n, "→", w(n))
```

**Output:**
```
7 → seven
42 → forty two
305 → three hundred five
12345 → twelve thousand three hundred forty five
```


## 37. Decimal ↔ Binary / Octal / Hexadecimal

**Definition:** Convert between number systems (base 2, 8, 16).

**Example:** 156 → binary 10011100, octal 234, hex 9C

**Logic:** Divide repeatedly by base and collect remainders in reverse. To go back, multiply by base and add digit.

```python
def to_base(n, b):
    d = "0123456789ABCDEF"; res = ""
    while n > 0:
        res = d[n % b] + res
        n //= b
    return res or "0"
n = 156
print(to_base(n, 2), to_base(n, 8), to_base(n, 16))
val = 0
for ch in "10011100": val = val * 2 + int(ch)
print("binary back to decimal:", val)
```

**Output:**
```
10011100 234 9C
binary back to decimal: 156
```


## 38. Roman Numerals (both directions)

**Definition:** Roman symbols: I=1 V=5 X=10 L=50 C=100 D=500 M=1000. Smaller before larger means subtract.

**Example:** 1994 → MCMXCIV

**Logic:** Greedy table for int→roman. For roman→int, subtract if next symbol is bigger.

```python
def to_roman(n):
    vals = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    res = ""
    for v, s in vals:
        while n >= v: res += s; n -= v
    return res
def from_roman(s):
    m = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000); t = 0
    for i, ch in enumerate(s):
        t += -m[ch] if i + 1 < len(s) and m[ch] < m[s[i+1]] else m[ch]
    return t
print(to_roman(1994), from_roman("MCMXCIV"))
```

**Output:**
```
MCMXCIV 1994
```


## 39. Perfect Square / Perfect Cube

**Definition:** Perfect square = k x k. Perfect cube = k x k x k.

**Example:** 64 is both (8², 4³), 27 is a cube, 50 is neither

**Logic:** Take integer root and verify by multiplying back.

```python
from math import isqrt
for n in (64, 27, 50):
    sq = isqrt(n) ** 2 == n
    c = round(n ** (1 / 3))
    print(n, "square" if sq else "-", "cube" if c ** 3 == n else "-")
```

**Output:**
```
64 square cube
27 - cube
50 - -
```


## 40. Trailing Zeros in Factorial

**Definition:** Count zeros at the end of n!.

**Example:** 100! has 24 trailing zeros

**Logic:** Each zero needs a factor 5 (2s are plenty): `n//5 + n//25 + n//125 ...`

```python
n, count, p = 100, 0, 5
while p <= n:
    count += n // p
    p *= 5
print(count)
```

**Output:**
```
24
```


## 41. Sieve of Eratosthenes

**Definition:** Fast way to list all primes up to N by crossing out multiples.

**Example:** N = 50 → 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

**Logic:** Assume all prime, for each prime p cross out p², p²+p, ...

```python
N = 50
prime = [True] * (N + 1)
prime[0] = prime[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = False
print([i for i in range(N + 1) if prime[i]])
```

**Output:**
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```


## 42. Print All Factors of a Number

**Definition:** Factors are numbers that divide n completely.

**Example:** 36 → 1 2 3 4 6 9 12 18 36

**Logic:** Loop to √n and add both `i` and `n/i`.

```python
n = 36
f = set()
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0: f.update((i, n // i))
print(sorted(f))
```

**Output:**
```
[1, 2, 3, 4, 6, 9, 12, 18, 36]
```


## 43. Twin Primes and Prime Pairs

**Definition:** Twin primes are primes that differ by 2.

**Example:** (3,5), (5,7), (11,13), (17,19)

**Logic:** Check `is_prime(p)` and `is_prime(p+2)`.

```python
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
print([(p, p + 2) for p in range(2, 60) if is_prime(p) and is_prime(p + 2)])
```

**Output:**
```
[(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61)]
```


---

# PART C: String Problems


## 44. Reverse a String

**Definition:** Write the characters in opposite order.

**Example:** hello → olleh

**Logic:** Slice with step -1, or loop from the end.

```python
s = "hello"
print(s[::-1])
r = ""
for ch in s: r = ch + r
print(r)
```

**Output:**
```
olleh
olleh
```


## 45. Palindrome String

**Definition:** A string that reads the same both ways.

**Example:** madam → Yes, hello → No

**Logic:** Compare string with its reverse (or two pointers from both ends).

```python
for s in ("madam", "hello", "racecar"):
    l, r, ok = 0, len(s) - 1, True
    while l < r:
        if s[l] != s[r]: ok = False; break
        l += 1; r -= 1
    print(s, "Palindrome" if ok else "Not")
```

**Output:**
```
madam Palindrome
hello Not
racecar Palindrome
```


## 46. Count Vowels and Consonants

**Definition:** Vowels are a e i o u; other letters are consonants.

**Example:** Programming → vowels 3, consonants 8

**Logic:** Loop over letters, check membership in "aeiou".

```python
s = "Programming"
v = sum(ch in "aeiou" for ch in s.lower())
c = sum(ch.isalpha() for ch in s) - v
print("Vowels:", v, "Consonants:", c)
```

**Output:**
```
Vowels: 3 Consonants: 8
```


## 47. Count Words in a Sentence

**Definition:** Words are groups of characters separated by spaces.

**Example:** "I love coding in Python" → 5

**Logic:** `split()` handles multiple spaces.

```python
print(len("I  love coding in Python".split()))
```

**Output:**
```
5
```


## 48. Character Frequency Count

**Definition:** Count how many times each character appears.

**Example:** banana → b:1 a:3 n:2

**Logic:** Use a dictionary; add 1 for every character.

```python
s = "banana"
freq = {}
for ch in s: freq[ch] = freq.get(ch, 0) + 1
print(freq)
```

**Output:**
```
{'b': 1, 'a': 3, 'n': 2}
```


## 49. First Non-Repeating Character

**Definition:** The first character in the string that appears exactly once.

**Example:** swiss → w

**Logic:** Count first, then scan again for count == 1.

```python
from collections import Counter
for s in ("swiss", "aabb"):
    c = Counter(s)
    print(s, next((ch for ch in s if c[ch] == 1), None))
```

**Output:**
```
swiss w
aabb None
```


## 50. First Repeating Character

**Definition:** The first character whose repeat is seen earliest while scanning.

**Example:** programming → r

**Logic:** Keep a set of seen characters; the first one already in set is the answer.

```python
s, seen = "programming", set()
for ch in s:
    if ch in seen: print(ch); break
    seen.add(ch)
```

**Output:**
```
r
```


## 51. Remove Duplicate Characters

**Definition:** Keep only the first occurrence of each character.

**Example:** programming → progamin

**Logic:** Use a set to track seen characters.

```python
s, seen, res = "programming", set(), ""
for ch in s:
    if ch not in seen: seen.add(ch); res += ch
print(res)
```

**Output:**
```
progamin
```


## 52. Remove Vowels / Spaces

**Definition:** Delete all vowels (or all spaces) from a string.

**Example:** "hello world" → "hll wrld" / "helloworld"

**Logic:** Build a new string with only the characters you want.

```python
s = "hello world"
print("".join(ch for ch in s if ch.lower() not in "aeiou"))
print(s.replace(" ", ""))
```

**Output:**
```
hll wrld
helloworld
```


## 53. Anagram Check

**Definition:** Two strings are anagrams if they contain exactly the same letters with the same counts.

**Example:** listen & silent → Anagram, hello & world → Not

**Logic:** Sort both and compare, or compare frequency counts (faster).

```python
from collections import Counter
for a, b in (("listen", "silent"), ("hello", "world"), ("Dormitory", "dirty room")):
    x, y = a.replace(" ", "").lower(), b.replace(" ", "").lower()
    print(a, "&", b, "→", "Anagram" if Counter(x) == Counter(y) else "Not Anagram")
```

**Output:**
```
listen & silent → Anagram
hello & world → Not Anagram
Dormitory & dirty room → Anagram
```


## 54. Toggle Case / Swap Case

**Definition:** Lowercase becomes uppercase and uppercase becomes lowercase.

**Example:** HeLLo → hEllO

**Logic:** Use ASCII: add or subtract 32, or use `swapcase()`.

```python
s = "HeLLo"
print("".join(ch.lower() if ch.isupper() else ch.upper() for ch in s))
print(s.swapcase())
```

**Output:**
```
hEllO
hEllO
```


## 55. Check Pangram

**Definition:** A sentence containing every letter a to z at least once.

**Example:** "The quick brown fox jumps over the lazy dog" → Pangram

**Logic:** Compare the set of letters with the full alphabet.

```python
import string
for s in ("The quick brown fox jumps over the lazy dog", "Hello world"):
    print(set(string.ascii_lowercase) <= set(s.lower()))
```

**Output:**
```
True
False
```


## 56. Reverse Words in a Sentence

**Definition:** Reverse the order of the words, not the letters.

**Example:** "I love coding" → "coding love I"

**Logic:** Split, reverse the list, join.

```python
print(" ".join("I love coding".split()[::-1]))
```

**Output:**
```
coding love I
```


## 57. Reverse Each Word

**Definition:** Keep the word order but reverse letters inside every word.

**Example:** "I love coding" → "I evol gnidoc"

**Logic:** Split, reverse each word, join.

```python
print(" ".join(w[::-1] for w in "I love coding".split()))
```

**Output:**
```
I evol gnidoc
```


## 58. Longest Word in a Sentence

**Definition:** Find the word with the most letters.

**Example:** "I love programming" → programming

**Logic:** `max(words, key=len)`

```python
print(max("I love programming a lot".split(), key=len))
```

**Output:**
```
programming
```


## 59. Capitalize First Letter of Each Word

**Definition:** Make the first letter of every word uppercase.

**Example:** "hello big world" → "Hello Big World"

**Logic:** Split and upper-case the first character.

```python
print(" ".join(w[0].upper() + w[1:] for w in "hello big world".split()))
```

**Output:**
```
Hello Big World
```


## 60. Compare Two Strings (without built-in)

**Definition:** Check if two strings are equal character by character.

**Example:** "abc" vs "abc" → Equal

**Logic:** Lengths must match, then compare each index.

```python
def same(a, b):
    if len(a) != len(b): return False
    for i in range(len(a)):
        if a[i] != b[i]: return False
    return True
print(same("abc", "abc"), same("abc", "abd"))
```

**Output:**
```
True False
```


## 61. Substring Search (Pattern Matching)

**Definition:** Find whether a smaller string appears inside a bigger string and where.

**Example:** "hello world" contains "world" at index 6

**Logic:** Slide the pattern over the text and compare each window.

```python
t, p = "hello world", "world"
pos = -1
for i in range(len(t) - len(p) + 1):
    if t[i:i + len(p)] == p: pos = i; break
print(pos)
```

**Output:**
```
6
```


## 62. Count Occurrences of a Substring

**Definition:** How many times a pattern appears (overlap allowed).

**Example:** "ababab", "ab" → 3

**Logic:** Check every window and count matches.

```python
t, p = "ababab", "ab"
print(sum(t[i:i + len(p)] == p for i in range(len(t) - len(p) + 1)))
```

**Output:**
```
3
```


## 63. String Compression

**Definition:** Replace repeated characters with character + count.

**Example:** aaabbc → a3b2c1

**Logic:** Count the length of each run of equal characters.

```python
s, res, i = "aaabbc", "", 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]: j += 1
    res += s[i] + str(j - i)
    i = j
print(res)
```

**Output:**
```
a3b2c1
```


## 64. Check if String is a Rotation of Another

**Definition:** Rotating "abcd" by 1 gives "bcda". Check if B can be obtained by rotating A.

**Example:** ABCD & CDAB → Yes

**Logic:** B must be a substring of A + A and lengths must match.

```python
a, b = "ABCD", "CDAB"
print(len(a) == len(b) and b in a + a)
```

**Output:**
```
True
```


## 65. Longest Palindromic Substring

**Definition:** Longest substring that is a palindrome.

**Example:** "babad" → "bab" (or "aba")

**Logic:** Expand around every centre (odd and even).

```python
def lps(s):
    best = ""
    for c in range(len(s)):
        for l, r in ((c, c), (c, c + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            if r - l - 1 > len(best): best = s[l + 1:r]
    return best
print(lps("babad"), lps("cbbd"))
```

**Output:**
```
bab bb
```


## 66. Longest Common Prefix

**Definition:** Longest starting part shared by all strings.

**Example:** ["flower","flow","flight"] → "fl"

**Logic:** Shrink the prefix until every word starts with it.

```python
words = ["flower", "flow", "flight"]
p = words[0]
for w in words[1:]:
    while not w.startswith(p): p = p[:-1]
print(repr(p))
```

**Output:**
```
'fl'
```


## 67. Longest Substring Without Repeating Characters

**Definition:** Longest window with all different characters.

**Example:** "abcabcbb" → 3 ("abc")

**Logic:** Sliding window with a dictionary of last seen index.

```python
s, last, start, best = "abcabcbb", {}, 0, 0
for i, ch in enumerate(s):
    if ch in last and last[ch] >= start: start = last[ch] + 1
    last[ch] = i
    best = max(best, i - start + 1)
print(best)
```

**Output:**
```
3
```


## 68. Isomorphic Strings

**Definition:** Characters of one string can be replaced one-to-one to get the other.

**Example:** egg & add → Yes, foo & bar → No

**Logic:** Maintain two mappings and check consistency.

```python
def iso(a, b):
    if len(a) != len(b): return False
    m1, m2 = {}, {}
    for x, y in zip(a, b):
        if m1.setdefault(x, y) != y or m2.setdefault(y, x) != x: return False
    return True
print(iso("egg", "add"), iso("foo", "bar"), iso("paper", "title"))
```

**Output:**
```
True False True
```


## 69. Valid Parentheses

**Definition:** Every opening bracket has the correct closing bracket in right order.

**Example:** "{[()]}" → Valid, "([)]" → Invalid

**Logic:** Push openings on a stack; on closing, top must match.

```python
def valid(s):
    pair, st = {")": "(", "]": "[", "}": "{"}, []
    for ch in s:
        if ch in "([{": st.append(ch)
        elif not st or st.pop() != pair[ch]: return False
    return not st
for s in ("{[()]}", "([)]", "((", ""):
    print(repr(s), valid(s))
```

**Output:**
```
'{[()]}' True
'([)]' False
'((' False
'' True
```


## 70. Remove All Adjacent Duplicates

**Definition:** Repeatedly delete pairs of equal neighbours.

**Example:** abbaca → ca

**Logic:** Use a stack; pop if top equals current character.

```python
st = []
for ch in "abbaca":
    if st and st[-1] == ch: st.pop()
    else: st.append(ch)
print("".join(st))
```

**Output:**
```
ca
```


## 71. Print All Permutations of a String

**Definition:** Every possible arrangement of the characters.

**Example:** abc → abc acb bac bca cab cba

**Logic:** Fix one character, permute the rest (recursion / backtracking).

```python
def perm(s, cur=""):
    if not s: print(cur, end=" "); return
    for i in range(len(s)):
        perm(s[:i] + s[i + 1:], cur + s[i])
perm("abc")
```

**Output:**
```
abc acb bac bca cab cba
```


## 72. Print All Substrings and Subsequences

**Definition:** Substring = continuous part. Subsequence = characters in order but may skip.

**Example:** abc → substrings a ab abc b bc c; subsequences add "ac" and empty

**Logic:** Two nested loops for substrings; include/exclude recursion for subsequences.

```python
s = "abc"
print([s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)])
def sub(i, cur):
    if i == len(s): print(repr(cur), end=" "); return
    sub(i + 1, cur + s[i]); sub(i + 1, cur)
sub(0, "")
```

**Output:**
```
['a', 'ab', 'abc', 'b', 'bc', 'c']
'abc' 'ab' 'ac' 'a' 'bc' 'b' 'c' ''
```


## 73. Caesar Cipher (Encrypt / Decrypt)

**Definition:** Shift each letter by a fixed number of positions.

**Example:** "Hello", shift 3 → "Khoor"

**Logic:** Use ASCII with modulo 26 and keep case.

```python
def caesar(s, k):
    out = ""
    for ch in s:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            out += chr((ord(ch) - base + k) % 26 + base)
        else: out += ch
    return out
e = caesar("Hello, World", 3)
print(e, "→", caesar(e, -3))
```

**Output:**
```
Khoor, Zruog → Hello, World
```


---

# PART D: Array Problems (Basic)


## 74. Largest and Smallest Element

**Definition:** Find the maximum and minimum value in an array.

**Example:** [4, 9, 1, 7] → max 9, min 1

**Logic:** Assume first element is both, update while scanning.

```python
a = [4, 9, 1, 7]
mx = mn = a[0]
for x in a:
    if x > mx: mx = x
    if x < mn: mn = x
print(mx, mn)
```

**Output:**
```
9 1
```


## 75. Second Largest / Second Smallest

**Definition:** Second biggest and second smallest distinct values.

**Example:** [10, 40, 30, 20] → 30 and 20

**Logic:** Track first and second in a single pass.

```python
a = [10, 40, 30, 20]
f = s = float("-inf")
for x in a:
    if x > f: s, f = f, x
    elif f > x > s: s = x
print("Second largest:", s)
f = s = float("inf")
for x in a:
    if x < f: s, f = f, x
    elif f < x < s: s = x
print("Second smallest:", s)
```

**Output:**
```
Second largest: 30
Second smallest: 20
```


## 76. Sum and Average

**Definition:** Total of all elements and total / count.

**Example:** [10, 20, 30, 40] → 100, 25.0

**Logic:** Accumulate in a loop.

```python
a = [10, 20, 30, 40]
print(sum(a), sum(a) / len(a))
```

**Output:**
```
100 25.0
```


## 77. Reverse an Array

**Definition:** Flip the order of elements in place.

**Example:** [1,2,3,4,5] → [5,4,3,2,1]

**Logic:** Swap first with last, move both pointers inward.

```python
a = [1, 2, 3, 4, 5]
l, r = 0, len(a) - 1
while l < r:
    a[l], a[r] = a[r], a[l]
    l += 1; r -= 1
print(a)
```

**Output:**
```
[5, 4, 3, 2, 1]
```


## 78. Count Even and Odd Elements

**Definition:** Number of even and odd values.

**Example:** [1,2,3,4,5,6,7] → even 3, odd 4

**Logic:** Check `x % 2`.

```python
a = [1, 2, 3, 4, 5, 6, 7]
e = sum(x % 2 == 0 for x in a)
print("Even:", e, "Odd:", len(a) - e)
```

**Output:**
```
Even: 3 Odd: 4
```


## 79. Linear Search

**Definition:** Check each element one by one until found.

**Example:** find 30 in [10,20,30,40] → index 2

**Logic:** Loop and compare. Time O(n).

```python
a, key = [10, 20, 30, 40], 30
print(next((i for i, x in enumerate(a) if x == key), -1))
```

**Output:**
```
2
```


## 80. Check if Array is Sorted

**Definition:** Each element is not greater than the next.

**Example:** [1,2,2,5] → Sorted, [3,1,2] → Not

**Logic:** Compare neighbours.

```python
for a in ([1, 2, 2, 5], [3, 1, 2]):
    print(a, all(a[i] <= a[i + 1] for i in range(len(a) - 1)))
```

**Output:**
```
[1, 2, 2, 5] True
[3, 1, 2] False
```


## 81. Copy and Merge Two Arrays

**Definition:** Copy = new array with same elements. Merge = join two arrays.

**Example:** [1,2,3] + [4,5] → [1,2,3,4,5]

**Logic:** Loop and append, or slicing.

```python
a, b = [1, 2, 3], [4, 5]
c = a[:]
merged = a + b
print(c, merged)
```

**Output:**
```
[1, 2, 3] [1, 2, 3, 4, 5]
```


## 82. Insert and Delete at a Position

**Definition:** Add or remove an element at a given index and shift the rest.

**Example:** insert 99 at index 2 in [1,2,3,4] → [1,2,99,3,4]

**Logic:** Shift elements right (insert) or left (delete).

```python
a = [1, 2, 3, 4]
a.insert(2, 99); print(a)
a.pop(1); print(a)
```

**Output:**
```
[1, 2, 99, 3, 4]
[1, 99, 3, 4]
```


---

# PART E: Array Problems (Medium)


## 83. Remove Duplicates from Array

**Definition:** Keep only unique elements.

**Example:** [1,1,2,2,3] → [1,2,3]

**Logic:** Sorted: two pointers. Unsorted: use a set (keep order with a seen set).

```python
a = [1, 1, 2, 2, 3, 3, 3]
j = 1
for i in range(1, len(a)):
    if a[i] != a[i - 1]: a[j] = a[i]; j += 1
print(a[:j])
seen, res = set(), []
for x in [4, 5, 4, 6, 5]:
    if x not in seen: seen.add(x); res.append(x)
print(res)
```

**Output:**
```
[1, 2, 3]
[4, 5, 6]
```


## 84. Find Duplicate Element

**Definition:** Find a number that appears more than once.

**Example:** [1,3,4,2,2] → 2

**Logic:** Use a set, or Floyd's cycle detection for O(1) space.

```python
seen = set()
for x in [1, 3, 4, 2, 2]:
    if x in seen: print(x); break
    seen.add(x)
```

**Output:**
```
2
```


## 85. Missing Number in 1 to N

**Definition:** One number from 1..N is absent.

**Example:** [1,2,4,5], N=5 → 3

**Logic:** Expected sum `N(N+1)/2` minus actual sum.

```python
a, n = [1, 2, 4, 5], 5
print(n * (n + 1) // 2 - sum(a))
```

**Output:**
```
3
```


## 86. Rotate Array by K

**Definition:** Shift elements left or right by k places.

**Example:** [1,2,3,4,5], k=2 → left [3,4,5,1,2], right [4,5,1,2,3]

**Logic:** Use `k % n` then slice, or reverse three times.

```python
a, k = [1, 2, 3, 4, 5], 2
k %= len(a)
print("Left :", a[k:] + a[:k])
print("Right:", a[-k:] + a[:-k])
```

**Output:**
```
Left : [3, 4, 5, 1, 2]
Right: [4, 5, 1, 2, 3]
```


## 87. Move All Zeros to End

**Definition:** Push zeros to the end keeping order of others.

**Example:** [0,1,0,3,12] → [1,3,12,0,0]

**Logic:** Pointer j marks the next slot for a non-zero.

```python
a = [0, 1, 0, 3, 12]
j = 0
for i in range(len(a)):
    if a[i] != 0:
        a[i], a[j] = a[j], a[i]; j += 1
print(a)
```

**Output:**
```
[1, 3, 12, 0, 0]
```


## 88. Separate Even and Odd Numbers

**Definition:** Put all evens first, then odds.

**Example:** [1,2,3,4,5,6] → [2,4,6,1,3,5]

**Logic:** Two pointers swapping wrong-placed elements.

```python
a = [1, 2, 3, 4, 5, 6]
l, r = 0, len(a) - 1
while l < r:
    if a[l] % 2 == 0: l += 1
    elif a[r] % 2 == 1: r -= 1
    else: a[l], a[r] = a[r], a[l]
print(a)
```

**Output:**
```
[6, 2, 4, 3, 5, 1]
```


## 89. Segregate 0s, 1s and 2s (Dutch National Flag)

**Definition:** Sort an array containing only 0, 1, 2 in one pass.

**Example:** [2,0,1,2,1,0] → [0,0,1,1,2,2]

**Logic:** Three pointers low, mid, high.

```python
a = [2, 0, 1, 2, 1, 0]
lo, mid, hi = 0, 0, len(a) - 1
while mid <= hi:
    if a[mid] == 0: a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1
    elif a[mid] == 1: mid += 1
    else: a[mid], a[hi] = a[hi], a[mid]; hi -= 1
print(a)
```

**Output:**
```
[0, 0, 1, 1, 2, 2]
```


## 90. Sort Array of 0s and 1s

**Definition:** Binary array sorted so 0s come first.

**Example:** [1,0,1,0,0,1] → [0,0,0,1,1,1]

**Logic:** Count zeros then fill, or two pointers.

```python
a = [1, 0, 1, 0, 0, 1]
z = a.count(0)
print([0] * z + [1] * (len(a) - z))
```

**Output:**
```
[0, 0, 0, 1, 1, 1]
```


## 91. Leaders in an Array

**Definition:** An element greater than everything to its right.

**Example:** [16,17,4,3,5,2] → 17, 5, 2

**Logic:** Scan from the right keeping the maximum so far.

```python
a, mx, res = [16, 17, 4, 3, 5, 2], float("-inf"), []
for x in reversed(a):
    if x > mx: res.append(x); mx = x
print(res[::-1])
```

**Output:**
```
[17, 5, 2]
```


## 92. Array Intersection and Union

**Definition:** Intersection = common elements. Union = all unique elements.

**Example:** [1,2,3,4] & [3,4,5] → common [3,4], union [1,2,3,4,5]

**Logic:** Use sets.

```python
a, b = [1, 2, 3, 4], [3, 4, 5]
print(sorted(set(a) & set(b)), sorted(set(a) | set(b)))
```

**Output:**
```
[3, 4] [1, 2, 3, 4, 5]
```


## 93. Frequency of Each Element

**Definition:** Count occurrences of every element.

**Example:** [1,2,2,3,3,3] → {1:1, 2:2, 3:3}

**Logic:** Dictionary counting.

```python
from collections import Counter
print(dict(Counter([1, 2, 2, 3, 3, 3])))
```

**Output:**
```
{1: 1, 2: 2, 3: 3}
```


## 94. Two Sum

**Definition:** Find two indices whose values add up to a target.

**Example:** [2,7,11,15], target 9 → indices 0 and 1

**Logic:** Dictionary stores seen numbers; check `target - x`.

```python
a, t, seen = [2, 7, 11, 15], 9, {}
for i, x in enumerate(a):
    if t - x in seen: print(seen[t - x], i); break
    seen[x] = i
```

**Output:**
```
0 1
```


## 95. Kadane's Algorithm (Maximum Subarray Sum)

**Definition:** Largest sum of a continuous part of an array.

**Example:** [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray 4,-1,2,1)

**Logic:** At each element choose: start fresh or extend the previous sum.

```python
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
cur = best = a[0]
for x in a[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)
print(best)
```

**Output:**
```
6
```


## 96. Majority Element (Moore's Voting)

**Definition:** An element that appears more than n/2 times.

**Example:** [2,2,1,1,1,2,2] → 2

**Logic:** Cancel out different pairs; the survivor is the candidate.

```python
a, cand, cnt = [2, 2, 1, 1, 1, 2, 2], None, 0
for x in a:
    if cnt == 0: cand = x
    cnt += 1 if x == cand else -1
print(cand, a.count(cand) > len(a) // 2)
```

**Output:**
```
2 True
```


## 97. Equilibrium Index

**Definition:** Index where sum of left elements equals sum of right elements.

**Example:** [-7,1,5,2,-4,3,0] → 3

**Logic:** Keep left sum, right = total - left - current.

```python
a, total, left = [-7, 1, 5, 2, -4, 3, 0], 0, 0
total = sum(a)
for i, x in enumerate(a):
    if left == total - left - x: print(i); break
    left += x
```

**Output:**
```
3
```


## 98. Prefix Sum and Suffix Sum

**Definition:** Prefix[i] = sum of elements up to i. Suffix[i] = sum from i to end.

**Example:** [1,2,3,4] → prefix [1,3,6,10], suffix [10,9,7,4]

**Logic:** Running totals. Range sum(l..r) = prefix[r] - prefix[l-1].

```python
a = [1, 2, 3, 4]
pre = [sum(a[:i + 1]) for i in range(len(a))]
suf = [sum(a[i:]) for i in range(len(a))]
print(pre, suf)
```

**Output:**
```
[1, 3, 6, 10] [10, 9, 7, 4]
```


## 99. Pair with Given Sum / Difference

**Definition:** Find all pairs adding to a sum (or having a difference).

**Example:** [1,5,7,-1,5], sum 6 → (1,5) (7,-1) (1,5)

**Logic:** Hash map of seen values.

```python
a, t, seen, pairs = [1, 5, 7, -1, 5], 6, {}, []
for x in a:
    for _ in range(seen.get(t - x, 0)): pairs.append((t - x, x))
    seen[x] = seen.get(x, 0) + 1
print(pairs)
```

**Output:**
```
[(1, 5), (7, -1), (1, 5)]
```


## 100. Product of Array Except Self

**Definition:** For each index, product of all other elements (no division).

**Example:** [1,2,3,4] → [24,12,8,6]

**Logic:** Prefix products times suffix products.

```python
a = [1, 2, 3, 4]
res, p = [1] * len(a), 1
for i in range(len(a)): res[i] = p; p *= a[i]
p = 1
for i in range(len(a) - 1, -1, -1): res[i] *= p; p *= a[i]
print(res)
```

**Output:**
```
[24, 12, 8, 6]
```


---

# PART F: Array Problems (Advanced)


## 101. Trapping Rain Water

**Definition:** Water trapped between bars after rain.

**Example:** [0,1,0,2,1,0,1,3,2,1,2,1] → 6

**Logic:** Two pointers with left max and right max.

```python
h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
l, r, lm, rm, w = 0, len(h) - 1, 0, 0, 0
while l < r:
    if h[l] < h[r]:
        lm = max(lm, h[l]); w += lm - h[l]; l += 1
    else:
        rm = max(rm, h[r]); w += rm - h[r]; r -= 1
print(w)
```

**Output:**
```
6
```


## 102. Maximum Product Subarray

**Definition:** Continuous subarray with the largest product.

**Example:** [2,3,-2,4,-1] → 48 (whole array: 2 x 3 x -2 x 4 x -1)

**Logic:** Track both max and min product (negatives flip).

```python
a = [2, 3, -2, 4, -1]
mx = mn = best = a[0]
for x in a[1:]:
    c = (x, mx * x, mn * x)
    mx, mn = max(c), min(c)
    best = max(best, mx)
print(best)
```

**Output:**
```
48
```


## 103. Merge Intervals

**Definition:** Combine overlapping intervals.

**Example:** [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

**Logic:** Sort by start, extend the last interval when overlapping.

```python
iv = sorted([[1, 3], [2, 6], [8, 10], [15, 18]])
res = [iv[0]]
for s, e in iv[1:]:
    if s <= res[-1][1]: res[-1][1] = max(res[-1][1], e)
    else: res.append([s, e])
print(res)
```

**Output:**
```
[[1, 6], [8, 10], [15, 18]]
```


## 104. Next Greater Element

**Definition:** For each element, the first greater element to its right (else -1).

**Example:** [4,5,2,25] → [5,25,25,-1]

**Logic:** Monotonic stack scanning from the right.

```python
a, res, st = [4, 5, 2, 25], [-1] * 4, []
for i in range(len(a) - 1, -1, -1):
    while st and st[-1] <= a[i]: st.pop()
    res[i] = st[-1] if st else -1
    st.append(a[i])
print(res)
```

**Output:**
```
[5, 25, 25, -1]
```


## 105. Next Permutation

**Definition:** Rearrange into the next lexicographically greater arrangement.

**Example:** [1,2,3] → [1,3,2], [3,2,1] → [1,2,3]

**Logic:** Find pivot from right, swap with next larger, reverse the tail.

```python
def nxt(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]: i -= 1
    if i >= 0:
        j = len(a) - 1
        while a[j] <= a[i]: j -= 1
        a[i], a[j] = a[j], a[i]
    a[i + 1:] = a[i + 1:][::-1]
    return a
print(nxt([1, 2, 3]), nxt([3, 2, 1]), nxt([1, 1, 5]))
```

**Output:**
```
[1, 3, 2] [1, 2, 3] [1, 5, 1]
```


## 106. Subarray with Given Sum

**Definition:** Continuous part adding to a target (positive numbers).

**Example:** [1,4,20,3,10,5], target 33 → indices 2..4

**Logic:** Sliding window: expand, shrink when sum exceeds.

```python
a, t, l, s = [1, 4, 20, 3, 10, 5], 33, 0, 0
for r, x in enumerate(a):
    s += x
    while s > t: s -= a[l]; l += 1
    if s == t: print(l, r); break
```

**Output:**
```
2 4
```


## 107. Longest Consecutive Sequence

**Definition:** Longest run of consecutive integers (any order in array).

**Example:** [100,4,200,1,3,2] → 4 (1,2,3,4)

**Logic:** Put in a set; start counting only from numbers with no predecessor.

```python
s, best = set([100, 4, 200, 1, 3, 2]), 0
for x in s:
    if x - 1 not in s:
        y = x
        while y + 1 in s: y += 1
        best = max(best, y - x + 1)
print(best)
```

**Output:**
```
4
```


## 108. Count Inversions

**Definition:** Pairs (i, j) with i < j but a[i] > a[j].

**Example:** [2,4,1,3,5] → 3

**Logic:** Modified merge sort counts inversions while merging.

```python
def count(a):
    if len(a) <= 1: return a, 0
    m = len(a) // 2
    l, x = count(a[:m]); r, y = count(a[m:])
    res, i, j, inv = [], 0, 0, x + y
    while i < len(l) and j < len(r):
        if l[i] <= r[j]: res.append(l[i]); i += 1
        else: res.append(r[j]); j += 1; inv += len(l) - i
    return res + l[i:] + r[j:], inv
print(count([2, 4, 1, 3, 5])[1])
```

**Output:**
```
3
```


## 109. Sliding Window Maximum

**Definition:** Maximum of every window of size k.

**Example:** [1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]

**Logic:** Deque keeps indices of decreasing values.

```python
from collections import deque
a, k, dq, res = [1, 3, -1, -3, 5, 3, 6, 7], 3, deque(), []
for i, x in enumerate(a):
    while dq and a[dq[-1]] <= x: dq.pop()
    dq.append(i)
    if dq[0] <= i - k: dq.popleft()
    if i >= k - 1: res.append(a[dq[0]])
print(res)
```

**Output:**
```
[3, 3, 5, 5, 6, 7]
```


## 110. 3Sum and 4Sum

**Definition:** Find unique triplets (or quadruplets) that add up to zero (or target).

**Example:** [-1,0,1,2,-1,-4] → [-1,-1,2] and [-1,0,1]

**Logic:** Sort, fix one number, two pointers for the rest.

```python
a = sorted([-1, 0, 1, 2, -1, -4]); res = []
for i in range(len(a) - 2):
    if i and a[i] == a[i - 1]: continue
    l, r = i + 1, len(a) - 1
    while l < r:
        s = a[i] + a[l] + a[r]
        if s < 0: l += 1
        elif s > 0: r -= 1
        else:
            res.append([a[i], a[l], a[r]]); l += 1
            while l < r and a[l] == a[l - 1]: l += 1
print(res)
```

**Output:**
```
[[-1, -1, 2], [-1, 0, 1]]
```


## 111. Stock Buy and Sell (Max Profit)

**Definition:** Buy once, sell later to earn the most profit.

**Example:** [7,1,5,3,6,4] → 5 (buy 1, sell 6)

**Logic:** Track the minimum price so far.

```python
p, mn, best = [7, 1, 5, 3, 6, 4], float("inf"), 0
for x in p:
    mn = min(mn, x)
    best = max(best, x - mn)
print(best)
```

**Output:**
```
5
```


## 112. Container with Most Water

**Definition:** Choose two lines forming a container holding the most water.

**Example:** [1,8,6,2,5,4,8,3,7] → 49

**Logic:** Two pointers, move the shorter wall inward.

```python
h, l, r, best = [1, 8, 6, 2, 5, 4, 8, 3, 7], 0, 8, 0
while l < r:
    best = max(best, min(h[l], h[r]) * (r - l))
    if h[l] < h[r]: l += 1
    else: r -= 1
print(best)
```

**Output:**
```
49
```


---

# PART G: 2D Array / Matrix Problems


## 113. Print Matrix (Row-wise and Column-wise)

**Definition:** A matrix is a table of rows and columns.

**Example:** [[1,2,3],[4,5,6],[7,8,9]]

**Logic:** Row-wise: outer loop rows. Column-wise: outer loop columns.

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for r in m: print(*r)
print("-- column wise --")
for j in range(3): print(*[m[i][j] for i in range(3)])
```

**Output:**
```
1 2 3
4 5 6
7 8 9
-- column wise --
1 4 7
2 5 8
3 6 9
```


## 114. Sum of Rows, Columns and Diagonals

**Definition:** Add the elements of each row, column and both diagonals.

**Example:** 3x3 above → rows 6 15 24, cols 12 15 18, diagonals 15 and 15

**Logic:** Main diagonal i==j, secondary diagonal i+j==n-1.

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n = 3
print("Rows:", [sum(r) for r in m])
print("Cols:", [sum(m[i][j] for i in range(n)) for j in range(n)])
print("Main:", sum(m[i][i] for i in range(n)), "Secondary:", sum(m[i][n - 1 - i] for i in range(n)))
```

**Output:**
```
Rows: [6, 15, 24]
Cols: [12, 15, 18]
Main: 15 Secondary: 15
```


## 115. Transpose of a Matrix

**Definition:** Swap rows and columns: `T[j][i] = M[i][j]`.

**Example:** [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]

**Logic:** Build a new matrix with swapped indexes.

```python
m = [[1, 2, 3], [4, 5, 6]]
t = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
for r in t: print(*r)
```

**Output:**
```
1 4
2 5
3 6
```


## 116. Matrix Addition, Subtraction and Multiplication

**Definition:** Add/subtract same-position elements. Multiply: `C[i][j] = sum(A[i][k] * B[k][j])`.

**Example:** [[1,2],[3,4]] x [[5,6],[7,8]] → [[19,22],[43,50]]

**Logic:** Triple loop for multiplication.

```python
A, B = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
add = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
mul = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print("Add:", add, "\nMul:", mul)
```

**Output:**
```
Add: [[6, 8], [10, 12]] 
Mul: [[19, 22], [43, 50]]
```


## 117. Check Symmetric Matrix

**Definition:** A square matrix equal to its transpose.

**Example:** [[1,2],[2,1]] → Symmetric

**Logic:** Check `m[i][j] == m[j][i]` for all i, j.

```python
for m in ([[1, 2], [2, 1]], [[1, 2], [3, 4]]):
    print(m, all(m[i][j] == m[j][i] for i in range(len(m)) for j in range(len(m))))
```

**Output:**
```
[[1, 2], [2, 1]] True
[[1, 2], [3, 4]] False
```


## 118. Identity, Sparse and Diagonal Matrix

**Definition:** Identity: 1 on diagonal, 0 elsewhere. Diagonal: non-zero only on diagonal. Sparse: more than half the elements are zero.

**Example:** [[1,0],[0,1]] → Identity, Diagonal

**Logic:** Check each position's value against its condition.

```python
m = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
n = len(m)
print("Identity:", all(m[i][j] == (1 if i == j else 0) for i in range(n) for j in range(n)))
print("Diagonal:", all(m[i][j] == 0 for i in range(n) for j in range(n) if i != j))
print("Sparse  :", sum(x == 0 for r in m for x in r) > n * n // 2)
```

**Output:**
```
Identity: True
Diagonal: True
Sparse  : True
```


## 119. Upper and Lower Triangular Matrix

**Definition:** Upper: all elements below the diagonal are 0. Lower: all above the diagonal are 0.

**Example:** [[1,2,3],[0,4,5],[0,0,6]] → Upper triangular

**Logic:** Upper: `j < i` must be zero. Lower: `j > i` must be zero.

```python
m = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]; n = 3
print("Upper:", all(m[i][j] == 0 for i in range(n) for j in range(i)))
print("Lower:", all(m[i][j] == 0 for i in range(n) for j in range(i + 1, n)))
```

**Output:**
```
Upper: True
Lower: False
```


## 120. Rotate Matrix by 90 Degrees

**Definition:** Rotate a square matrix clockwise.

**Example:** [[1,2,3],[4,5,6],[7,8,9]] → [[7,4,1],[8,5,2],[9,6,3]]

**Logic:** Transpose, then reverse every row.

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n = 3
for i in range(n):
    for j in range(i + 1, n): m[i][j], m[j][i] = m[j][i], m[i][j]
for r in m: r.reverse()
for r in m: print(*r)
```

**Output:**
```
7 4 1
8 5 2
9 6 3
```


## 121. Spiral Traversal

**Definition:** Visit elements in a spiral: right, down, left, up.

**Example:** 3x3 above → 1 2 3 6 9 8 7 4 5

**Logic:** Four boundaries (top, bottom, left, right) shrinking inward.

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t, b, l, r, res = 0, 2, 0, 2, []
while t <= b and l <= r:
    res += m[t][l:r + 1]; t += 1
    res += [m[i][r] for i in range(t, b + 1)]; r -= 1
    if t <= b: res += m[b][l:r + 1][::-1]; b -= 1
    if l <= r: res += [m[i][l] for i in range(b, t - 1, -1)]; l += 1
print(res)
```

**Output:**
```
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```


## 122. Boundary Traversal

**Definition:** Print only the outer border elements.

**Example:** 3x3 above → 1 2 3 6 9 8 7 4

**Logic:** Top row, right column, bottom row reversed, left column reversed.

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = m[0] + [m[i][2] for i in range(1, 3)] + m[2][:-1][::-1] + [m[i][0] for i in range(1, 2)][::-1]
print(res)
```

**Output:**
```
[1, 2, 3, 6, 9, 8, 7, 4]
```


## 123. Diagonal Traversal

**Definition:** Visit elements along diagonals (i + j constant).

**Example:** 3x3 above → [1] [2,4] [3,5,7] [6,8] [9]

**Logic:** Group elements by `i + j`.

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for d in range(5):
    print([m[i][d - i] for i in range(3) if 0 <= d - i < 3])
```

**Output:**
```
[1]
[2, 4]
[3, 5, 7]
[6, 8]
[9]
```


## 124. Search in a Sorted Matrix

**Definition:** Rows and columns are sorted; find a key fast.

**Example:** key 16 in [[1,4,7],[8,11,16],[20,25,30]] → found at (1,2)

**Logic:** Start at top-right: smaller → go left, larger → go down.

```python
m, key = [[1, 4, 7], [8, 11, 16], [20, 25, 30]], 16
i, j = 0, 2
while i < 3 and j >= 0:
    if m[i][j] == key: print("Found at", (i, j)); break
    if m[i][j] > key: j -= 1
    else: i += 1
```

**Output:**
```
Found at (1, 2)
```


## 125. Set Matrix Zeroes

**Definition:** If an element is 0, make its entire row and column 0.

**Example:** [[1,1,1],[1,0,1],[1,1,1]] → [[1,0,1],[0,0,0],[1,0,1]]

**Logic:** Record zero rows/cols first, then update.

```python
m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
rows = {i for i, r in enumerate(m) if 0 in r}
cols = {j for r in m for j, x in enumerate(r) if x == 0}
for i in range(3):
    for j in range(3):
        if i in rows or j in cols: m[i][j] = 0
for r in m: print(*r)
```

**Output:**
```
1 0 1
0 0 0
1 0 1
```


## 126. Saddle Point

**Definition:** An element that is the minimum in its row and maximum in its column.

**Example:** [[9,8,7],[5,3,2],[6,6,1]] → 7 at (0,2): smallest in its row (7) and largest in its column (7,2,1)

**Logic:** Find each row minimum and check it is the maximum of its column.

```python
m = [[9, 8, 7], [5, 3, 2], [6, 6, 1]]
for i, r in enumerate(m):
    j = r.index(min(r))
    if m[i][j] == max(row[j] for row in m): print("Saddle point:", m[i][j], "at", (i, j))
```

**Output:**
```
Saddle point: 7 at (0, 2)
```


## 127. Pascal's Triangle (Matrix Form)

**Definition:** Each element is the sum of the two above it.

**Example:** 5 rows → 1 / 1 1 / 1 2 1 / 1 3 3 1 / 1 4 6 4 1

**Logic:** `tri[i][j] = tri[i-1][j-1] + tri[i-1][j]`

```python
n, tri = 5, []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i): row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
    tri.append(row)
for r in tri: print(*r)
```

**Output:**
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```


## 128. Magic Square Check

**Definition:** Every row, column and both diagonals have the same sum.

**Example:** [[2,7,6],[9,5,1],[4,3,8]] → Magic (sum 15)

**Logic:** Compute all sums and compare.

```python
m = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]; n = 3
sums = [sum(r) for r in m] + [sum(m[i][j] for i in range(n)) for j in range(n)]
sums += [sum(m[i][i] for i in range(n)), sum(m[i][n - 1 - i] for i in range(n))]
print("Magic" if len(set(sums)) == 1 else "Not Magic", set(sums))
```

**Output:**
```
Magic {15}
```


## 129. Sudoku Validator

**Definition:** Each row, column and 3x3 box must contain 1 to 9 without repeats.

**Example:** A correct completed board → Valid

**Logic:** Use sets for rows, columns and boxes.

```python
board = [[(i * 3 + i // 3 + j) % 9 + 1 for j in range(9)] for i in range(9)]
ok = all(len(set(r)) == 9 for r in board)
ok &= all(len({board[i][j] for i in range(9)}) == 9 for j in range(9))
ok &= all(len({board[r + i][c + j] for i in range(3) for j in range(3)}) == 9 for r in (0, 3, 6) for c in (0, 3, 6))
print("Valid" if ok else "Invalid")
```

**Output:**
```
Valid
```


## 130. Maximum Sum Rectangle (Advanced)

**Definition:** Find the sub-rectangle with the largest sum.

**Example:** [[1,2,-1],[-3,4,2],[2,-1,3]] → 9 (the whole matrix: 1+2-1-3+4+2+2-1+3)

**Logic:** Fix two rows, compress columns, then run Kadane.

```python
m = [[1, 2, -1], [-3, 4, 2], [2, -1, 3]]
R, C, best = 3, 3, float("-inf")
for top in range(R):
    col = [0] * C
    for bot in range(top, R):
        for j in range(C): col[j] += m[bot][j]
        cur = mx = col[0]
        for x in col[1:]:
            cur = max(x, cur + x); mx = max(mx, cur)
        best = max(best, mx)
print(best)
```

**Output:**
```
9
```


---

# PART H: Searching and Sorting


## 131. Linear Search vs Binary Search

**Definition:** Linear: check one by one. Binary: halve a SORTED array each step.

**Example:** find 23 in [2,5,8,12,16,23,38,56] → index 5

**Logic:** Compare with middle; discard the half that cannot contain the key. Time O(log n).

```python
a, key = [2, 5, 8, 12, 16, 23, 38, 56], 23
lo, hi = 0, len(a) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] == key: print("Found at", mid); break
    if a[mid] < key: lo = mid + 1
    else: hi = mid - 1
```

**Output:**
```
Found at 5
```


## 132. Binary Search (Recursive)

**Definition:** Same as binary search but the function calls itself.

**Example:** find 16 → index 4

**Logic:** Base case: lo > hi means not found.

```python
def bs(a, k, lo, hi):
    if lo > hi: return -1
    m = (lo + hi) // 2
    if a[m] == k: return m
    return bs(a, k, m + 1, hi) if a[m] < k else bs(a, k, lo, m - 1)
a = [2, 5, 8, 12, 16, 23]
print(bs(a, 16, 0, len(a) - 1), bs(a, 99, 0, len(a) - 1))
```

**Output:**
```
4 -1
```


## 133. First and Last Occurrence

**Definition:** Positions of the first and last time a value appears in a sorted array.

**Example:** [1,2,2,2,3], key 2 → first 1, last 3

**Logic:** Binary search, but keep searching left (or right) after a match.

```python
def find(a, k, first):
    lo, hi, res = 0, len(a) - 1, -1
    while lo <= hi:
        m = (lo + hi) // 2
        if a[m] == k:
            res = m
            if first: hi = m - 1
            else: lo = m + 1
        elif a[m] < k: lo = m + 1
        else: hi = m - 1
    return res
a = [1, 2, 2, 2, 3]
print(find(a, 2, True), find(a, 2, False))
```

**Output:**
```
1 3
```


## 134. Search in Rotated Sorted Array

**Definition:** A sorted array rotated at an unknown pivot.

**Example:** [4,5,6,7,0,1,2], key 0 → index 4

**Logic:** One half is always sorted; decide which half holds the key.

```python
a, k = [4, 5, 6, 7, 0, 1, 2], 0
lo, hi, ans = 0, len(a) - 1, -1
while lo <= hi:
    m = (lo + hi) // 2
    if a[m] == k: ans = m; break
    if a[lo] <= a[m]:
        if a[lo] <= k < a[m]: hi = m - 1
        else: lo = m + 1
    else:
        if a[m] < k <= a[hi]: lo = m + 1
        else: hi = m - 1
print(ans)
```

**Output:**
```
4
```


## 135. Peak Element

**Definition:** An element greater than both neighbours.

**Example:** [1,3,20,4,1,0] → 20

**Logic:** Binary search: move toward the larger neighbour.

```python
a = [1, 3, 20, 4, 1, 0]
lo, hi = 0, len(a) - 1
while lo < hi:
    m = (lo + hi) // 2
    if a[m] < a[m + 1]: lo = m + 1
    else: hi = m
print(a[lo])
```

**Output:**
```
20
```


## 136. Square Root using Binary Search

**Definition:** Integer square root (floor) without sqrt().

**Example:** 50 → 7

**Logic:** Binary search the answer between 1 and n.

```python
n, lo, hi, ans = 50, 1, 50, 0
while lo <= hi:
    m = (lo + hi) // 2
    if m * m <= n: ans = m; lo = m + 1
    else: hi = m - 1
print(ans)
```

**Output:**
```
7
```


## 137. Bubble Sort

**Definition:** Repeatedly swap adjacent elements if they are in the wrong order.

**Example:** [64,34,25,12,22] → [12,22,25,34,64]

**Logic:** After each pass the largest element "bubbles" to the end. O(n²).

```python
a = [64, 34, 25, 12, 22]
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]: a[j], a[j + 1] = a[j + 1], a[j]
print(a)
```

**Output:**
```
[12, 22, 25, 34, 64]
```


## 138. Selection Sort

**Definition:** Pick the minimum of the unsorted part and place it at the front.

**Example:** [64,25,12,22,11] → [11,12,22,25,64]

**Logic:** Find min index, swap with current position. O(n²).

```python
a = [64, 25, 12, 22, 11]
for i in range(len(a)):
    m = min(range(i, len(a)), key=lambda k: a[k])
    a[i], a[m] = a[m], a[i]
print(a)
```

**Output:**
```
[11, 12, 22, 25, 64]
```


## 139. Insertion Sort

**Definition:** Insert each element into its correct place in the sorted left part (like sorting playing cards).

**Example:** [12,11,13,5,6] → [5,6,11,12,13]

**Logic:** Shift bigger elements right, drop the key in the gap.

```python
a = [12, 11, 13, 5, 6]
for i in range(1, len(a)):
    key, j = a[i], i - 1
    while j >= 0 and a[j] > key: a[j + 1] = a[j]; j -= 1
    a[j + 1] = key
print(a)
```

**Output:**
```
[5, 6, 11, 12, 13]
```


## 140. Merge Sort

**Definition:** Divide the array in halves, sort each, then merge. Time O(n log n).

**Example:** [38,27,43,3,9,82,10] → [3,9,10,27,38,43,82]

**Logic:** Recursion + merge two sorted lists.

```python
def ms(a):
    if len(a) <= 1: return a
    m = len(a) // 2
    l, r, res = ms(a[:m]), ms(a[m:]), []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]: res.append(l[i]); i += 1
        else: res.append(r[j]); j += 1
    return res + l[i:] + r[j:]
print(ms([38, 27, 43, 3, 9, 82, 10]))
```

**Output:**
```
[3, 9, 10, 27, 38, 43, 82]
```


## 141. Quick Sort

**Definition:** Pick a pivot, put smaller elements left and larger right, recurse. Average O(n log n).

**Example:** [10,7,8,9,1,5] → [1,5,7,8,9,10]

**Logic:** Partition around the pivot.

```python
def qs(a):
    if len(a) <= 1: return a
    p = a[len(a) // 2]
    return qs([x for x in a if x < p]) + [x for x in a if x == p] + qs([x for x in a if x > p])
print(qs([10, 7, 8, 9, 1, 5]))
```

**Output:**
```
[1, 5, 7, 8, 9, 10]
```


## 142. Heap Sort

**Definition:** Build a max-heap, repeatedly move the max to the end. O(n log n).

**Example:** [12,11,13,5,6,7] → [5,6,7,11,12,13]

**Logic:** Heapify, swap root with last, shrink heap.

```python
def heapify(a, n, i):
    big, l, r = i, 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[big]: big = l
    if r < n and a[r] > a[big]: big = r
    if big != i: a[i], a[big] = a[big], a[i]; heapify(a, n, big)
a = [12, 11, 13, 5, 6, 7]
for i in range(len(a) // 2 - 1, -1, -1): heapify(a, len(a), i)
for end in range(len(a) - 1, 0, -1):
    a[0], a[end] = a[end], a[0]; heapify(a, end, 0)
print(a)
```

**Output:**
```
[5, 6, 7, 11, 12, 13]
```


## 143. Counting Sort

**Definition:** Count how many times each value occurs, then rebuild. Works for small integer ranges. O(n + k).

**Example:** [4,2,2,8,3,3,1] → [1,2,2,3,3,4,8]

**Logic:** Frequency array of size max+1.

```python
a = [4, 2, 2, 8, 3, 3, 1]
cnt = [0] * (max(a) + 1)
for x in a: cnt[x] += 1
print([i for i, c in enumerate(cnt) for _ in range(c)])
```

**Output:**
```
[1, 2, 2, 3, 3, 4, 8]
```


## 144. Sort by Frequency and Custom Comparator

**Definition:** Order elements by how often they occur (ties by value).

**Example:** [4,5,6,5,4,3] → [3,6,4,4,5,5]

**Logic:** Sort with a key tuple `(frequency, value)`.

```python
from collections import Counter
a = [4, 5, 6, 5, 4, 3]
c = Counter(a)
print(sorted(a, key=lambda x: (c[x], x)))
print(sorted(["pear", "fig", "banana", "kiwi"], key=lambda s: (len(s), s)))
```

**Output:**
```
[3, 6, 4, 4, 5, 5]
['fig', 'kiwi', 'pear', 'banana']
```


## 145. K-th Largest Element

**Definition:** The element that would be at position k from the top if sorted descending.

**Example:** [3,2,1,5,6,4], k=2 → 5

**Logic:** Sort, or keep a min-heap of size k.

```python
import heapq
a, k = [3, 2, 1, 5, 6, 4], 2
h = []
for x in a:
    heapq.heappush(h, x)
    if len(h) > k: heapq.heappop(h)
print(h[0])
```

**Output:**
```
5
```


---

# PART I: Recursion Problems


## 146. Factorial and Fibonacci (Recursion)

**Definition:** A function that calls itself with a smaller input until a base case.

**Example:** fact(5) = 120, fib(8) = 21

**Logic:** Always write the base case first.

```python
def fact(n): return 1 if n <= 1 else n * fact(n - 1)
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fact(5), fib(8))
```

**Output:**
```
120 21
```


## 147. Sum of Digits and Reverse Number (Recursion)

**Definition:** Break the number using `n % 10` and `n // 10` in each call.

**Example:** 1234 → sum 10, reverse 4321

**Logic:** Reverse needs a helper with accumulator.

```python
def sod(n): return 0 if n == 0 else n % 10 + sod(n // 10)
def rev(n, r=0): return r if n == 0 else rev(n // 10, r * 10 + n % 10)
print(sod(1234), rev(1234))
```

**Output:**
```
10 4321
```


## 148. Power of a Number (Recursion)

**Definition:** x^n using divide and conquer.

**Example:** 2^10 = 1024

**Logic:** `x^n = (x^(n/2))²`, times x if n is odd.

```python
def p(x, n):
    if n == 0: return 1
    h = p(x, n // 2)
    return h * h * (x if n % 2 else 1)
print(p(2, 10), p(3, 5))
```

**Output:**
```
1024 243
```


## 149. Palindrome and GCD (Recursion)

**Definition:** Check ends and recurse inward / Euclid with recursion.

**Example:** "level" → True, gcd(48, 18) → 6

**Logic:** Palindrome: compare first and last, recurse on the middle.

```python
def pal(s): return len(s) < 2 or (s[0] == s[-1] and pal(s[1:-1]))
def gcd(a, b): return a if b == 0 else gcd(b, a % b)
print(pal("level"), pal("hello"), gcd(48, 18))
```

**Output:**
```
True False 6
```


## 150. Print 1 to N and N to 1

**Definition:** Print numbers using recursion only.

**Example:** N = 5 → 1 2 3 4 5 and 5 4 3 2 1

**Logic:** Print before the recursive call to go down, after it to go up.

```python
def up(n):
    if n: up(n - 1); print(n, end=" ")
def down(n):
    if n: print(n, end=" "); down(n - 1)
up(5); print(); down(5)
```

**Output:**
```
1 2 3 4 5 
5 4 3 2 1
```


## 151. Tower of Hanoi

**Definition:** Move n disks from A to C using B, one at a time, never placing a bigger disk on a smaller one.

**Example:** 3 disks → 7 moves (2ⁿ - 1)

**Logic:** Move n-1 to helper, move last disk, move n-1 onto it.

```python
def hanoi(n, a, c, b):
    if n == 0: return
    hanoi(n - 1, a, b, c)
    print(f"Move disk {n}: {a} → {c}")
    hanoi(n - 1, b, c, a)
hanoi(3, "A", "C", "B")
```

**Output:**
```
Move disk 1: A → C
Move disk 2: A → B
Move disk 1: C → B
Move disk 3: A → C
Move disk 1: B → A
Move disk 2: B → C
Move disk 1: A → C
```


## 152. Generate All Subsets (Power Set)

**Definition:** Every possible selection of elements, including empty.

**Example:** [1,2,3] → 8 subsets

**Logic:** For each element: include or exclude.

```python
def subsets(a, i=0, cur=[]):
    if i == len(a): print(cur); return
    subsets(a, i + 1, cur + [a[i]])
    subsets(a, i + 1, cur)
subsets([1, 2, 3])
```

**Output:**
```
[1, 2, 3]
[1, 2]
[1, 3]
[1]
[2, 3]
[2]
[3]
[]
```


## 153. Generate All Permutations (Array)

**Definition:** Every possible order of the elements.

**Example:** [1,2,3] → 6 permutations

**Logic:** Swap each element into the first position, recurse on the rest.

```python
def perm(a, l=0):
    if l == len(a): print(a); return
    for i in range(l, len(a)):
        a[l], a[i] = a[i], a[l]
        perm(a, l + 1)
        a[l], a[i] = a[i], a[l]
perm([1, 2, 3])
```

**Output:**
```
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
```


## 154. N-Queens

**Definition:** Place N queens on an N x N board so none attack each other.

**Example:** N = 4 → 2 solutions

**Logic:** Backtracking: place row by row, check column and diagonals.

```python
def solve(n):
    res = []
    def go(r, cols):
        if r == n: res.append(cols[:]); return
        for c in range(n):
            if all(c != x and abs(c - x) != r - i for i, x in enumerate(cols)):
                go(r + 1, cols + [c])
    go(0, [])
    return res
for sol in solve(4):
    for c in sol: print("".join("Q" if j == c else "." for j in range(4)))
    print()
```

**Output:**
```
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..
```


## 155. Sudoku Solver

**Definition:** Fill a 9x9 grid so every row, column and 3x3 box has 1 to 9.

**Example:** Standard puzzle with blanks (0)

**Logic:** Backtracking: try 1..9 in each empty cell, undo if stuck.

```python
g = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
def ok(r, c, v):
    if v in g[r] or any(g[i][c] == v for i in range(9)): return False
    br, bc = r // 3 * 3, c // 3 * 3
    return all(g[br + i][bc + j] != v for i in range(3) for j in range(3))
def solve():
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                for v in range(1, 10):
                    if ok(r, c, v):
                        g[r][c] = v
                        if solve(): return True
                        g[r][c] = 0
                return False
    return True
solve()
for r in g: print(*r)
```

**Output:**
```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```


## 156. Rat in a Maze

**Definition:** Find a path from top-left to bottom-right moving through open cells (1).

**Example:** 4x4 maze → path of D (down) and R (right)

**Logic:** Backtracking: try each direction, mark visited, undo on failure.

```python
m = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
n, path = 4, []
def go(r, c, p, seen):
    if r == n - 1 and c == n - 1: path.append(p); return
    for dr, dc, ch in ((1,0,"D"),(0,1,"R"),(0,-1,"L"),(-1,0,"U")):
        a, b = r + dr, c + dc
        if 0 <= a < n and 0 <= b < n and m[a][b] and (a, b) not in seen:
            go(a, b, p + ch, seen | {(a, b)})
go(0, 0, "", {(0, 0)})
print(path)
```

**Output:**
```
['DRDDRR']
```


## 157. Subset Sum

**Definition:** Is there a subset whose sum equals the target?

**Example:** [3,34,4,12,5,2], target 9 → Yes (4+5)

**Logic:** Include or exclude each element.

```python
def ss(a, i, t):
    if t == 0: return True
    if i == len(a) or t < 0: return False
    return ss(a, i + 1, t - a[i]) or ss(a, i + 1, t)
print(ss([3, 34, 4, 12, 5, 2], 0, 9), ss([3, 34, 4], 0, 100))
```

**Output:**
```
True False
```


## 158. Combination Sum

**Definition:** Find all combinations of numbers (reuse allowed) adding to a target.

**Example:** [2,3,6,7], target 7 → [2,2,3], [7]

**Logic:** Backtracking; stay on same index to allow reuse.

```python
def comb(a, t, i=0, cur=[]):
    if t == 0: print(cur); return
    for k in range(i, len(a)):
        if a[k] <= t: comb(a, t - a[k], k, cur + [a[k]])
comb([2, 3, 6, 7], 7)
```

**Output:**
```
[2, 2, 3]
[7]
```


---

# PART J: Bit Manipulation, Maths and Puzzles


## 159. Check if Number is a Power of 2

**Definition:** Numbers like 1, 2, 4, 8, 16 ... have exactly one bit set.

**Example:** 16 → Yes, 18 → No

**Logic:** `n & (n - 1) == 0`

```python
for n in (16, 18, 1, 0):
    print(n, n > 0 and n & (n - 1) == 0)
```

**Output:**
```
16 True
18 False
1 True
0 False
```


## 160. Count Set Bits

**Definition:** Number of 1s in the binary form.

**Example:** 13 = 1101 → 3

**Logic:** Brian Kernighan: `n &= n - 1` removes the lowest set bit.

```python
n, c = 13, 0
while n: n &= n - 1; c += 1
print(c, bin(13))
```

**Output:**
```
3 0b1101
```


## 161. Swap Using XOR

**Definition:** XOR swapping needs no extra variable.

**Example:** a=5, b=9 → a=9, b=5

**Logic:** `a ^= b; b ^= a; a ^= b`

```python
a, b = 5, 9
a ^= b; b ^= a; a ^= b
print(a, b)
```

**Output:**
```
9 5
```


## 162. Single Non-Repeating Number (XOR)

**Definition:** Every number appears twice except one.

**Example:** [4,1,2,1,2] → 4

**Logic:** XOR of equal numbers is 0, so duplicates cancel.

```python
r = 0
for x in [4, 1, 2, 1, 2]: r ^= x
print(r)
```

**Output:**
```
4
```


## 163. Find Two Missing Numbers

**Definition:** Two numbers are missing from 1..N.

**Example:** [1,2,4,6], N = 6 → 3 and 5

**Logic:** Sum and product (or sum and sum of squares) give two equations.

```python
a, n = [1, 2, 4, 6], 6
s = n * (n + 1) // 2 - sum(a)
sq = n * (n + 1) * (2 * n + 1) // 6 - sum(x * x for x in a)
d = int((2 * sq - s * s) ** 0.5)
print((s - d) // 2, (s + d) // 2)
```

**Output:**
```
3 5
```


## 164. Reverse Bits

**Definition:** Reverse the binary representation.

**Example:** 8-bit 00001101 (13) → 10110000 (176)

**Logic:** Shift bits out of one end into the other.

```python
n, r = 13, 0
for _ in range(8):
    r = (r << 1) | (n & 1); n >>= 1
print(r, format(r, "08b"))
```

**Output:**
```
176 10110000
```


## 165. Gray Code

**Definition:** Sequence where consecutive numbers differ in one bit.

**Example:** 3 bits → 000 001 011 010 110 111 101 100

**Logic:** `i ^ (i >> 1)`

```python
print([format(i ^ (i >> 1), "03b") for i in range(8)])
```

**Output:**
```
['000', '001', '011', '010', '110', '111', '101', '100']
```


## 166. Pythagorean Triplets

**Definition:** Three numbers with a² + b² = c².

**Example:** (3,4,5) (5,12,13) (6,8,10)

**Logic:** Two loops for a, b and check if c is integer.

```python
from math import isqrt
n = 20
print([(a, b, isqrt(a * a + b * b)) for a in range(1, n) for b in range(a, n)
       if isqrt(a * a + b * b) ** 2 == a * a + b * b and isqrt(a * a + b * b) <= n])
```

**Output:**
```
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
```


## 167. Collatz Sequence

**Definition:** If even divide by 2, if odd do 3n + 1, repeat until 1.

**Example:** 6 → 6 3 10 5 16 8 4 2 1

**Logic:** Simple while loop.

```python
n, seq = 6, []
while n != 1:
    seq.append(n); n = n // 2 if n % 2 == 0 else 3 * n + 1
print(seq + [1])
```

**Output:**
```
[6, 3, 10, 5, 16, 8, 4, 2, 1]
```


## 168. Sum of Series

**Definition:** Sum of common mathematical series.

**Example:** 1 + 1/2 + 1/3 + ... + 1/5, and e^x = 1 + x + x²/2! + ...

**Logic:** Loop with running term; multiply/divide to get the next term.

```python
print("Harmonic:", round(sum(1 / i for i in range(1, 6)), 4))
x, term, total = 1, 1.0, 1.0
for i in range(1, 15):
    term *= x / i; total += term
print("e^1 ≈", round(total, 5))
print("1²+2²+..+5² =", sum(i * i for i in range(1, 6)))
```

**Output:**
```
Harmonic: 2.2833
e^1 ≈ 2.71828
1²+2²+..+5² = 55
```


## 169. Perfect Square Series

**Definition:** Squares of natural numbers: 1, 4, 9, 16, ...

**Example:** First 10 → 1 4 9 16 25 36 49 64 81 100

**Logic:** Square of loop counter, or add successive odd numbers.

```python
print([i * i for i in range(1, 11)])
s, odd = 0, 1
for _ in range(5): s += odd; odd += 2; print(s, end=" ")
```

**Output:**
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
1 4 9 16 25
```


## 170. Print All Divisors and Check Co-Prime

**Definition:** Divisors of n. Two numbers are co-prime when GCD = 1.

**Example:** divisors of 28 → 1 2 4 7 14 28, (8, 15) co-prime

**Logic:** Loop to √n. Co-prime via GCD.

```python
from math import gcd
print([i for i in range(1, 29) if 28 % i == 0])
print(gcd(8, 15) == 1, gcd(8, 12) == 1)
```

**Output:**
```
[1, 2, 4, 7, 14, 28]
True False
```
