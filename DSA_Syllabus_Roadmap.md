# DSA Syllabus and Roadmap (Beginner → Advanced)

> Goal: understand each data structure and algorithm **visually**, know the **brute force** and the **optimal** way, then practice by difficulty.
> Language independent. Practice in Python / C++ / Java. Problem names follow common platforms (LeetCode, GFG, Codeforces style).

---

## 0. Roadmap at a Glance

```
PHASE 1  Foundations        PHASE 2  Core Structures      PHASE 3  Core Algorithms
-----------------------     -------------------------     --------------------------
1 Complexity (Big-O)        7  Linked List                11 Recursion
2 Arrays                    8  Stack                      12 Backtracking
3 Strings                   9  Queue / Deque              13 Greedy
4 Hashing                   10 Heap / Priority Queue      14 Dynamic Programming
5 Two Pointers / Window                                   15 Bit Manipulation
6 Sorting + Binary Search

PHASE 4  Non-Linear          PHASE 5  Advanced
-----------------------     -------------------------
16 Binary Tree               20 Union-Find (DSU)
17 Binary Search Tree        21 Trie
18 Graph (BFS / DFS)         22 Segment Tree / Fenwick
19 Shortest Path / MST       23 Advanced patterns + mock interviews
```

| Phase | Weeks | Topics | Target problems |
|-------|-------|--------|-----------------|
| 1 | 1 to 4 | Big-O, Arrays, Strings, Hashing, Two Pointers, Sliding Window, Prefix Sum, Sorting, Binary Search | 80 |
| 2 | 5 to 7 | Linked List, Stack, Queue, Heap | 60 |
| 3 | 8 to 11 | Recursion, Backtracking, Greedy, DP, Bits | 90 |
| 4 | 12 to 14 | Trees, BST, Graphs, Shortest Path | 70 |
| 5 | 15 to 16 | DSU, Trie, Segment Tree, revision, mocks | 50 |

### How to study every topic (the 6-step loop)
1. **Read** the definition and draw the structure on paper.
2. **Implement** it from scratch (no library).
3. **Solve** 3 easy → 3 medium → 1 hard problem.
4. For every problem write the **brute force first**, then improve to **optimal**.
5. Write time and space complexity for each solution.
6. **Revise** after 3 days and after 7 days (spaced repetition).

### Problem solving template
```
Understand  -> restate the problem, write 2 examples + 1 edge case
Brute force -> simplest correct idea, state its complexity
Optimize    -> find the bottleneck, ask: "which data structure removes it?"
Code        -> clean names, small functions
Test        -> empty input, one element, duplicates, negatives, large input
```

---

# PHASE 1: FOUNDATIONS

## 1. Time and Space Complexity (Big-O)

**Definition:** Big-O describes how the running time (or memory) of an algorithm **grows** as the input size `n` grows. It ignores constants and small terms.

**Visual: growth rate**
```
operations
   ^
   |                                              n!   2^n
   |                                          .  /   /
   |                                       . /  /   /
   |                                n^2 ./  /  /
   |                           . '  /  /
   |                     n log n . '
   |         ________________.' ----------------- n
   |  ==================================================== log n
   |  ---------------------------------------------------- 1
   +-----------------------------------------------------------> n
```

| Big-O | Name | n = 1000 roughly | Example |
|-------|------|------------------|---------|
| O(1) | Constant | 1 | array index, hash lookup |
| O(log n) | Logarithmic | 10 | binary search |
| O(n) | Linear | 1,000 | single loop |
| O(n log n) | Linearithmic | 10,000 | merge sort |
| O(n²) | Quadratic | 1,000,000 | nested loops |
| O(2ⁿ) | Exponential | huge | all subsets |
| O(n!) | Factorial | huge | all permutations |

**How it works (counting steps)**
```python
for i in range(n):          # runs n times
    for j in range(n):      # runs n times for each i
        print(i, j)         # total n * n = O(n^2)
```
- Drop constants: `3n + 5` → **O(n)**.
- Keep the biggest term: `n² + n` → **O(n²)**.
- Sequential loops **add**, nested loops **multiply**.
- Halving the problem each step gives **O(log n)**.

**Real-world examples**
- Searching a name in an unsorted contact list: O(n). In a sorted phone book (flip to middle): O(log n).
- Checking every pair of friends on a social app: O(n²), which is why big apps avoid it.

**Rule of thumb (1 second ≈ 10⁸ simple operations):**

| n up to | Aim for |
|---------|---------|
| 10 | O(n!) |
| 20 | O(2ⁿ) |
| 500 | O(n³) |
| 5,000 | O(n²) |
| 10⁶ | O(n log n) or O(n) |
| 10⁹+ | O(log n) or O(1) |

**Related concepts:** best / average / worst case, amortized analysis (dynamic array append is O(1) amortized), space complexity, recursion stack space, Ω (lower bound) and Θ (tight bound).

**Practice**
- **Easy:** find complexity of 10 small code snippets; Fibonacci iterative vs recursive comparison.
- **Medium:** analyse `for (i=1; i<n; i*=2)`, nested loops with dependent bounds (`j<i`), recursion `T(n)=2T(n/2)+n`.
- **Hard:** amortized analysis of dynamic array resizing; solve recurrences with the Master theorem.

---

## 2. Arrays

**Definition:** A collection of elements stored in **contiguous memory**, accessed by index.

**Visual**
```
index:    0     1     2     3     4
        +-----+-----+-----+-----+-----+
 a  =   |  10 |  20 |  30 |  40 |  50 |
        +-----+-----+-----+-----+-----+
address: 100   104   108   112   116        (int = 4 bytes)

a[3] -> address = base + 3 * 4 = 112   => O(1) access
```

**How it works**
| Operation | Cost | Why |
|-----------|------|-----|
| Access `a[i]` | O(1) | address formula |
| Search (unsorted) | O(n) | check each |
| Insert / delete in middle | O(n) | shift elements |
| Append at end | O(1) amortized | dynamic array doubles capacity |

```
Insert 25 at index 2:
before: [10, 20, 30, 40, 50]
shift : [10, 20, __, 30, 40, 50]    <- everything after index 2 moves right
after : [10, 20, 25, 30, 40, 50]
```

**Real-world examples:** pixel rows in an image, marks of students in a class, a playlist stored in order, spreadsheet columns.

**Brute force vs optimal**
| Problem | Brute force | Optimal |
|---------|-------------|---------|
| Max subarray sum | all subarrays O(n²) | Kadane's O(n) |
| Two Sum | two loops O(n²) | hash map O(n) |
| Missing number | sort O(n log n) | sum formula / XOR O(n) |
| Rotate array | rotate one by one O(n·k) | reversal trick O(n), O(1) space |

**Related concepts:** 2D arrays (matrix), dynamic arrays (vector / ArrayList), in-place operations, prefix / suffix arrays, Dutch National Flag.

