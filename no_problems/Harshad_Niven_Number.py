# Definition: A number is Harshad if it is completely divisible by the sum of its digits.

# Example: 18

# Step 1: Sum digits.

# \[ 1+8=9 \]

# Step 2: Divide original number by digit sum.

# \[ 18\div9=2 \]

# Remainder = 0.

# 18 is Harshad

# Another example: 19

# \[ 1+9=10 \]

# 19 is not divisible by 10.

# So 19 is not Harshad.

n=int(input())
no=n
sum=0
while n!=0:
    rev=n%10
    sum+=rev
    n=n//10

if(no%sum==0):
    print(f"{no} is Harshad")
else:
    print(f"{no} is not Harshad")
