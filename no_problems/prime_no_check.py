n=int(input())
for i in range(2,n):
    if n%i==0:
        print("not prime no")
        break
else:
    print("prime no")




"""
Prime Number
Simple definition: A number greater than 1 that is divisible only by 1 and itself.

Example: 7

Factors of 7:

1, 7

Total factors = 2.
7 is Prime
Example: 8

Factors of 8:

1, 2, 4, 8

Total factors = 4.
8 is Not Prime
Other prime numbers:

2, 3, 5, 7, 11, 13, 17, 19, 23.

Remember: 1 is neither prime nor composite.

"""