**Practice**
- **Easy:** Two Sum, Best Time to Buy and Sell Stock, Move Zeroes, Remove Duplicates from Sorted Array, Missing Number, Single Number, Merge Sorted Array, Contains Duplicate.
- **Medium:** Maximum Subarray (Kadane), Product of Array Except Self, Rotate Array, Sort Colors, Next Permutation, Merge Intervals, 3Sum, Container With Most Water, Spiral Matrix, Set Matrix Zeroes.
- **Hard:** Trapping Rain Water, First Missing Positive, Maximum Product Subarray, Count of Smaller Numbers After Self, Median of Two Sorted Arrays.

---

## 3. Strings

**Definition:** A sequence of characters, usually stored as an array of characters (immutable in Python / Java).

**Visual**
```
 s = "hello"
 index:  0   1   2   3   4
       +---+---+---+---+---+
       | h | e | l | l | o |
       +---+---+---+---+---+
 ASCII: 104 101 108 108 111      'a'=97  'A'=65  '0'=48
```

**How it works:** most string problems use one of these tools:
```
 Frequency array  -> count letters in int[26]
 Two pointers     -> palindrome, reverse
 Sliding window   -> longest substring with a condition
 Hashing          -> anagram groups
 Stack            -> valid parentheses
 KMP / Z / Rabin-Karp -> fast pattern search
```
Immutable strings: `s += c` inside a loop costs O(n²). Use a list and `join` instead.

**Real-world examples:** search bar and autocomplete, spell checkers, DNA matching, plagiarism detection, text editors (find and replace).

**Brute force vs optimal**
| Problem | Brute force | Optimal |
|---------|-------------|---------|
| Substring search | compare at every index O(n·m) | KMP O(n + m) |
| Longest substring without repeat | all substrings O(n³) | sliding window + map O(n) |
| Anagram check | sort both O(n log n) | frequency count O(n) |
| Longest palindromic substring | check all O(n³) | expand around centre O(n²), Manacher O(n) |

**Related concepts:** ASCII / Unicode, string builder, rolling hash, suffix array, edit distance (see DP).

**Practice**
- **Easy:** Reverse String, Valid Palindrome, Valid Anagram, First Unique Character, Longest Common Prefix, Roman to Integer, Implement strStr.
- **Medium:** Longest Substring Without Repeating Characters, Group Anagrams, Longest Palindromic Substring, String to Integer (atoi), Generate Parentheses, Decode String, Minimum Window Substring (sliding window), Longest Repeating Character Replacement.
- **Hard:** Edit Distance, Regular Expression Matching, Wildcard Matching, Shortest Palindrome (KMP), Longest Valid Parentheses.

---

## 4. Hashing (HashMap / HashSet)

**Definition:** A structure that maps a **key** to a **value** using a **hash function** that converts the key into an array index. Gives average O(1) insert, delete and lookup.

**Visual**
```
 key "apple" --hash()--> 7      table size 10
 key "mango" --hash()--> 3
 key "grape" --hash()--> 7      <- COLLISION with apple

 index   bucket
   0
   3     -> ("mango", 40)
   7     -> ("apple", 50) -> ("grape", 90)     <- chaining (linked list)
   9
```

**How it works**
1. Compute `index = hash(key) % table_size`.
2. Store / fetch at that bucket.
3. **Collision:** two keys land in the same bucket. Fix by chaining (list per bucket) or open addressing (probe next slot).
4. When load factor passes about 0.75, the table **resizes** and rehashes.

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert / Search / Delete | O(1) | O(n) |

**Real-world examples:** login system (username → user record), caching (URL → page), spell dictionary, counting word frequency, database indexes, deduplication.

**Brute force vs optimal**
| Problem | Brute force | Optimal |
|---------|-------------|---------|
| Two Sum | nested loops O(n²) | store `target - x` in map O(n) |
| Find duplicate | compare all O(n²) | HashSet O(n) |
| Subarray sum = K | all subarrays O(n²) | prefix sum + map O(n) |
| Longest consecutive sequence | sort O(n log n) | HashSet, start only at sequence starts O(n) |

**Related concepts:** hash function quality, load factor, chaining vs open addressing, HashSet vs HashMap, Counter, ordered map (tree based, O(log n)).

**Practice**
- **Easy:** Two Sum, Contains Duplicate, Valid Anagram, Intersection of Two Arrays, Happy Number, Isomorphic Strings, Ransom Note.
- **Medium:** Group Anagrams, Top K Frequent Elements, Subarray Sum Equals K, Longest Consecutive Sequence, 4Sum II, Longest Substring Without Repeating Characters, LRU Cache (HashMap + doubly linked list).
- **Hard:** Max Points on a Line, Substring with Concatenation of All Words, All O(1) Data Structure, Longest Duplicate Substring (rolling hash).

---

## 5. Two Pointers and Sliding Window

### 5A. Two Pointers

**Definition:** Use two indexes that move through the data (usually a sorted array or a string) to avoid a nested loop.

**Visual (pair with target sum 9 in sorted array)**
```
 [ 1, 2, 4, 7, 11, 15 ]  target = 9
   L                R      1 + 15 = 16 > 9  -> move R left
   L            R          1 + 11 = 12 > 9  -> move R left
   L         R             1 +  7 =  8 < 9  -> move L right
      L      R             2 +  7 =  9  FOUND
```

**How it works:** patterns are (1) **opposite ends** moving inward, (2) **fast and slow** moving in the same direction, (3) **read and write** pointer to modify in place.

**Real-world examples:** merging two sorted playlists, finding two items whose prices fit a gift card, removing duplicate entries from a sorted log.

**Brute force vs optimal:** checking every pair O(n²) → sorted + two pointers O(n).

### 5B. Sliding Window

**Definition:** Keep a contiguous **window** `[left, right]` and slide it, updating the answer incrementally instead of recomputing.

**Visual (max sum of window size 3)**
```
 a = [2, 1, 5, 1, 3, 2]
      [2  1  5] = 8
         [1  5  1] = 7       remove 2, add 1
            [5  1  3] = 9    remove 1, add 3   <- max
               [1  3  2] = 6
```

| Type | Idea |
|------|------|
| Fixed size | add new right element, drop old left element |
| Variable size | expand right; while invalid, shrink left |

**Real-world examples:** moving average of stock prices, network traffic in the last 60 seconds, "last 7 days" analytics, rate limiting.

**Brute force vs optimal:** recompute each window O(n·k) → slide with add / remove O(n).

**Related concepts:** prefix sum, monotonic deque, fast and slow pointers (cycle detection), Dutch National Flag, hashing inside a window.

**Practice**
- **Easy:** Valid Palindrome, Merge Sorted Array, Remove Duplicates from Sorted Array, Squares of a Sorted Array, Maximum Average Subarray I, Best Time to Buy and Sell Stock.
- **Medium:** 3Sum, Container With Most Water, Sort Colors, Longest Substring Without Repeating Characters, Permutation in String, Fruit Into Baskets, Longest Repeating Character Replacement, Max Consecutive Ones III, Minimum Size Subarray Sum.
- **Hard:** Trapping Rain Water, Minimum Window Substring, Sliding Window Maximum (monotonic deque), Substring with Concatenation of All Words, Longest Substring with At Most K Distinct Characters.

---

## 6. Prefix Sum and Difference Array

