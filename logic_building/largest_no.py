a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(f"{a} is largest no")
elif b>=a and b>=c:
    print(f"{b} is largest no")
else:
    print(f"{c} is largest no")

"""
12
12
2
12 is largest no
"""

a=int(input())
b=int(input())
if a>=b:
    print(f"{a} is largest no")
else:
    print(f"{b} is largest no")