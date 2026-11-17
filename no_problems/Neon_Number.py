# Definition: A number is neon if the sum of the digits of its square equals the original number.

# Example: 9

# Step 1: Square the number.

# \[ 9^2=81 \]

# Step 2: Add square's digits.

# \[ 8+1=9 \]

# 9 is Neon

n=int(input())
sum=0
square=n**2

while square!=0:
    rev=square%10
    sum+=rev
    square=square//10
if n==sum:
    print(f"{n} is neon no")
else:
    print(f"{n} is not neon no")


"""
8
8 is not neon no

"""