**Definition:** Pre-compute running totals so any range sum is answered in O(1).

**Visual**
```
 a      = [ 3,  1,  4,  2,  5 ]
 prefix = [ 3,  4,  8, 10, 15 ]      prefix[i] = a[0] + ... + a[i]

 sum of a[1..3] = prefix[3] - prefix[0] = 10 - 3 = 7      (1 + 4 + 2)
```

**How it works:** build once in O(n), answer each query in O(1). **Difference array** is the reverse: apply "add x to range [l, r]" in O(1) by `d[l] += x; d[r+1] -= x`, then rebuild with a prefix sum.

**Real-world examples:** total sales between two dates, cumulative score boards, image blur filters, booking overlaps.

**Brute force vs optimal:** q queries x O(n) each → O(n + q).

**Related concepts:** 2D prefix sum, prefix XOR, prefix + hashmap (subarray sum = K), Fenwick tree for updates.

**Practice**
- **Easy:** Running Sum of 1D Array, Range Sum Query Immutable, Find Pivot Index, Number of Ways to Split Array.
- **Medium:** Subarray Sum Equals K, Continuous Subarray Sum, Product of Array Except Self, Range Sum Query 2D, Corporate Flight Bookings (difference array), Car Pooling.
- **Hard:** Maximum Sum of 3 Non-Overlapping Subarrays, Count of Range Sum, Shortest Subarray with Sum at Least K.

---

## 7. Sorting

**Definition:** Arranging elements in a defined order (ascending or descending).

**Visual: Merge Sort (divide, sort, merge)**
```
              [38, 27, 43, 3]
              /              \
        [38, 27]            [43, 3]
        /     \             /     \
     [38]    [27]        [43]     [3]
        \     /             \     /
        [27, 38]            [3, 43]
              \              /
             [3, 27, 38, 43]
```

**How the main sorts work**
| Algorithm | Idea | Best | Average | Worst | Space | Stable |
|-----------|------|------|---------|-------|-------|--------|
| Bubble | swap adjacent out-of-order pairs | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | pick the minimum, place at front | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | insert each item into sorted left part | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | split, sort halves, merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | pivot partition | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | build max-heap, extract | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting | count each value | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix | sort digit by digit | O(d(n + k)) | | | O(n + k) | Yes |

```
Quick sort partition (pivot = 4):
 [7, 2, 9, 4, 1]  ->  [2, 1] 4 [7, 9]
                       < pivot   > pivot      then sort both sides
```

**Real-world examples:** leaderboards, sorting products by price, calendar events by time, database ORDER BY, merging sorted logs.

**Brute force vs optimal:** O(n²) simple sorts are fine for small n; use O(n log n) in general; use counting / radix when values lie in a small range.

**Related concepts:** stable vs unstable, in-place, comparison-based lower bound Ω(n log n), custom comparators, `k`-th element with quickselect (average O(n)), merge step reused for counting inversions.

**Practice**
- **Easy:** Sort an Array (implement 3 sorts), Merge Sorted Array, Valid Anagram (sort method), Squares of a Sorted Array, Relative Sort Array, Height Checker.
- **Medium:** Sort Colors, Merge Intervals, Kth Largest Element (quickselect), Top K Frequent Elements, Sort Characters by Frequency, Largest Number, Meeting Rooms II, Insert Interval.
- **Hard:** Count of Smaller Numbers After Self, Reverse Pairs, Maximum Gap (radix / bucket), Count Inversions, Median of Two Sorted Arrays.

---

## 8. Binary Search

**Definition:** Search in a **sorted** (or monotonic) space by repeatedly halving the range. O(log n).

**Visual: find 23**
```
 idx:  0   1   2   3    4    5    6    7
 a  = [2,  5,  8, 12,  16,  23,  38,  56]
       L              M                R       mid=4 -> 16 < 23 -> go right
                           L    M       R      mid=6 -> 38 > 23 -> go left
                           L,M,R               mid=5 -> 23  FOUND
```

**How it works**
```python
lo, hi = 0, n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2         # avoids overflow
    if a[mid] == key:   return mid
    elif a[mid] < key:  lo = mid + 1
    else:               hi = mid - 1
```
**Binary search on the answer:** if you can write a yes/no function `feasible(x)` that is monotonic (all NO then all YES), binary search the smallest YES.
```
 x:         1  2  3  4  5  6  7  8
 feasible:  N  N  N  N  Y  Y  Y  Y      -> answer = 5
```

**Real-world examples:** dictionary lookup, `git bisect` to find the bad commit, finding a version number where a bug started, guessing games, searching a sorted database index.

**Brute force vs optimal:** linear scan O(n) → binary search O(log n). Minimum capacity / speed problems: try every value O(n·m) → binary search on answer O(n log m).

**Related concepts:** lower bound / upper bound, rotated array search, peak element, search in 2D matrix, ternary search, bisect module.

**Practice**
- **Easy:** Binary Search, Search Insert Position, Sqrt(x), First Bad Version, Valid Perfect Square, Guess Number Higher or Lower.
- **Medium:** Find First and Last Position, Search in Rotated Sorted Array, Find Peak Element, Search a 2D Matrix, Koko Eating Bananas, Capacity to Ship Packages, Find Minimum in Rotated Sorted Array, Time Based Key-Value Store.
- **Hard:** Median of Two Sorted Arrays, Split Array Largest Sum, Aggressive Cows / Painter's Partition, Kth Smallest Number in Multiplication Table, Find in Mountain Array.

---

# PHASE 2: CORE LINEAR STRUCTURES

## 9. Linked List

**Definition:** A chain of **nodes**; each node holds data and a pointer to the next node. Memory is not contiguous.

**Visual**
```
 Singly:   head
            |
            v
         +----+---+    +----+---+    +----+------+
         | 10 | o-+--> | 20 | o-+--> | 30 | null |
         +----+---+    +----+---+    +----+------+

 Doubly:   null <-- [10] <--> [20] <--> [30] --> null

 Circular: [10] -> [20] -> [30] -+
             ^-------------------+
```

**How it works**
| Operation | Singly linked list | Array |
|-----------|--------------------|-------|
| Access by index | O(n) | O(1) |
| Insert / delete at head | O(1) | O(n) |
| Insert after a known node | O(1) | O(n) |
| Search | O(n) | O(n) |

```
Reverse a list (3 pointers: prev, curr, next):
 null  1 -> 2 -> 3          step 1: 1 -> null
 prev  curr                 step 2: 2 -> 1 -> null
                            step 3: 3 -> 2 -> 1 -> null
```

**Real-world examples:** browser back / forward history (doubly), music playlist "next / previous", undo history, memory allocators, LRU cache.

**Brute force vs optimal**
| Problem | Brute force | Optimal |
|---------|-------------|---------|
| Middle of list | count length, walk again O(n) | slow and fast pointer, one pass |
| Detect cycle | store visited nodes O(n) space | Floyd's tortoise and hare O(1) space |
| Nth node from end | two passes | two pointers n apart, one pass |
| Merge k sorted lists | merge one by one O(nk) | min-heap O(N log k) |

