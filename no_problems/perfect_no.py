n=int(input())
sum=0
for i in range(1,n):
  if n%i==0:
    sum+=i

if(n==sum):
  print(f"{n} is perfect no")
else:
  print(f"{n} is not perfect no")


"""

5
5 is not perfect no

defination no is divisible by nos and its sum of those no is equal to that no

eg: n=6
sum=0
6% 1==0
true then sum=sum+1=1
6%2==0
true sum=sum=1+2=3
6%3==0:
true then sum=3+3=6

remaing all comparison n-1
all false

so file is 
if n==sum:
   print perfect no
else:
    print not perfect no


Perfect Number
Simple definition: A number is perfect when the sum of all its factors except itself equals the original number.

Example: 6

Find factors of 6:

1, 2, 3, 6

Remove 6 because we don't include the number itself.

Add remaining factors:
\[
1+2+3=6
\]

6 is Perfect Number
Another example: 28

Factors: 1, 2, 4, 7, 14, 28.

Exclude 28.
\[
1+2+4+7+14=28
\]

28 is Perfect Number
Example of not perfect: 12
\[
1+2+3+4+6=16
\]

16 is not equal to 12.


"""