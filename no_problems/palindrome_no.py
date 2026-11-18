n=int(input())
pal=n
ans=0
while n!=0:
  rev=n%10
  ans=(ans*10)+rev
  n=n//10

if pal==ans:
  print(f"{pal} is palindrome")
else:
   print(f"{pal} is not palindrome")



"""
Palindrome Number

121 → Reverse is 121


Palindrome Number
Simple definition: A number that looks the same when read forward and backward.

Example: 121

Original number:
\[
121
\]

Reverse:
\[
121
\]

Both are equal.
121 is Palindrome
Another example: 123

Original = 123

Reverse = 321

123 is not equal to 321.
Not Palindrome
Other examples: 11, 22, 121, 131, 1331.

"""