**Related concepts:** dummy / sentinel node, fast and slow pointers, in-place reversal, doubly linked list, skip list.

**Practice**
- **Easy:** Reverse Linked List, Middle of the Linked List, Merge Two Sorted Lists, Linked List Cycle, Palindrome Linked List, Remove Duplicates from Sorted List, Intersection of Two Linked Lists.
- **Medium:** Remove Nth Node From End, Add Two Numbers, Reorder List, Linked List Cycle II, Sort List (merge sort), Copy List with Random Pointer, Odd Even Linked List, Swap Nodes in Pairs.
- **Hard:** Reverse Nodes in k-Group, Merge k Sorted Lists, LRU Cache, Flatten a Multilevel Doubly Linked List.

---

## 10. Stack

**Definition:** A **LIFO** (Last In, First Out) structure. You can only push and pop at the top.

**Visual**
```
   push(10) push(20) push(30)        pop() -> 30

                         | 30 | <- top        | 20 | <- top
            | 20 | <- top | 20 |              | 10 |
   | 10 |    | 10 |       | 10 |              +----+
   +----+    +----+       +----+
```

**How it works:** push, pop, peek are all O(1). Used when the **most recent** item matters first.

**Monotonic stack** (keeps elements in increasing or decreasing order) solves "next greater element" in O(n):
```
 a = [4, 5, 2, 25]
 4  -> stack [4]
 5  -> pop 4 (next greater of 4 is 5), stack [5]
 2  -> stack [5, 2]
 25 -> pop 2, pop 5 (both get 25), stack [25]
```

**Real-world examples:** undo / redo in editors, browser back button, function call stack, bracket matching in compilers, expression evaluation.

**Brute force vs optimal:** next greater element: for each element scan right O(n²) → monotonic stack O(n). Valid parentheses: repeated string replace O(n²) → stack O(n).

**Related concepts:** call stack and recursion, postfix / infix conversion, monotonic stack, min stack, stack using queues.

**Practice**
- **Easy:** Valid Parentheses, Implement Stack using Queues, Min Stack, Baseball Game, Next Greater Element I, Remove All Adjacent Duplicates.
- **Medium:** Daily Temperatures, Evaluate Reverse Polish Notation, Decode String, Next Greater Element II, Asteroid Collision, Remove K Digits, Online Stock Span, Simplify Path.
- **Hard:** Largest Rectangle in Histogram, Maximal Rectangle, Trapping Rain Water (stack approach), Basic Calculator, Longest Valid Parentheses.

---

## 11. Queue and Deque

**Definition:** A **FIFO** (First In, First Out) structure: add at the rear, remove from the front. A **deque** allows insert and delete at both ends.

**Visual**
```
 enqueue ->  rear                          front  -> dequeue
            +----+----+----+----+
            | 40 | 30 | 20 | 10 |
            +----+----+----+----+

 Circular queue (array of size 5, reuses freed slots):
        [ 6 ][ 7 ][ _ ][ 4 ][ 5 ]      front=3, rear=1, indexes wrap with % size
```

**How it works:** enqueue and dequeue are O(1). Variants: circular queue, **priority queue** (see Heap), **monotonic deque** (keeps window maximum).

**Real-world examples:** printer jobs, customer support ticket line, CPU task scheduling (round robin), BFS traversal, message queues (Kafka, RabbitMQ).

**Brute force vs optimal:** Sliding window maximum: scan each window O(n·k) → monotonic deque O(n).

**Related concepts:** BFS, level order traversal, circular buffer, producer-consumer problem, two stacks to build a queue.

**Practice**
- **Easy:** Implement Queue using Stacks, Implement Stack using Queues, Number of Recent Calls, Moving Average from Data Stream, Design Circular Queue.
- **Medium:** Rotting Oranges, Binary Tree Level Order Traversal, Perfect Squares (BFS), Open the Lock, Design Circular Deque, Task Scheduler.
- **Hard:** Sliding Window Maximum, Shortest Subarray with Sum at Least K, Word Ladder II, Constrained Subsequence Sum.

---

## 12. Heap / Priority Queue

**Definition:** A complete binary tree where each parent is ≤ its children (**min-heap**) or ≥ its children (**max-heap**). The top is always the min (or max).

**Visual: min-heap and its array**
```
          1
        /   \
       3     2              array: [1, 3, 2, 7, 4, 5]
      / \   /               index :  0  1  2  3  4  5
     7   4 5
 parent(i) = (i-1)//2     left(i) = 2i+1     right(i) = 2i+2
```

**How it works**
| Operation | Cost | Steps |
|-----------|------|-------|
| Peek min | O(1) | read root |
| Insert | O(log n) | add at end, **bubble up** |
| Extract min | O(log n) | move last to root, **bubble down** |
| Build heap from array | O(n) | heapify from the middle backwards |

```
Insert 0 into [1, 3, 2, 7, 4, 5]:   add at end -> compare with parent -> swap up to root.
```

**Real-world examples:** hospital emergency queue (priority), OS process scheduler, "top 10 trending" feed, Dijkstra's shortest path, merging sorted log files.

**Brute force vs optimal**
| Problem | Brute force | Optimal |
|---------|-------------|---------|
| K-th largest | sort O(n log n) | min-heap of size k O(n log k) |
| Merge k sorted lists | collect + sort O(N log N) | heap of k heads O(N log k) |
| Running median | sort each time O(n² log n) | two heaps (max-heap + min-heap) O(log n) per insert |

**Related concepts:** heapify, heap sort, top-K pattern, two-heap pattern, indexed priority queue, Fibonacci heap (theory).

**Practice**
- **Easy:** Kth Largest Element in a Stream, Last Stone Weight, Relative Ranks, Minimum Cost to Connect Sticks.
- **Medium:** Kth Largest Element in an Array, Top K Frequent Elements, K Closest Points to Origin, Task Scheduler, Reorganize String, Merge k Sorted Lists, Find K Pairs with Smallest Sums, Meeting Rooms II.
- **Hard:** Find Median from Data Stream, Sliding Window Median, Merge k Sorted Lists (heap), IPO, Smallest Range Covering Elements from K Lists.

---

# PHASE 3: CORE ALGORITHMIC TECHNIQUES

## 13. Recursion

**Definition:** A function that solves a problem by calling **itself** on a smaller input until it reaches a **base case**.

**Visual: factorial(3) on the call stack**
```
 fact(3)  = 3 * fact(2)
              fact(2) = 2 * fact(1)
                          fact(1) = 1            <- base case
                        returns 1
                      returns 2 * 1 = 2
            returns 3 * 2 = 6

 call stack:   | fact(1) |   grows downwards, then unwinds
               | fact(2) |
               | fact(3) |
```

**How it works:** every recursion needs (1) a **base case**, (2) a **smaller subproblem**, (3) a **combine** step. Time = (number of calls) x (work per call).

**Real-world examples:** folders inside folders (file explorer), family tree, fractals, parsing nested JSON, divide and conquer in search engines.

**Brute force vs optimal:** plain recursive Fibonacci repeats work, O(2ⁿ). Add **memoization** (store results) → O(n). That is the bridge to Dynamic Programming.
```
 fib(5)
  /    \
fib(4) fib(3)       fib(3) is computed twice (and more below). Cache it!
```

