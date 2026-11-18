# **30 Number-Based Programming Questions – Definitions, Examples & Manual Solutions**

This is your complete number-programming practice syllabus. We'll understand every question **without writing code first**.

For each program, I'll explain:

1. Simple definition.
2. Example input.
3. Step-by-step mathematical calculation.
4. Final answer.

# **Part 1: Basic Number Programs**

## **1. Reverse a Number**

**Definition:** Reverse a number by arranging its digits from last to first.

**Example:** 12345

Calculation:

Original: 1 → 2 → 3 → 4 → 5

Reverse: 5 → 4 → 3 → 2 → 1

Answer: 54321

Other examples:

- 123 → 321
- 456 → 654
- 120 → 21

## **2. Palindrome Number**

**Definition:** A number is a palindrome if its reverse is equal to the original number.

**Example:** 121

Calculation:

Original = 121

Reverse = 121

\\[ 121=121 \\]

121 is Palindrome

Another example:

123 → 321

123 ≠ 321, so it is not a palindrome.

## **3. Count Digits**

**Definition:** Count the total number of digits present in a number.

**Example:** 12345

Calculation:

1, 2, 3, 4, 5

Total digits = 5.

Answer: 5

Other examples:

- 123 → 3 digits
- 56 → 2 digits
- 987654 → 6 digits

## **4. Sum of Digits**

**Definition:** Add all individual digits of a number.

**Example:** 1234

Calculation:

\\[ 1+2+3+4=10 \\]

Answer: 10

Another example:

567 = 5 + 6 + 7 = 18.

## **5. Armstrong Number**

**Definition:** A number is Armstrong if the sum of its digits raised to the power of the total number of digits equals the original number.

**Formula:**

\\[ n=d_1^k+d_2^k+\cdots+d_k^k \\]

Here, k = total digits.

**Example:** 153

153 has 3 digits.

\\[ 1^3+5^3+3^3 \\]

\\[ 1+125+27=153 \\]

153 is Armstrong

### **Armstrong Number in a Range**

**Definition:** Find all Armstrong numbers between two given numbers.

Example: Range 1 to 500.

Some calculations:

- 1 → \\(1^1=1\\)
- 153 → \\(1^3+5^3+3^3=153\\)
- 370 → \\(3^3+7^3+0^3=370\\)
- 371 → \\(3^3+7^3+1^3=371\\)
- 407 → \\(4^3+0^3+7^3=407\\)

Answer:

1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407.

## **6. Prime Number Check**

**Definition:** A prime number is greater than 1 and has exactly two factors: 1 and itself.

**Example:** 7

Factors: 1, 7.

Total factors = 2.

7 is Prime

Another example: 8

Factors: 1, 2, 4, 8.

Total factors = 4.

8 is Not Prime

## **7. Prime Numbers in a Range**

**Definition:** Find all prime numbers between two given numbers.

Example: 1 to 20.

Check some numbers:

| Number | Factors    | Result    |
| ------ | ---------- | --------- |
| 2      | 1, 2       | Prime     |
| 3      | 1, 3       | Prime     |
| 4      | 1, 2, 4    | Not Prime |
| 5      | 1, 5       | Prime     |
| 6      | 1, 2, 3, 6 | Not Prime |
| 7      | 1, 7       | Prime     |
| 9      | 1, 3, 9    | Not Prime |
| 11     | 1, 11      | Prime     |
| 13     | 1, 13      | Prime     |
| 17     | 1, 17      | Prime     |
| 19     | 1, 19      | Prime     |

Answer:

\\[ 2,3,5,7,11,13,17,19 \\]

Total = 8 prime numbers.

## **8. Perfect Number**

**Definition:** A number is perfect if the sum of its factors, excluding itself, equals the original number.

**Example:** 6

Factors: 1, 2, 3, 6.

Exclude 6.

\\[ 1+2+3=6 \\]

6 is Perfect

Another example: 28

\\[ 1+2+4+7+14=28 \\]

## **9. Strong Number**

**Definition:** A number is strong if the sum of the factorials of its digits equals the original number.

**Formula:**

\\[ n=d_1!+d_2!+\cdots+d_k! \\]

**Example:** 145

Remember factorial:

\\[ 5!=5\times4\times3\times2\times1=120 \\]

Calculation:

\\[ 1!+4!+5! \\]

\\[ 1+24+120=145 \\]

145 is Strong

## **10. Automorphic Number**

**Definition:** A number is automorphic if its square ends with the original number.

**Example:** 25

