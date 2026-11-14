# Logic Building Syllabus (Basic → Advanced)

> Language independent: practice in C / C++ / Java / Python / JavaScript.
> Rule: First draw the pattern on paper, find the relation between **row (i)**, **column (j)** and **n**, then code it.

---

## PART 1: STAR PATTERNS

### How to solve any pattern (5-step method)
1. Count the number of **rows**.
2. For each row, count **spaces**, **stars**, and **numbers/characters**.
3. Find the formula of each in terms of `i` and `n`.
4. Decide loops: 1 outer loop (rows) + inner loop(s) (spaces / stars).
5. Dry run for n = 1, 2, 3 and then submit.

---

### Category 1: Basic Patterns (Beginner)
Goal: understand nested loops.

| # | Pattern Name | Concept |
|---|--------------|---------|
| 1 | Square (solid) | `n x n` stars |
| 2 | Rectangle (solid) | rows x cols |
| 3 | Hollow Square | print star only on border |
| 4 | Hollow Rectangle | border condition |
| 5 | Single Row / Single Column | one loop |
| 6 | Left Half Pyramid (Right Triangle) | j <= i |
| 7 | Inverted Left Half Pyramid | j <= n-i+1 |
| 8 | Right Half Pyramid (mirrored) | spaces + stars |
| 9 | Inverted Right Half Pyramid | spaces + stars |

### Category 2: Triangle Patterns (Easy)
| # | Pattern Name | Concept |
|---|--------------|---------|
| 10 | Full Pyramid | spaces `n-i`, stars `2i-1` |
| 11 | Inverted Full Pyramid | reverse of above |
| 12 | Hollow Pyramid | stars on edges + base |
| 13 | Hollow Inverted Pyramid | edges + top row |
| 14 | Hollow Right Triangle | border only |
| 15 | Hollow Inverted Right Triangle | border only |
| 16 | Right Pascal Triangle (Mountain) | increase then decrease |
| 17 | Left Pascal Triangle | spaces + mountain |
| 18 | Equilateral Triangle (with space between stars) | `* * *` |
| 19 | Number-Star Mix Triangle | alternate `*` and number |

### Category 3: Diamond & Shape Patterns (Medium)
| # | Pattern Name | Concept |
|---|--------------|---------|
| 20 | Diamond (solid) | pyramid + inverted pyramid |
| 21 | Hollow Diamond | edge stars only |
| 22 | Half Diamond (right) | increase then decrease |
| 23 | Half Diamond (left) | spaces + stars |
| 24 | Butterfly Pattern | two triangles mirrored |
| 25 | Hourglass (solid) | inverted pyramid + pyramid |
| 26 | Hollow Hourglass | edges only |
| 27 | Sandglass / Bow-tie | combination |
| 28 | Parallelogram | shifting spaces |
| 29 | Rhombus (solid & hollow) | parallelogram variant |
| 30 | Arrow (right / left / up / down) | combination of triangle + stem |
| 31 | Plus (+) Pattern | row == mid OR col == mid |
| 32 | X Pattern / Cross | i == j OR i + j == n+1 |
| 33 | Hollow X | diagonal only |
| 34 | Letter patterns (A, E, F, H, I, K, L, M, N, O, P, S, T, U, V, W, X, Y, Z) | condition-based |
| 35 | Hexagon / Octagon (star) | multi-section |

### Category 4: Advanced Star Patterns (Hard)
| # | Pattern Name | Concept |
|---|--------------|---------|
| 36 | Spiral Star Pattern | boundary shrinking |
| 37 | Zig-Zag Pattern | `(i+j) % 4` conditions |
| 38 | Wave Pattern | sine-like row logic |
| 39 | Checkerboard (star/space) | `(i+j) % 2` |
| 40 | Concentric Squares | `min(i, j, n-i, n-j)` |
| 41 | Concentric Diamonds | distance from centre |
| 42 | Mirror / Symmetric Patterns | left half + right half |
| 43 | Heart Shape | math condition |
| 44 | Christmas Tree | stacked pyramids + trunk |
| 45 | Star Burst / Sun Pattern | multiple directions |
| 46 | Sierpinski Triangle (star) | recursion / bitwise `(i & j) == 0` |
| 47 | Pascal's Triangle (numbers, then star form) | nCr |
| 48 | Floyd's-style Star Triangle | continuous counting |
| 49 | Alphabet + Star Combined | char arithmetic |
| 50 | Window / Door / House Shapes | custom shapes |

---

