
n = int(input())

# Upper hollow pyramid
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")

    for j in range(i+1):
        if j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(i):
        if j == i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Lower inverted hollow pyramid
for i in range(n-1):
    for j in range(i+1):
        print(" ", end=" ")

    for j in range(n-i-1):
        if j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(n-i-2):
        if j == n-i-3:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()
print()

for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1):
    for j in range(i+2):
        print(" ", end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(n-i-2):
        print("*",end=" ")
    print()
