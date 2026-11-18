n=int(input())
ans=0
while n != 0:
    rev = n % 10
    ans = (ans * 10) + rev
    n = n // 10

print(ans)

"""
123
321
"""

"""
Reverse Number
Simple definition: Change the order of digits of a number from last to first.

Example: 1234

Original:

1 → 2 → 3 → 4

Reverse:

4 → 3 → 2 → 1
Answer = 4321
Another example:
Original	Reverse
123	321
456	654
9876	6789
120	21

"""