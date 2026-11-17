'''
Definition: A number is automorphic if its square ends with the original number.

Example: 25

Step 1: Calculate square.

[ 25^2=625 ]

Step 2: Check ending digits.

625 ends with 25.

25 is Automorphic

Another example:

[ 76^2=5776 ]

5776 ends with 76.

So 76 is automorphic.

'''
n=int(input())
square=n**2
digit=len(str(n))
ans= square % (10**digit)
if n==ans:
  print(f"{n} is Automorphic Number")
else:
  print(f"{n} is not Automorphic Number")



"""
output:
3
3 is not Automorphic Number

25
25 is Automorphic Number

"""