**Related concepts:** tail recursion, stack overflow, memoization, divide and conquer, recursion to iteration with an explicit stack, recurrence relations.

**Practice**
- **Easy:** Fibonacci, Power of Two, Reverse String (recursive), Sum of Digits, Climbing Stairs, Pow(x, n), Palindrome check.
- **Medium:** Pow(x, n) fast power, Generate Parentheses, Subsets, Permutations, Letter Combinations of a Phone Number, Merge Sort / Quick Sort, Tower of Hanoi.
- **Hard:** N-Queens, Sudoku Solver, Expression Add Operators, Word Search II, Regular Expression Matching.

---

## 14. Backtracking

**Definition:** Build a solution step by step; if a choice leads to a dead end, **undo it** (backtrack) and try the next choice. It is recursion + "choose, explore, un-choose".

**Visual: subsets of [1, 2, 3] (include or exclude each)**
```
                        []
              /                   \
          [1]                      []
         /    \                  /    \
     [1,2]    [1]            [2]       []
     /   \    /  \          /   \     /  \
 [1,2,3] [1,2] [1,3] [1] [2,3] [2]  [3]  []     <- 8 subsets
```

**How it works (template)**
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:]); return
    for c in choices:
        if not valid(c): continue      # PRUNING: skip bad branches early
        path.append(c)                 # choose
        backtrack(path, next_choices)  # explore
        path.pop()                     # un-choose
```

**Real-world examples:** Sudoku and crossword solvers, route / schedule planning with constraints, password cracking, puzzle games (maze, N-Queens), chess engines.

**Brute force vs optimal:** brute force tries every full combination. Backtracking **prunes** invalid partial solutions early (for example, two queens attacking), cutting the search a lot even though the worst case stays exponential.

**Related concepts:** state space tree, pruning, bitmask optimisation, constraint propagation, branch and bound, memoised backtracking = DP.

**Practice**
- **Easy:** Binary Watch, Letter Case Permutation, Generate all binary strings, Subsets (iterative), Path Sum II.
- **Medium:** Subsets, Subsets II, Permutations, Permutations II, Combination Sum, Combination Sum II, Palindrome Partitioning, Word Search, Generate Parentheses, Letter Combinations.
- **Hard:** N-Queens, Sudoku Solver, Word Search II, Expression Add Operators, Partition to K Equal Sum Subsets, Remove Invalid Parentheses.

---

## 15. Greedy

**Definition:** At every step pick the **locally best** option hoping it leads to the global best. Works only when the problem has the **greedy-choice property** and **optimal substructure**.

**Visual: Activity selection (pick the most non-overlapping meetings)**
```
 time ->  1  2  3  4  5  6  7  8  9
 A        [-----]
 B           [-----]
 C                 [-----]
 D              [--------]
 E                       [-----]
 Sort by END time. Pick A (ends 3), skip B, pick C (starts 4), pick E (starts 7)... => A, C, E
```

**How it works:** (1) decide a sort order or a priority, (2) walk through items and take the best valid one, (3) **prove** it works (exchange argument) or test against brute force.

**Real-world examples:** giving change with fewest coins (standard currency), scheduling meetings in a room, Huffman coding for file compression, loading a truck by value / weight, routing (Dijkstra).

**Brute force vs optimal:** trying all subsets of meetings O(2ⁿ) → sort by end time + one pass O(n log n).

**Caution:** greedy is NOT always right. Coin change with coins {1, 3, 4} and amount 6: greedy gives 4+1+1 (3 coins) but optimal is 3+3 (2 coins) → needs DP.

**Related concepts:** exchange argument, interval scheduling, Huffman coding, fractional knapsack (greedy) vs 0/1 knapsack (DP), Kruskal and Prim (MST).

**Practice**
- **Easy:** Assign Cookies, Best Time to Buy and Sell Stock II, Lemonade Change, Maximum Units on a Truck, Array Partition, Minimum Absolute Difference.
- **Medium:** Jump Game, Jump Game II, Gas Station, Non-overlapping Intervals, Merge Intervals, Task Scheduler, Partition Labels, Queue Reconstruction by Height, Minimum Number of Arrows to Burst Balloons, Hand of Straights.
- **Hard:** Candy, Minimum Number of Refueling Stops, Course Schedule III, Create Maximum Number, Smallest Range Covering Elements.

---

## 16. Dynamic Programming (DP)

**Definition:** Solve a problem by breaking it into **overlapping subproblems**, solving each only **once**, and storing the answers (memoization / tabulation).

**When to use:** the problem asks for max / min / count / "is it possible", and decisions depend on smaller versions of the same problem.

**Visual: Fibonacci table**
```
 dp[0]=0, dp[1]=1,  dp[i] = dp[i-1] + dp[i-2]
 i :   0  1  2  3  4  5  6
 dp:  [0, 1, 1, 2, 3, 5, 8]
```

**Visual: 0/1 Knapsack (capacity 5, items: w=2 v=3, w=3 v=4, w=4 v=5)**
```
 dp[i][w] = best value using first i items with capacity w
 w ->     0  1  2  3  4  5
 i=0      0  0  0  0  0  0
 i=1      0  0  3  3  3  3        (take item 1: w=2, v=3)
 i=2      0  0  3  4  4  7        (item 2: w=3, v=4 -> 3 + 4 = 7 at w=5)
 i=3      0  0  3  4  5  7        answer = 7
 dp[i][w] = max( dp[i-1][w],  value[i] + dp[i-1][w - weight[i]] )
```

**How to solve any DP (5 steps)**
1. **State:** what does `dp[i]` (or `dp[i][j]`) mean?
2. **Transition:** how does it depend on smaller states?
3. **Base case:** smallest known answers.
4. **Order:** which direction to fill (top-down memo or bottom-up table).
5. **Answer:** which cell holds it? Then **optimise space** (keep only last row).

**Real-world examples:** GPS route planning, spell correction (edit distance), DNA sequence alignment, stock trading strategies, resource allocation (knapsack), text justification.

**Brute force vs optimal**
| Problem | Brute force | DP |
|---------|-------------|----|
| Fibonacci | O(2ⁿ) | O(n), O(1) space |
| Climbing stairs | O(2ⁿ) | O(n) |
| Coin change (min coins) | try all combinations O(Sⁿ) | O(amount x coins) |
| LCS of two strings | all subsequences O(2ⁿ) | O(n·m) |
| 0/1 Knapsack | all subsets O(2ⁿ) | O(n·W) |

**Common DP families**
```
 1D DP          : Climbing Stairs, House Robber, Decode Ways, Max Subarray
 Knapsack       : Subset Sum, Partition Equal Subset, Coin Change, Target Sum
 Strings (2D)   : LCS, Edit Distance, Longest Palindromic Subsequence
 Grid (2D)      : Unique Paths, Min Path Sum, Maximal Square
 LIS            : Longest Increasing Subsequence (O(n log n) with binary search)
 Interval DP    : Burst Balloons, Matrix Chain Multiplication
 Bitmask DP     : Travelling Salesman, Assignment problems
 Tree DP        : House Robber III, Diameter of Tree
 DP on stocks   : Buy and Sell with cooldown / k transactions
