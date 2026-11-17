# Strong Number
# 145 → 1! + 4! + 5! = 145


n=int(input())
comp_no=n
ans=0
while n!=0:
    rev=n%10
    fact=1
    for i in range(1,rev+1):
        fact*=i
    ans+=fact
    n=n//10

if(ans==comp_no):
    print(f"{comp_no} is strong no")
else:
    print(f"{comp_no} is not strong no")

"""
output:

123
123 is not strong no

145
145 is strong no

"""

'''
Strong Number
Simple definition: A number is strong if the sum of the factorials of its digits equals the original number.

Example: 145

First understand factorial:
\[
5!=5\times4\times3\times2\times1=120
\]

Now calculate:
\[
1!+4!+5!
\]

\[
1+24+120=145
\]

145 is Strong Number
Another example: 123
\[
1!+2!+3!
\]

\[
1+2+6=9
\]

9 is not equal to 123.
123 is Not Strong

'''
