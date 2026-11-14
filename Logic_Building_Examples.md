# Logic Building: Examples, Output Look and How to Solve

> Language used: **Python** (easy to read). The logic is identical in C / C++ / Java.
> Each example has: **Question → Output (how it looks) → Logic → Code**.

---

## 0. Golden Rule for Solving Anything

```
1. Read the question and write a small input/output example.
2. Solve it by hand on paper for 2 or 3 inputs.
3. Find the repeating step  ->  that is your LOOP.
4. Find the decision point  ->  that is your IF.
5. Write code. Dry run. Test edge cases (0, 1, negative, empty).
```

---

# PART 1: STAR PATTERNS

**Pattern thinking trick:** for every row `i` ask 3 things:
`how many spaces?` / `how many stars?` / `what is printed in between?`

---

## Category 1: Basic Patterns

### 1. Solid Square (n = 5)
```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```
**Logic:** n rows, n stars in each row.
```python
n = 5
for i in range(n):
    print("* " * n)
```

### 2. Hollow Square (n = 5)
```
* * * * *
*       *
*       *
*       *
* * * * *
```
**Logic:** print `*` only if it is the first/last row or first/last column, else space.
```python
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

### 3. Right Triangle (n = 5)
```
*
* *
* * *
* * * *
* * * * *
```
**Logic:** row `i` has `i` stars.
```python
n = 5
for i in range(1, n+1):
    print("* " * i)
```

### 4. Inverted Right Triangle (n = 5)
```
* * * * *
* * * *
* * *
* *
*
```
**Logic:** row `i` goes from n down to 1.
```python
n = 5
for i in range(n, 0, -1):
    print("* " * i)
```

### 5. Right-Aligned Triangle (n = 5)
```
        *
      * *
    * * *
  * * * *
* * * * *
```
**Logic:** spaces = `2*(n-i)`, stars = `i`.
```python
n = 5
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)
```

---

## Category 2: Pyramid Patterns

### 6. Full Pyramid (n = 5)
```
    *
   * *
  * * *
 * * * *
* * * * *
```
**Logic:** spaces = `n-i`, stars = `i` (each star followed by a space).
```python
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
```

### 7. Inverted Pyramid (n = 5)
```
* * * * *
 * * * *
  * * *
   * *
    *
```
```python
n = 5
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)
```

### 8. Hollow Pyramid (n = 5)
```
    *
   * *
  *   *
 *     *
* * * * *
```
**Logic:** first row = 1 star. Last row = full. Middle rows = star + `(2i-3)` spaces + star.
```python
n = 5
for i in range(1, n+1):
    print(" " * (n-i), end="")
    if i == 1:
        print("*")
    elif i == n:
        print("* " * n)
    else:
        print("*" + " " * (2*i - 3) + "*")
```

---

## Category 3: Diamond and Shapes (n = 4)

### 9. Solid Diamond
```
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
```
**Logic:** pyramid for `i = 1..n`, then inverted pyramid for `i = n-1..1`.
```python
n = 4
for i in list(range(1, n+1)) + list(range(n-1, 0, -1)):
    print(" " * (n-i) + "* " * i)
```

### 10. Hollow Diamond
```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```
```python
n = 4
for i in list(range(1, n+1)) + list(range(n-1, 0, -1)):
    print(" " * (n-i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2*i - 3) + "*")
```

### 11. Half Diamond
```
*
* *
* * *
* * * *
* * *
* *
*
```
```python
n = 4
for i in list(range(1, n+1)) + list(range(n-1, 0, -1)):
    print("* " * i)
```

### 12. Butterfly
```
*      *
**    **
***  ***
********
***  ***
**    **
*      *
```
**Logic:** left stars `i` + spaces `2*(n-i)` + right stars `i`.
```python
n = 4
for i in list(range(1, n+1)) + list(range(n-1, 0, -1)):
    print("*" * i + " " * (2*(n-i)) + "*" * i)
```

### 13. Hourglass
```
* * * *
 * * *
  * *
   *
  * *
 * * *
* * * *
```
```python
n = 4
for i in list(range(n, 0, -1)) + list(range(2, n+1)):
    print(" " * (n-i) + "* " * i)