```

**Related concepts:** memoization vs tabulation, overlapping subproblems, optimal substructure, space optimisation, bitmask DP, DP on trees and graphs, digit DP.

**Practice**
- **Easy:** Climbing Stairs, Fibonacci Number, Min Cost Climbing Stairs, House Robber, Maximum Subarray, Pascal's Triangle, N-th Tribonacci Number.
- **Medium:** Coin Change, Coin Change II, Longest Increasing Subsequence, Longest Common Subsequence, Unique Paths (I and II), Minimum Path Sum, Partition Equal Subset Sum, Decode Ways, Word Break, House Robber II, Edit Distance, Target Sum, Best Time to Buy and Sell Stock with Cooldown.
- **Hard:** Burst Balloons, Regular Expression Matching, Longest Valid Parentheses, Distinct Subsequences, Palindrome Partitioning II, Maximal Rectangle, Best Time to Buy and Sell Stock IV, Travelling Salesman (bitmask), Egg Dropping.

---

## 17. Bit Manipulation

**Definition:** Working directly with the **binary bits** of numbers using AND, OR, XOR, NOT and shifts.

**Visual**
```
  5 = 0101        A & B  (AND)  both 1        0101 & 0011 = 0001
  3 = 0011        A | B  (OR)   any 1         0101 | 0011 = 0111
                  A ^ B  (XOR)  different     0101 ^ 0011 = 0110
  x << 1  = x * 2           x >> 1  = x / 2
```

**Useful tricks**
| Trick | Code | Meaning |
|-------|------|---------|
| Check bit i | `(n >> i) & 1` | is the i-th bit set |
| Set bit i | `n \| (1 << i)` | make it 1 |
| Clear bit i | `n & ~(1 << i)` | make it 0 |
| Toggle bit i | `n ^ (1 << i)` | flip it |
| Power of 2 | `n & (n-1) == 0` | only one bit set |
| Remove lowest set bit | `n & (n-1)` | used to count bits |
| Isolate lowest set bit | `n & -n` | |
| Find the single number | XOR all | pairs cancel (`a ^ a = 0`) |

```
Single Number [4, 1, 2, 1, 2]:  4 ^ 1 ^ 2 ^ 1 ^ 2 = 4
```

**Real-world examples:** permissions flags (read / write / execute), compression and encryption, graphics masks, network IP and subnet masks, fast hash functions.

**Brute force vs optimal:** find the unique number: hash map O(n) space → XOR O(1) space. Subsets of n items: use a bitmask from 0 to 2ⁿ - 1.

**Related concepts:** two's complement, bitmask DP, Gray code, subset enumeration with masks, XOR properties.

**Practice**
- **Easy:** Single Number, Number of 1 Bits, Power of Two, Missing Number, Reverse Bits, Hamming Distance, Counting Bits.
- **Medium:** Single Number II and III, Subsets (bitmask), Sum of Two Integers (no +), Bitwise AND of Numbers Range, Maximum XOR of Two Numbers (trie), Divide Two Integers.
- **Hard:** Maximum XOR With an Element From Array, Count Triplets with XOR equal, Shortest Path Visiting All Nodes (bitmask BFS), Smallest Sufficient Team.

---

# PHASE 4: NON-LINEAR STRUCTURES

## 18. Binary Tree

**Definition:** A hierarchical structure where each node has at most **two children** (left and right). Top node = **root**, nodes with no children = **leaves**.

**Visual**
```
              1            <- root, level 0
            /   \
           2     3         <- level 1
          / \     \
         4   5     6       <- leaves: 4, 5, 6      height = 2

 Inorder   (L, Root, R) : 4 2 5 1 3 6
 Preorder  (Root, L, R) : 1 2 4 5 3 6
 Postorder (L, R, Root) : 4 5 2 6 3 1
 Level order (BFS)      : 1 | 2 3 | 4 5 6
```

**How it works:** most tree problems are solved with **recursion** (DFS) or a **queue** (BFS). Think: "what do I need from my left and right child, and how do I combine it at this node?"
```python
def height(node):
    if not node: return 0                      # base case
    return 1 + max(height(node.left), height(node.right))
```

**Types:** full, complete (heap), perfect, balanced (AVL / red-black), skewed (like a linked list, worst case).

**Real-world examples:** file system folders, HTML DOM, company org chart, decision trees in machine learning, expression parsing in compilers.

**Brute force vs optimal:** Diameter of tree: compute height for every node O(n²) → compute height and diameter together in one DFS O(n). Lowest Common Ancestor: store both root paths O(n) space → one recursive pass O(1) extra.

**Related concepts:** DFS vs BFS, Morris traversal (O(1) space), serialization, tree DP, Euler tour, binary lifting for LCA.

**Practice**
- **Easy:** Maximum Depth, Invert Binary Tree, Same Tree, Symmetric Tree, Path Sum, Diameter of Binary Tree, Balanced Binary Tree, Subtree of Another Tree, Merge Two Binary Trees.
- **Medium:** Level Order Traversal, Zigzag Level Order, Right Side View, Lowest Common Ancestor, Construct Tree from Preorder and Inorder, Path Sum II / III, Flatten Binary Tree to Linked List, Binary Tree Maximum Path Sum (hard-ish), Count Good Nodes.
- **Hard:** Binary Tree Maximum Path Sum, Serialize and Deserialize Binary Tree, Vertical Order Traversal, Recover Binary Search Tree, Binary Tree Cameras.

---

## 19. Binary Search Tree (BST) and Balanced Trees

**Definition:** A binary tree where for every node: **all left values < node < all right values**.

**Visual**
```
            8
          /   \
         3     10          search 6:  8 -> go left -> 3 -> go right -> 6  FOUND
        / \      \
       1   6      14       inorder traversal of a BST is SORTED: 1 3 4 6 7 8 10 13 14
          / \    /
         4   7  13
```

**How it works**
| Operation | Balanced | Skewed (worst) |
|-----------|----------|----------------|
| Search / Insert / Delete | O(log n) | O(n) |

Delete cases: node with 0 children (remove), 1 child (replace with child), 2 children (replace with **inorder successor**, then delete that).

**Self-balancing:** AVL and Red-Black trees rotate nodes after insert / delete to keep height O(log n).
```
 Right rotation fixes a left-heavy tree:      z               y
                                             /               / \
                                            y      ->       x   z
                                           /
                                          x