Step 1: Calculate square.

\\[ 25^2=625 \\]

Step 2: Check ending digits.

625 ends with 25.

25 is Automorphic

Another example:

\\[ 76^2=5776 \\]

5776 ends with 76.

So 76 is automorphic.

# **Part 2: Mathematical Number Programs**

## **11. Neon Number**

**Definition:** A number is neon if the sum of the digits of its square equals the original number.

**Example:** 9

Step 1: Square the number.

\\[ 9^2=81 \\]

Step 2: Add square's digits.

\\[ 8+1=9 \\]

9 is Neon

## **12. Harshad (Niven) Number**

**Definition:** A number is Harshad if it is completely divisible by the sum of its digits.

**Example:** 18

Step 1: Sum digits.

\\[ 1+8=9 \\]

Step 2: Divide original number by digit sum.

\\[ 18\div9=2 \\]

Remainder = 0.

18 is Harshad

Another example: 19

\\[ 1+9=10 \\]

19 is not divisible by 10.

So 19 is not Harshad.

## **13. Happy Number**

**Definition:** A number is happy if repeatedly adding the squares of its digits eventually produces 1.

**Example:** 19

Step 1:

\\[ 1^2+9^2=1+81=82 \\]

Step 2:

\\[ 8^2+2^2=64+4=68 \\]

Step 3:

\\[ 6^2+8^2=36+64=100 \\]

Step 4:

\\[ 1^2+0^2+0^2=1 \\]

19 is Happy

## **14. Magic Number**

**Definition:** In a common programming definition, a number is magic if repeatedly adding its digits until one digit remains gives 1.

**Example:** 1729

Step 1:

\\[ 1+7+2+9=19 \\]

Step 2:

\\[ 1+9=10 \\]

Step 3:

\\[ 1+0=1 \\]

1729 is Magic

Note: Some textbooks use a different definition of Magic Number. Confirm the definition expected in your syllabus or interview.

## **15. Spy Number**

**Definition:** A number is a spy number if the sum of its digits equals the product of its digits.

**Example:** 1124

Sum:

\\[ 1+1+2+4=8 \\]

Product:

\\[ 1\times1\times2\times4=8 \\]

Sum = Product.

1124 is Spy Number

Another example: 123

Sum = 1 + 2 + 3 = 6.

Product = 1 × 2 × 3 = 6.

So 123 is also a Spy Number.

## **16. Krishnamurthy Number**

**Definition:** A number is Krishnamurthy if the sum of the factorials of its digits equals the original number.

**Example:** 145

\\[ 1!+4!+5! \\]

\\[ 1+24+120=145 \\]

145 is Krishnamurthy

**Important:** Krishnamurthy Number and Strong Number use the same mathematical definition.

## **17. Disarium Number**

**Definition:** A number is Disarium if the sum of its digits raised to their respective positions equals the original number.

Positions start from the left at 1.

**Example:** 135

- First digit: \\(1^1=1\\)
- Second digit: \\(3^2=9\\)
- Third digit: \\(5^3=125\\)

Calculation:

\\[ 1+9+125=135 \\]

135 is Disarium

Another example: 89

\\[ 8^1+9^2=8+81=89 \\]

## **18. Duck Number**

**Definition:** A Duck Number contains at least one zero in its digits, but zero should not be the leading digit.

**Example:** 1023

Digits: 1, 0, 2, 3.

It contains zero.

1023 is Duck Number

Another example:

- 405 → Duck Number.
- 1205 → Duck Number.
- 123 → Not Duck Number.
- 0123 → Usually treated as 123, not a Duck Number.

## **19. Buzz Number**

**Definition:** A number is a Buzz Number if it is divisible by 7 or its last digit is 7.

**Example 1:** 14

\\[ 14\div7=2 \\]

Remainder = 0.

14 is Buzz Number

**Example 2:** 27

It ends with 7.

27 is Buzz Number

Example 3: 25

Not divisible by 7 and does not end with 7.

Not a Buzz Number.

# **Part 3: Mathematical and Series Programs**

## **20. GCD / HCF and LCM**

**GCD/HCF Definition:** The greatest number that divides two numbers completely.

**LCM Definition:** The smallest positive number that is divisible by both numbers.

**Example:** 12 and 18.

Factors of 12:

1, 2, 3, 4, 6, 12.

Factors of 18:

1, 2, 3, 6, 9, 18.

Common factors:

1, 2, 3, 6.

GCD/HCF = 6

Multiples of 12:

12, 24, 36, 48...

Multiples of 18:

18, 36, 54...

First common multiple = 36.

LCM = 36

**Formula:**

\\[ HCF\times LCM=a\times b \\]

\\[ 6\times36=12\times18=216 \\]

## **21. Prime Factorization**

**Definition:** Breaking a number into prime numbers whose product equals the original number.

**Example:** 60

Divide by the smallest possible prime number repeatedly.

| Calculation | Result |
| ----------- | ------ |
| 60 ÷ 2      | 30     |
| 30 ÷ 2      | 15     |
| 15 ÷ 3      | 5      |
| 5 ÷ 5       | 1      |

Now multiply all prime factors:

\\[ 60=2\times2\times3\times5 \\]

Prime Factors: 2, 2, 3, 5

## **22. Fibonacci Series (Loop and Recursion)**

**Definition:** A series where each new number is the sum of the previous two numbers.

**Formula:**

\\[ F_n=F\_{n-1}+F\_{n-2} \\]

Starting values:

\\[ F_0=0,\quad F_1=1 \\]

**Example: First 8 numbers**

| Position | Calculation     | Result |
| -------- | --------------- | ------ |
| 1        | Starting number | 0      |
| 2        | Starting number | 1      |
| 3        | 0 + 1           | 1      |
| 4        | 1 + 1           | 2      |
| 5        | 1 + 2           | 3      |
| 6        | 2 + 3           | 5      |
| 7        | 3 + 5           | 8      |
| 8        | 5 + 8           | 13     |

Answer:

\\[ 0,1,1,2,3,5,8,13 \\]

**Two approaches:**

- Loop: Calculate next number repeatedly.
- Recursion: Calculate a number by calling the same function for previous two numbers.

## **23. Check Fibonacci Number**

**Definition:** Check whether a given number is present in the Fibonacci series.

**Example:** 13

Fibonacci series:

\\[ 0,1,1,2,3,5,8,13,21 \\]

13 is present.

13 is Fibonacci Number

Another example: 10.

10 is not present in the series.

**Mathematical condition:**

A positive integer \\(n\\) is Fibonacci if either:

\\[ 5n^2+4 \\]

or

\\[ 5n^2-4 \\]

is a perfect square.

## **24. Power of a Number (Without&#x20;**`pow`**)**

**Definition:** Calculate a number raised to a particular power using repeated multiplication.

**Formula:**

\\[ a^b=\underbrace{a\times a\times\cdots\times a}\_{b\text{ times}} \\]

**Example:**

\\[ 2^4=2\times2\times2\times2 \\]

\\[ =16 \\]

Answer = 16

Another example:

\\[ 3^3=3\times3\times3=27 \\]

## **25. Number to Words Conversion**

**Definition:** Convert a numerical value into its English word representation.

**Example 1:**

Input: 123

Break it into:

- 1 → One
- 2 → Twenty
- 3 → Three

Combined:

One Hundred Twenty Three

**Example 2:**

Input: 45

\\[ 45=40+5 \\]

Answer: Forty Five.

**Remember:** You need to understand ones, tens, hundreds, thousands and lakhs for larger numbers.

## **26. Decimal ↔ Binary / Octal / Hex Conversion**

**Definition:** Convert numbers from one number system to another.

There are four commonly used number systems:

| Number system | Base | Digits   |
| ------------- | ---- | -------- |
| Decimal       | 10   | 0–9      |
| Binary        | 2    | 0, 1     |
| Octal         | 8    | 0–7      |
| Hexadecimal   | 16   | 0–9, A–F |

**Example 1: Decimal to Binary**

Convert 10 into binary.

Divide by 2 repeatedly:

| Division | Remainder |
| -------- | --------- |
| 10 ÷ 2   | 0         |
| 5 ÷ 2    | 1         |
| 2 ÷ 2    | 0         |
| 1 ÷ 2    | 1         |

Read remainders from bottom to top.

10 = 1010 (Binary)

**Example 2: Binary to Decimal**

Convert 1010 into decimal.

\\[ 1\times2^3+0\times2^2+1\times2^1+0\times2^0 \\]

\\[ 8+0+2+0=10 \\]

1010 = 10 (Decimal)

**Example 3: Decimal to Octal**

\\[ 10=12_8 \\]

**Example 4: Decimal to Hexadecimal**

\\[ 10=A\_{16} \\]

## **27. Roman Number Conversion**

**Definition:** Convert a decimal number into Roman numerals or Roman numerals into decimal numbers.