```

### 14. Parallelogram (n = 4, width 5)
```
*****
 *****
  *****
   *****
```
**Logic:** row `i` has `i` leading spaces then fixed stars.
```python
n = 4
for i in range(n):
    print(" " * i + "*" * 5)
```

---

## Category 4: Condition-Based Patterns (n = 5)
> Trick: use `i` (row) and `j` (column) in an `if` condition.

### 15. Plus (+)
```
  *
  *
*****
  *
  *
```
**Condition:** `i == mid or j == mid`
```python
n = 5
mid = n // 2
for i in range(n):
    for j in range(n):
        print("*" if i == mid or j == mid else " ", end="")
    print()
```

### 16. X Pattern
```
*   *
 * *
  *
 * *
*   *
```
**Condition:** `i == j or i + j == n-1`
```python
n = 5
for i in range(n):
    for j in range(n):
        print("*" if i == j or i + j == n-1 else " ", end="")
    print()
```

### 17. Letter Z
```
*****
   *
  *
 *
*****
```
**Condition:** `i == 0 or i == n-1 or i + j == n-1`
```python
n = 5
for i in range(n):
    for j in range(n):
        print("*" if i == 0 or i == n-1 or i + j == n-1 else " ", end="")
    print()
```

### 18. Checkerboard
```
*   *   *
  *   *
*   *   *
  *   *
*   *   *
```
**Condition:** `(i + j) % 2 == 0`
```python
n = 5
for i in range(n):
    for j in range(n):
        print("*" if (i + j) % 2 == 0 else " ", end=" ")
    print()
```

---

## Category 5: Number and Alphabet Patterns

### 19. Number Triangle (n = 5)
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
```python
n = 5
for i in range(1, n+1):
    print(*range(1, i+1))
```

### 20. Same Number Triangle (n = 4)
```
1
2 2
3 3 3
4 4 4 4
```
```python
n = 4
for i in range(1, n+1):
    print((str(i) + " ") * i)
```

### 21. Floyd's Triangle (n = 4)
```
1
2 3
4 5 6
7 8 9 10
```
**Logic:** one counter that keeps increasing and never resets.
```python
n = 4
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

### 22. Alphabet Triangle (n = 4)
```
A
A B
A B C
A B C D
```
**Logic:** `chr(65 + j)` converts 0 to A, 1 to B, and so on.
```python
n = 4
for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
```

### 23. Binary Triangle (n = 4)
```
1
0 1
1 0 1
0 1 0 1
```
**Logic:** value = `(i + j + 1) % 2`.
```python
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print((i + j + 1) % 2, end=" ")
    print()
```

### 24. Number Pyramid / Palindrome Pyramid (n = 4)
```
   1
  121
 12321
1234321
```
**Logic:** spaces, then count up to `i`, then count down to 1.
```python
n = 4
for i in range(1, n+1):
    up = "".join(str(j) for j in range(1, i+1))
    down = "".join(str(j) for j in range(i-1, 0, -1))
    print(" " * (n-i) + up + down)
```

### 25. Pascal's Triangle (n = 5)
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```
**Logic:** each number = sum of the two numbers above it.
```python
n = 5
row = [1]
for _ in range(n):
    print(" ".join(map(str, row)).center(2*n - 1))
    row = [a + b for a, b in zip([0] + row, row + [0])]
```

### 26. Concentric Squares (n = 3)
```
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
```
**Logic:** value = `n - (distance from nearest border)`.
```python
n = 3
size = 2*n - 1
for i in range(size):
    for j in range(size):
        print(n - min(i, j, size-1-i, size-1-j), end=" ")
    print()
```

---

# PART 2: NUMBER LOGIC

### 1. Factorial
**Question:** Find `5!`  (5 x 4 x 3 x 2 x 1)
**Output:** `120`
**Logic:** start result = 1, multiply with every number from 1 to n.
```python
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)   # 120
```

### 2. Fibonacci Series
**Question:** Print first 8 terms.
**Output:** `0 1 1 2 3 5 8 13`
**Logic:** next = previous two added. Keep two variables `a, b`.
```python
n = 8
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