```

**Real-world examples:** ordered maps and sets (`TreeMap`, C++ `map`), database indexes (B-trees), autocomplete suggestions, auto-sorted leaderboards.

**Brute force vs optimal:** validate BST by checking each node against the whole subtree O(n²) → pass down (min, max) bounds O(n). K-th smallest: full inorder O(n) → stop early at k.

**Related concepts:** inorder successor / predecessor, AVL, Red-Black, B-tree, Treap, order statistic tree.

**Practice**
- **Easy:** Search in a BST, Insert into a BST, Range Sum of BST, Minimum Absolute Difference in BST, Convert Sorted Array to BST, Two Sum IV (BST), Lowest Common Ancestor of a BST.
- **Medium:** Validate BST, Kth Smallest Element in a BST, Delete Node in a BST, Binary Search Tree Iterator, Construct BST from Preorder, Inorder Successor, Unique Binary Search Trees (DP).
- **Hard:** Recover BST, Count of Smaller Numbers After Self, Serialize and Deserialize BST, Closest Binary Search Tree Value II, Contains Duplicate III.

---

## 20. Graphs (BFS, DFS, Topological Sort)

**Definition:** A set of **vertices (nodes)** connected by **edges**. Can be directed or undirected, weighted or unweighted.

**Visual**
```
     A --- B                 Adjacency list:             Adjacency matrix:
     |     |  \              A: [B, C]                      A B C D E
     C --- D   E             B: [A, D, E]                A  0 1 1 0 0
                             C: [A, D]                   B  1 0 0 1 1
                             D: [B, C]                   C  1 0 0 1 0
                             E: [B]                      D  0 1 1 0 0
                                                         E  0 1 0 0 0
```

**BFS (level by level, uses a queue) from A:**
```
 level 0: A
 level 1: B, C          queue: [A] -> [B, C] -> [C, D, E] -> [D, E] -> ...
 level 2: D, E          BFS gives the SHORTEST path in an unweighted graph
