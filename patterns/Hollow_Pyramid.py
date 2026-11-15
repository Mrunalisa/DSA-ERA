"""
    *
   * *
  *   *
 *     *
*********
"""

# n=int(input())
# arr=[]
# for i in range(n):
#     t=int(input())
#     arr.append(t)
# print(*arr)

# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+2):
#         print(" ",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     for j in range(n-i-2):
#         print("*",end=" ")
#     print()

n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i):
        if j==i-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

