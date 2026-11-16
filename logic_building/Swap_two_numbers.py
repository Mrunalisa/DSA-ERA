#1. using 3rd variable
a=int(input())
b=int(input())
print("before swapping:")
print("a =", a)
print("b =", b)
c=a
a=b
b=c
print()
print("after swapping:")
print("a =", a)
print("b =", b)

print("---------------------------------------------------")

#2.without using 3rd
a=int(input())
b=int(input())
print("before swapping:")
print("a =", a)
print("b =", b)

a,b=b,a
print()
print("after swapping:")
print("a =", a)
print("b =", b)

print("---------------------------------------------------")

#3.without using 3rd
a=int(input())
b=int(input())
print("before swapping:")
print("a =", a)
print("b =", b)

a=a+b
b=a-b
a=a-b
print()
print("after swapping:")
print("a =", a)
print("b =", b)