Important Roman symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

**Example 1: 14 into Roman**

\\[ 14=10+4 \\]

10 = X

4 = IV

Answer:

14 = XIV

**Example 2: 25 into Roman**

\\[ 25=10+10+5 \\]

X + X + V = XXV.

**Example 3: Roman to Decimal**

\\[ XIV=10+4=14 \\]

# **Part 4: Advanced Number Programs**

## **28. Perfect Square / Perfect Cube Check**

**Perfect Square Definition:** A number is a perfect square if it can be written as an integer multiplied by itself.

**Example:** 25

\\[ 5\times5=25 \\]

25 is Perfect Square

Another example:

\\[ 36=6\times6 \\]

**Perfect Cube Definition:** A number is a perfect cube if it can be written as an integer multiplied by itself three times.

**Example:** 27

\\[ 3\times3\times3=27 \\]

27 is Perfect Cube

Another example:

\\[ 64=4\times4\times4 \\]

## **29. Count Trailing Zeros in Factorial**

**Definition:** Count how many zeros appear at the end of a factorial result.

**Example:** 5!

First calculate:

\\[ 5!=5\times4\times3\times2\times1=120 \\]

120 contains one trailing zero.

Answer = 1

**Another example: 10!**

\\[ 10!=3628800 \\]

It has 2 trailing zeros.

**Important mathematical formula:**

Instead of calculating the complete factorial, use:

\\[ Z=\left\lfloor\frac{n}{5}\right\rfloor+ \left\lfloor\frac{n}{25}\right\rfloor+ \left\lfloor\frac{n}{125}\right\rfloor+\cdots \\]

**Example: 100!**

\\[ Z=20+4=24 \\]

100! has 24 trailing zeros

## **30. Sieve of Eratosthenes**

**Definition:** An efficient method to find all prime numbers up to a given number by repeatedly eliminating multiples of prime numbers.

**Example: Find prime numbers from 1 to 20.**

Step 1: Write all numbers.

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20.

Step 2: Start with 2. Keep 2 and eliminate its multiples.

Remove: 4, 6, 8, 10, 12, 14, 16, 18, 20.

Step 3: Move to 3. Keep 3 and eliminate its remaining multiples.

Remove: 9, 15.

Step 4: Move to 5. Its multiples within 20 have already been removed or are outside the relevant checking range.

Step 5: Remaining numbers are prime.

Answer: 2, 3, 5, 7, 11, 13, 17, 19

# **Quick Revision – Which logic belongs to which program?**

This is the most important table to remember before coding.

| Logic / Operation   | Programs                                         |
| ------------------- | ------------------------------------------------ |
| Reverse digits      | Reverse, Palindrome, Sum of Digits, Count Digits |
| Factor checking     | Prime, Prime Range, Perfect, Prime Factorization |
| Factorial           | Strong, Krishnamurthy                            |
| Digit power         | Armstrong, Neon, Disarium                        |
| Digit sum           | Harshad, Spy, Magic, Happy                       |
| Multiplication      | Power, Spy, Factorial                            |
| Number system       | Binary, Octal, Hexadecimal, Roman                |
| Mathematical series | Fibonacci, Sieve of Eratosthenes                 |
| Square / Cube       | Perfect Square, Perfect Cube, Automorphic        |

# **Recommended Learning Order**

Don't try all 30 in one day. Follow this order:

## **Your 30-program checklist**

Your learning progress

**0/30 completed**

**Level 1 – Basic logic**

Reverse Number

Palindrome Number

Count Digits

Sum of Digits

**Level 2 – Factor logic**

Prime Number

Prime Numbers in Range

Perfect Number

Prime Factorization

GCD / HCF and LCM

**Level 3 – Digit mathematics**

Armstrong Number

Armstrong in Range

Strong Number

Automorphic Number

Neon Number

Harshad Number

Spy Number

Krishnamurthy Number

Disarium Number

Duck Number

Buzz Number

Happy Number

Magic Number

**Level 4 – Advanced logic**

Fibonacci Series

Check Fibonacci Number

Power Without pow

Number to Words

Number System Conversion

Roman Number Conversion

Perfect Square / Cube

Trailing Zeros in Factorial

Sieve of Eratosthenes

**My advice:** For every program, follow this process:

1. Understand the definition.
2. Solve the example manually.
3. Identify the mathematical operation.
4. Write Python code.
5. Dry run with a different input.
6. Try solving without looking at previous code.

This will help you develop your own coding logic instead of memorizing programs.