```

**DFS (go deep first, uses recursion / stack) from A:** `A → B → D → C → E`

| Algorithm | Time | Used for |
|-----------|------|----------|
| BFS | O(V + E) | shortest path (unweighted), levels, flood fill |
| DFS | O(V + E) | connected components, cycle detection, paths, topological sort |
| Topological sort | O(V + E) | order tasks with dependencies (DAG only) |

```
 Topological sort (Kahn's):  courses  A -> B -> D,  A -> C -> D
 in-degree: A0 B1 C1 D2 .  Start with in-degree 0 (A). Remove A: B0 C0 -> queue. Result: A B C D
```

**Real-world examples:** social network friends, Google Maps roads, web page links (PageRank), course prerequisites, network routing, dependency managers (npm, pip).

**Brute force vs optimal:** finding connected components by comparing every pair O(V²) → DFS / BFS O(V + E). Cycle detection with all paths → DFS colour marking (white / grey / black) O(V + E).

**Related concepts:** adjacency list vs matrix, visited set, directed vs undirected, cycle detection, bipartite check, connected and strongly connected components (Kosaraju / Tarjan), grid as graph, multi-source BFS.

**Practice**
- **Easy:** Flood Fill, Find if Path Exists in Graph, Number of Provinces, Find the Town Judge, Island Perimeter, Employee Importance.
- **Medium:** Number of Islands, Clone Graph, Course Schedule I and II (topological), Rotting Oranges (multi-source BFS), Pacific Atlantic Water Flow, Surrounded Regions, Is Graph Bipartite, Word Ladder, Redundant Connection, Max Area of Island.
- **Hard:** Word Ladder II, Alien Dictionary, Critical Connections in a Network (Tarjan), Shortest Path Visiting All Nodes, Reconstruct Itinerary, Minimum Height Trees.

---

## 21. Shortest Path and Minimum Spanning Tree

**Definition:** **Shortest path** = least-cost route between nodes in a weighted graph. **MST** = a set of edges connecting all nodes with minimum total weight and no cycle.

**Visual: Dijkstra from A**
```
          2        3
     A ------ B ------ D
      \       |       /
     5 \    1 |     / 1
        \     |   /
          --- C ----
 dist: A=0  B=2  C=3 (via B: 2+1)  D=4 (via C: 3+1)

 Always pick the unvisited node with the smallest distance (min-heap).
```

| Algorithm | Handles | Time | Idea |
|-----------|---------|------|------|
| BFS | unweighted | O(V + E) | levels |
| Dijkstra | non-negative weights | O((V + E) log V) | greedy + min-heap |
| Bellman-Ford | negative weights, detects negative cycle | O(V·E) | relax all edges V-1 times |
| Floyd-Warshall | all pairs | O(V³) | DP through intermediate nodes |
| Kruskal (MST) | | O(E log E) | sort edges, add if no cycle (DSU) |
| Prim (MST) | | O(E log V) | grow tree from a node (min-heap) |

**Real-world examples:** GPS navigation, flight and ticket pricing, internet packet routing (OSPF), laying cable / pipe network with minimum cost (MST).

**Brute force vs optimal:** trying every path is exponential → Dijkstra O((V+E) log V).

**Related concepts:** relaxation, priority queue, 0-1 BFS, A* search (heuristic), negative cycles, DSU for Kruskal.

**Practice**
- **Easy:** Network Delay Time (simple graph), Find the Town Judge, Min Cost to Connect Sticks (heap warm-up).
- **Medium:** Network Delay Time, Cheapest Flights Within K Stops, Path With Minimum Effort, Path with Maximum Probability, Min Cost to Connect All Points (MST), Connecting Cities With Minimum Cost, Swim in Rising Water.
- **Hard:** Shortest Path Visiting All Nodes, Minimum Cost to Make at Least One Valid Path, Critical and Pseudo-Critical Edges in MST, Reachable Nodes in Subdivided Graph.

---

# PHASE 5: ADVANCED

## 22. Union-Find (Disjoint Set Union, DSU)

**Definition:** A structure to track which elements belong to the **same group**, with fast `find` (which group?) and `union` (merge groups).

**Visual**
```
 start:   0  1  2  3  4     (each is its own parent)
 union(0,1), union(2,3), union(1,3):

        0            parent[1]=0, parent[3]=2 -> after union(1,3): parent[2]=0
       / \                         0
      1   2          group {0,1,2,3}  /|\
          |                          1 2 ...
          3          4 is alone
 Path compression: find(3) re-points 3 directly to root 0.
```

**How it works:** `find` follows parents to the root (with **path compression**); `union` attaches the smaller tree under the larger (**union by rank / size**). Both become nearly **O(α(n)) ≈ O(1)**.

**Real-world examples:** friend groups / connected networks, detecting a cycle when adding cables (Kruskal), image segmentation, merging accounts with shared emails.

**Brute force vs optimal:** DFS each time to check connectivity O(V + E) per query → DSU almost O(1) per query.

**Related concepts:** Kruskal's MST, cycle detection in undirected graphs, connected components count, weighted DSU, offline queries.

**Practice**
- **Easy:** Find if Path Exists in Graph, Number of Provinces (DSU version), Redundant Connection (easy version).
- **Medium:** Redundant Connection, Number of Connected Components, Accounts Merge, Most Stones Removed, Satisfiability of Equality Equations, Graph Valid Tree, Evaluate Division.
- **Hard:** Number of Islands II, Swim in Rising Water, Smallest String With Swaps, Bricks Falling When Hit, Checking Existence of Edge Length Limited Paths.

---

## 23. Trie (Prefix Tree)

**Definition:** A tree where each edge is a **character**; every path from the root spells a prefix. Used for fast prefix and word lookup.

**Visual: words "cat", "car", "dog"**
```
            (root)
           /      \
          c        d
          |        |
          a        o
         / \       |
        t*  r*     g*          * = end of a word
 search("car") -> c -> a -> r  (end marker) = found    O(length of word)
```

**How it works:** each node stores up to 26 children (array or map) plus an `isEnd` flag. Insert, search and startsWith all cost **O(L)** where L = word length, independent of how many words are stored.

**Real-world examples:** autocomplete in search bars and phones, spell checkers, IP routing (longest prefix match), word games (Boggle / Scrabble).

**Brute force vs optimal:** store words in a list and scan for a prefix O(N·L) → trie O(L).

**Related concepts:** compressed trie / radix tree, suffix tree, Aho-Corasick (multi-pattern search), binary trie for maximum XOR.

**Practice**
- **Easy:** Implement Trie (Prefix Tree), Longest Common Prefix (trie), Index Pairs of a String.
- **Medium:** Design Add and Search Words, Replace Words, Map Sum Pairs, Search Suggestions System, Maximum XOR of Two Numbers, Longest Word in Dictionary, Prefix and Suffix Search.
- **Hard:** Word Search II, Concatenated Words, Palindrome Pairs, Stream of Characters, Maximum XOR With an Element From Array.

---

## 24. Segment Tree and Fenwick Tree (BIT)

**Definition:** Structures that answer **range queries** (sum, min, max) and **point updates** both in **O(log n)**.

**Visual: segment tree for sums on [2, 4, 1, 3]**
```
                [0..3] = 10
               /            \
         [0..1] = 6        [2..3] = 4
         /      \          /      \
     [0] = 2  [1] = 4  [2] = 1  [3] = 3

 query sum(1..2) -> use nodes [1]=4 and [2]=1 -> 5          O(log n)
 update a[2]=5   -> change leaf, recompute parents [2..3] and [0..3]
```

| Structure | Query | Update | Build | Notes |
|-----------|-------|--------|-------|-------|
| Prefix sum | O(1) | O(n) | O(n) | no updates allowed |
| Segment tree | O(log n) | O(log n) | O(n) | any associative op (sum, min, gcd), lazy propagation for range updates |
| Fenwick (BIT) | O(log n) | O(log n) | O(n log n) | shorter code, prefix sums |

**Real-world examples:** stock price range analytics with live updates, game leaderboards by rank, database range aggregation, event counters.

**Brute force vs optimal:** q range queries on an array with updates: O(n) each → O(log n) each.

**Related concepts:** lazy propagation, sparse table (static range min, O(1) query), sqrt decomposition, Mo's algorithm, offline queries.

**Practice**
- **Easy:** Range Sum Query Immutable (prefix sum warm-up).
- **Medium:** Range Sum Query Mutable, Count of Smaller Numbers After Self (BIT), Range Sum Query 2D Mutable, My Calendar I / II / III, Count of Range Sum.
- **Hard:** The Skyline Problem, Reverse Pairs, Longest Increasing Subsequence II, Falling Squares, Rectangle Area II.

---

# QUICK REFERENCE

## A. "If you see this, think this" cheat sheet
| Clue in the problem | Try |
|---------------------|-----|
| Sorted array, find a pair / triplet | Two pointers |
| Subarray / substring with a condition | Sliding window |
| Count or sum over ranges | Prefix sum (+ hash map) |
| "Have I seen this before?" | HashSet / HashMap |
| Sorted input or "minimum value such that..." | Binary search (on index or on answer) |
| Next greater / smaller, matching brackets | Stack / monotonic stack |
| Top K, K-th, running median | Heap |
| Shortest path, unweighted, levels | BFS |
| All combinations / permutations / subsets | Backtracking |
| Count ways / min cost / max profit with choices | Dynamic programming |
| Intervals, scheduling, "always pick the earliest ending" | Greedy |
| Tree problem | DFS recursion (or BFS for levels) |
| Groups, connectivity, merging | Union-Find |
| Dependencies / ordering | Topological sort |
| Prefix of strings | Trie |
| Pairs cancel out, single element | XOR |

## B. Data structure operation costs
| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked list | O(n) | O(n) | O(1)* | O(1)* |
| Stack / Queue | O(n) | O(n) | O(1) | O(1) |
| Hash table | - | O(1) avg | O(1) avg | O(1) avg |
| BST (balanced) | - | O(log n) | O(log n) | O(log n) |
| Heap | O(1) top | O(n) | O(log n) | O(log n) |
| Trie | - | O(L) | O(L) | O(L) |

\* when the node position is already known.

## C. Algorithm complexity summary
| Algorithm | Time | Space |
|-----------|------|-------|
| Binary search | O(log n) | O(1) |
| Merge sort | O(n log n) | O(n) |
| Quick sort (avg) | O(n log n) | O(log n) |
| BFS / DFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) | O(V) |
| Kruskal | O(E log E) | O(V) |
| Knapsack DP | O(n·W) | O(W) |
| LCS DP | O(n·m) | O(min(n, m)) |

## D. Recommended practice order (about 250 problems)
```
Week 1-2   Arrays, Strings, Hashing                 (35)
Week 3-4   Two pointers, Window, Prefix, Sort, BS   (45)
Week 5-6   Linked List, Stack, Queue, Heap          (45)
Week 7-9   Recursion, Backtracking, Greedy, Bits    (40)
Week 10-12 Dynamic Programming                      (40)
Week 13-14 Trees, BST                               (30)
Week 15-16 Graphs, Shortest Path, DSU, Trie         (30)
Then       Mock interviews, company-wise sets, contests
```

## E. Famous problem lists to follow
- **Blind 75** (the smallest high-value list)
- **NeetCode 150** (Blind 75 extended, grouped by topic)
- **Striver's SDE Sheet / A2Z** (very popular in India)
- **Love Babbar 450**
- **LeetCode Top Interview 150**

## F. Interview checklist
- [ ] Clarify input size, constraints, duplicates, negatives, empty input.
- [ ] Say the brute force out loud with its complexity.
- [ ] Spot the bottleneck, then name the data structure or pattern that fixes it.
- [ ] Code cleanly, then dry run on a small example.
- [ ] State final time and space complexity.
- [ ] Discuss trade-offs and follow-ups (what if the data is huge, streaming, or sorted?).

---

## Progress Tracker

- [ ] 1 Complexity
- [ ] 2 Arrays
- [ ] 3 Strings
- [ ] 4 Hashing
- [ ] 5 Two Pointers and Sliding Window
- [ ] 6 Prefix Sum
- [ ] 7 Sorting
- [ ] 8 Binary Search
- [ ] 9 Linked List
- [ ] 10 Stack
- [ ] 11 Queue and Deque
- [ ] 12 Heap
- [ ] 13 Recursion
- [ ] 14 Backtracking
- [ ] 15 Greedy
- [ ] 16 Dynamic Programming
- [ ] 17 Bit Manipulation
- [ ] 18 Binary Tree
- [ ] 19 BST
- [ ] 20 Graphs
- [ ] 21 Shortest Path and MST
- [ ] 22 Union-Find
- [ ] 23 Trie
- [ ] 24 Segment Tree and Fenwick