### 3. Prime Number Check
**Question:** Is 29 prime?
**Output:** `Prime`
**Logic:** a number is prime if no number from 2 to sqrt(n) divides it. We stop at sqrt because divisors come in pairs.
```python
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print("Prime" if is_prime(29) else "Not Prime")
```
**Dry run (n = 29):** i=2 (29%2=1), i=3 (29%3=2), i=4 (29%4=1), i=5 → 25 <= 29 (29%5=4), i=6 → 36 > 29 stop → Prime.

### 4. All Primes up to N (Sieve of Eratosthenes)
**Output (N = 30):** `2 3 5 7 11 13 17 19 23 29`
**Logic:** assume all are prime, then cross out multiples of each prime.
```python
N = 30
is_p = [True] * (N + 1)
is_p[0] = is_p[1] = False
for i in range(2, int(N**0.5) + 1):
    if is_p[i]:
        for j in range(i*i, N+1, i):
            is_p[j] = False
print([i for i in range(N+1) if is_p[i]])
```

### 5. Reverse a Number
**Question:** `1234` → `4321`
**Logic:** take last digit (`n % 10`), add it to rev (`rev*10 + digit`), remove last digit (`n // 10`).
```python
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)   # 4321
```
| n | digit | rev |
|---|-------|-----|
| 1234 | 4 | 4 |
| 123 | 3 | 43 |
| 12 | 2 | 432 |
| 1 | 1 | 4321 |

### 6. Palindrome Number
**Question:** `121` is palindrome, `123` is not.
**Logic:** reverse the number and compare with original.
```python
n = 121
temp, rev = n, 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Palindrome" if rev == n else "Not Palindrome")
```

### 7. Sum of Digits
**Question:** `1234` → `10`
```python
n = 1234
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)   # 10
```

### 8. Armstrong Number
**Question:** `153` → 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✔
**Logic:** count digits `p`, add each digit raised to power `p`, compare.
```python
n = 153
p = len(str(n))
total = sum(int(d) ** p for d in str(n))
print("Armstrong" if total == n else "Not Armstrong")
```

### 9. GCD (HCF) and LCM
**Question:** GCD(12, 18) = 6, LCM = 36
**Logic (Euclid):** `gcd(a, b) = gcd(b, a % b)` until b becomes 0. `LCM = a*b / GCD`.
```python
a, b = 12, 18
x, y = a, b
while y:
    x, y = y, x % y
print("GCD:", x)            # 6
print("LCM:", a * b // x)   # 36
```

### 10. Perfect Number
**Question:** `28` = 1 + 2 + 4 + 7 + 14 = 28 ✔
**Logic:** add all divisors except the number itself.
```python
n = 28
s = sum(i for i in range(1, n//2 + 1) if n % i == 0)
print("Perfect" if s == n else "Not Perfect")
```

### 11. Strong Number
**Question:** `145` = 1! + 4! + 5! = 1 + 24 + 120 = 145 ✔
```python
from math import factorial
n = 145
s = sum(factorial(int(d)) for d in str(n))
print("Strong" if s == n else "Not Strong")
```

### 12. Decimal to Binary
**Question:** `10` → `1010`
**Logic:** divide by 2 repeatedly, collect remainders, read them in reverse.
```python
n = 10
bits = ""
while n > 0:
    bits = str(n % 2) + bits
    n //= 2
print(bits)   # 1010
```

### 13. Power of 2 Check (Bit Trick)
**Logic:** a power of 2 has only one `1` bit, so `n & (n-1) == 0`.
```python
n = 16
print("Yes" if n > 0 and n & (n-1) == 0 else "No")   # Yes
```

---

# PART 3: STRING LOGIC

### 14. Palindrome String
**Question:** `madam` → Yes
```python
s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")
```

### 15. Count Vowels
**Question:** `education` → 5
```python
s = "education"
count = sum(1 for ch in s.lower() if ch in "aeiou")
print(count)   # 5
```

### 16. Anagram Check
**Question:** `listen` and `silent` use the same letters → Anagram.
**Logic:** sort both and compare, or count letters of both.
```python
a, b = "listen", "silent"

# Method 1: sorting
print(sorted(a) == sorted(b))          # True

# Method 2: frequency count (faster, O(n))
from collections import Counter
print(Counter(a) == Counter(b))        # True
```