### Related Number & Character Patterns (Do after stars)

**Basic**
- Number right triangle (1, 12, 123 ...)
- Same number triangle (1, 22, 333 ...)
- Reverse number triangle
- Floyd's Triangle
- Alphabet triangle (A, AB, ABC ...)
- Binary triangle (1, 01, 101 ...)

**Medium**
- Number pyramid (1 / 121 / 12321)
- Palindromic pyramid
- Diamond with numbers
- Butterfly with numbers
- Pascal's Triangle
- Zig-Zag number pattern

**Advanced**
- Spiral matrix pattern
- Diagonal number pattern
- Hollow number diamond
- Cyclic number pattern
- Fibonacci triangle
- Prime-number triangle

---

## PART 2: MOST ASKED INTERVIEW QUESTIONS (Category-wise)

### Category A: Basic Programming Logic (Must Know)
1. Swap two numbers (with and without 3rd variable)
2. Check even / odd
3. Largest of 2 / 3 numbers
4. Check leap year
5. Sum of N natural numbers
6. Factorial of a number
7. Multiplication table
8. Check positive / negative / zero
9. Simple and compound interest
10. Calculator using switch-case

### Category B: Number-Based Problems (Very High Frequency)
1. Reverse a number
2. Palindrome number
3. Count digits
4. Sum of digits
5. Armstrong number (and Armstrong in range)
6. Prime number check
7. Prime numbers in a range
8. Perfect number
9. Strong number
10. Automorphic number
11. Neon number
12. Harshad (Niven) number
13. Happy number
14. Magic number
15. Spy number
16. Krishnamurthy number
17. Disarium number
18. Duck number
19. Buzz number
20. GCD / HCF and LCM
21. Prime factorization
22. Fibonacci series (loop and recursion)
23. Check Fibonacci number
24. Power of a number (without pow)
25. Number to words conversion
26. Decimal ↔ Binary / Octal / Hex conversion
27. Roman number conversion
28. Perfect square / perfect cube check
29. Count trailing zeros in factorial
30. Sieve of Eratosthenes

### Category C: Pattern Problems (Very High in Fresher Interviews)
1. Right triangle star / number / alphabet
2. Pyramid and inverted pyramid
3. Diamond pattern
4. Hollow patterns
5. Floyd's Triangle
6. Pascal's Triangle
7. Butterfly pattern
8. Hourglass pattern
9. X / Plus patterns
10. Spiral pattern

### Category D: String Problems (Very High Frequency)
1. Reverse a string
2. Palindrome string
3. Count vowels and consonants
4. Count words in a sentence
5. Character frequency count
6. First non-repeating character
7. First repeating character
8. Remove duplicate characters
9. Remove vowels / spaces
10. Anagram check
11. Toggle case / swap case
12. Check pangram
13. Reverse words in a sentence
14. Reverse each word
15. Longest word in a sentence
16. Capitalize first letter of each word
17. Compare two strings (without built-in)
18. Substring search (pattern matching)
19. Count occurrences of a substring
20. String compression (`aaabb` → `a3b2`)
21. Check if string is rotation of another
22. Longest palindromic substring
23. Longest common prefix
24. Longest substring without repeating characters
25. Isomorphic strings
26. Valid parentheses
27. Remove all adjacent duplicates
28. Print all permutations of a string
29. Print all subsequences / substrings
30. Caesar cipher (encrypt / decrypt)

### Category E: Array Problems (Very High Frequency)
**Basic**
1. Find largest / smallest element
2. Second largest / second smallest
3. Sum and average of elements
4. Reverse an array
5. Count even / odd elements
6. Search an element (linear search)
7. Check if array is sorted
8. Copy one array to another
9. Merge two arrays
10. Insert / delete at a position

