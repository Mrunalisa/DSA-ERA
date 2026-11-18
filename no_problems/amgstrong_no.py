n=int(input())
amg=n
ans=0
count=0

while n!=0:
  count+=1
  n=n//10
n=amg
while n!=0:
  rev=n%10
  ans+=(rev**count)
  n=n//10

if amg==ans:
    print(f"{amg} is amstrong")
else:
    print(f"{amg} is not amstrong")


"""
Armstrong Number

153 → 1³ + 5³ + 3³ = 153


Armstrong Number
Simple definition: A number is an Armstrong number if the sum of its digits raised to the power of the total number of digits equals the original number.

Example: 153

Step 1: Count digits = 3.

Step 2: Raise each digit to power 3.
\[
1^3+5^3+3^3
\]

Step 3: Calculate.
\[
1+125+27=153
\]

Step 4: Compare with original number.

153 = 153.
153 is Armstrong
Another example: 123
\[
1^3+2^3+3^3=1+8+27=36
\]

36 is not equal to 123, so it is not Armstrong.

"""