### 17. Character Frequency
**Question:** `banana` → `{'b':1, 'a':3, 'n':2}`
```python
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)   # {'b': 1, 'a': 3, 'n': 2}
```

### 18. First Non-Repeating Character
**Question:** `swiss` → `w`
**Logic:** count all characters first, then scan again and return first with count 1.
```python
from collections import Counter
s = "swiss"
cnt = Counter(s)
for ch in s:
    if cnt[ch] == 1:
        print(ch)   # w
        break
```

### 19. Reverse Words in a Sentence
**Question:** `I love coding` → `coding love I`
```python
s = "I love coding"
print(" ".join(s.split()[::-1]))
```

### 20. Remove Duplicate Characters
**Question:** `programming` → `progamin`
```python
s = "programming"
res = ""
for ch in s:
    if ch not in res:
        res += ch
print(res)   # progamin
```

### 21. String Compression
**Question:** `aaabbc` → `a3b2c1`
**Logic:** for each character, count how many times it repeats in a row.
```python
s = "aaabbc"
res, i = "", 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    res += s[i] + str(j - i)
    i = j
print(res)   # a3b2c1
```

---

# PART 4: ARRAY LOGIC (Bridge to DSA)

### 22. Second Largest Element
**Question:** `[10, 40, 30, 20]` → `30`
**Logic:** track `largest` and `second` in a single pass.
```python
arr = [10, 40, 30, 20]
first = second = float("-inf")
for x in arr:
    if x > first:
        second, first = first, x
    elif first > x > second:
        second = x
print(second)   # 30
```

### 23. Missing Number (1 to N)
**Question:** `[1, 2, 4, 5]`, N = 5 → `3`
**Logic:** expected sum `N(N+1)/2` minus actual sum.
```python
arr = [1, 2, 4, 5]
n = 5
print(n * (n + 1) // 2 - sum(arr))   # 3
```

### 24. Move All Zeros to End
**Question:** `[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`
**Logic:** keep pointer `j` for the next non-zero position and swap.
```python
a = [0, 1, 0, 3, 12]
j = 0
for i in range(len(a)):
    if a[i] != 0:
        a[i], a[j] = a[j], a[i]
        j += 1
print(a)   # [1, 3, 12, 0, 0]
```

### 25. Rotate Array Left by K
**Question:** `[1,2,3,4,5]`, k = 2 → `[3,4,5,1,2]`
```python
a, k = [1, 2, 3, 4, 5], 2
k %= len(a)
print(a[k:] + a[:k])   # [3, 4, 5, 1, 2]
```

### 26. Two Sum
**Question:** `[2, 7, 11, 15]`, target = 9 → indices `(0, 1)`
**Logic:** store each seen number in a dictionary; check if `target - x` was already seen.
```python
a, target = [2, 7, 11, 15], 9
seen = {}
for i, x in enumerate(a):
    if target - x in seen:
        print(seen[target - x], i)   # 0 1
        break
    seen[x] = i
```

### 27. Maximum Subarray Sum (Kadane's Algorithm)
**Question:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → `6` (subarray `4, -1, 2, 1`)
**Logic:** at every element decide: *start fresh* or *extend* the previous sum.
```python
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
cur = best = a[0]
for x in a[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)
print(best)   # 6
```
| x | cur | best |
|---|-----|------|
| -2 | -2 | -2 |
| 1 | 1 | 1 |
| -3 | -2 | 1 |
| 4 | 4 | 4 |
| -1 | 3 | 4 |
| 2 | 5 | 5 |
| 1 | 6 | 6 |
| -5 | 1 | 6 |
| 4 | 5 | 6 |

---

# Practice Plan Before Starting DSA

- [ ] Type (do not copy) every pattern 1 to 26 and change `n` to see the effect
- [ ] Draw a new pattern yourself and find its `spaces / stars` formula
- [ ] Solve Part 2 and Part 3 without looking, then compare
- [ ] Explain each solution out loud in simple words
- [ ] Solve Part 4 using only loops (no built-in functions), then using built-ins

> After this, start DSA with: **Time and Space Complexity → Arrays → Strings → Hashing → Recursion → Sorting/Searching → Linked List → Stack/Queue → Trees → Graphs → DP**.