**Medium**
11. Remove duplicates from sorted / unsorted array
12. Find duplicate element
13. Find missing number in 1..N
14. Rotate array (left / right by k)
15. Move all zeros to end
16. Separate even and odd numbers
17. Segregate 0s, 1s and 2s (Dutch National Flag)
18. Leaders in an array
19. Array intersection and union
20. Frequency of each element
21. Two Sum problem
22. Kadane's Algorithm (maximum subarray sum)
23. Find majority element (Moore's voting)
24. Equilibrium index
25. Prefix sum and suffix sum
26. Pair with given sum / difference
27. Product of array except self
28. Sort array of 0s and 1s

**Advanced**
29. Trapping rain water
30. Maximum product subarray
31. Merge intervals
32. Next greater element
33. Next permutation
34. Subarray with given sum
35. Longest consecutive sequence
36. Count inversions
37. Sliding window maximum
38. 3Sum / 4Sum
39. Stock buy-sell (max profit)
40. Container with most water

### Category F: 2D Array / Matrix Problems
1. Print matrix (row-wise / column-wise)
2. Sum of rows, columns, diagonals
3. Transpose of a matrix
4. Matrix addition / subtraction / multiplication
5. Check symmetric matrix
6. Check identity / sparse / diagonal matrix
7. Upper and lower triangular matrix
8. Rotate matrix by 90°
9. Spiral traversal
10. Boundary traversal
11. Diagonal traversal
12. Search in a sorted matrix
13. Set matrix zeroes
14. Saddle point
15. Pascal's Triangle (matrix form)
16. Magic square
17. Sudoku validator
18. Maximum sum rectangle (advanced)

### Category G: Searching & Sorting
**Searching:** Linear search, Binary search (iterative + recursive), first / last occurrence, search in rotated array, peak element, square root using binary search.

**Sorting (write logic, not just call sort):**
Bubble, Selection, Insertion, Merge, Quick, Heap, Counting sort. Also: sort by frequency, sort strings, custom comparator, k-th largest element.

### Category H: Recursion Problems
1. Factorial, Fibonacci
2. Sum of digits / reverse number
3. Power of a number
4. Palindrome check
5. GCD
6. Print 1 to N and N to 1
7. Tower of Hanoi
8. Binary search (recursive)
9. Generate all subsets
10. Generate all permutations
11. N-Queens
12. Sudoku solver
13. Rat in a maze
14. Subset sum
15. Combination sum

### Category I: Basic Maths & Logical Puzzles
1. Check if number is power of 2
2. Count set bits
3. Swap using XOR
4. Find single non-repeating number (XOR)
5. Find two missing numbers
6. Number of trailing zeros
7. Reverse bits
8. Gray code
9. Pythagorean triplets
10. Collatz sequence
11. Sum of series (1 + 1/2 + 1/3 ..., x^n/n!)
12. Perfect-square series
13. Print all divisors / factors

### Category J: Intermediate / Advanced Logic Topics
- **Two pointer technique**
- **Sliding window**
- **Hashing (HashMap / HashSet) problems**
- **Stack problems:** valid parentheses, next greater element, min stack, evaluate postfix
- **Queue problems:** queue using stack, circular queue
- **Linked list:** reverse, detect cycle, middle element, merge two lists, palindrome list
- **Bit manipulation**
- **Greedy:** activity selection, coin change (greedy), fractional knapsack
- **Basic Dynamic Programming:** Fibonacci, climbing stairs, coin change, 0/1 knapsack, LCS, LIS, minimum path sum
- **Backtracking:** subsets, permutations, N-Queens
- **Basic Trees / Graphs:** traversals, BFS, DFS, height of tree

---

## PART 3: PRACTICE ROADMAP

| Week | Topics |
|------|--------|
| 1 | Basic programming + star patterns (Category 1 and 2) |
| 2 | Star patterns (Category 3 and 4) + number patterns |
| 3 | Number-based problems (Armstrong, prime, palindrome, etc.) |
| 4 | Strings |
| 5 | Arrays (basic + medium) |
| 6 | Matrix + searching + sorting |
| 7 | Recursion + bit manipulation |
| 8 | Arrays advanced + two pointers + sliding window + hashing |
| 9 | Stack, queue, linked list |
| 10 | Greedy, backtracking, basic DP + mock interviews |

---

## PART 4: INTERVIEW TIPS
- Always explain your approach **before** coding.
- Start with brute force, then optimize.
- State **time complexity** and **space complexity**.
- Handle edge cases: empty input, single element, negative numbers, duplicates, overflow.
- Dry run your code with a sample input.
- Write clean variable names.

---

## Progress Tracker

- [ ] Basic Star Patterns
- [ ] Triangle Patterns
- [ ] Diamond and Shape Patterns
- [ ] Advanced Star Patterns
- [ ] Number and Character Patterns
- [ ] Basic Programming Logic
- [ ] Number-Based Problems
- [ ] Strings
- [ ] Arrays
- [ ] 2D Arrays / Matrix
- [ ] Searching and Sorting
- [ ] Recursion
- [ ] Bit Manipulation / Maths
- [ ] Advanced Topics (Stack, Queue, LL, DP, Greedy, Backtracking)
