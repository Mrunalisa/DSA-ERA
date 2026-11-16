# print("1. using list : arr=list(map(int,input().split()))")
# n=int(input())
# arr=list(map(int,input().split()))
# print("---------------------------------------------------")
# print("2. using [int(i) for i in input().split()] : arr=[int(i) for i in input().split()]")
# n=int(input())
# arr=[int(i) for i in input().split()]
# print("---------------------------------------------------")

# print("""3. using for loop and append method :
#             n=int(input()) 
#             arr=[]
#             for i in range(n):
#                 inp=int(input())
#                 arr.append=(inp)""")
# n=int(input()) 
# arr=[]
# for i in range(n):
#     inp=int(input())
#     arr.append(inp)
# print(arr)
# print("---------------------------------------------------")

# '''
# output:
# 1. using list : arr=list(map(int,input().split()))
# 3
# 1 2 3  
# ---------------------------------------------------
# 2. using [int(i) for i in input().split()] : arr=[int(i) for i in input().split()]
# 3
# 23 45 67
# ---------------------------------------------------
# 3. using for loop and append method :
#             n=int(input()) 
#             arr=[]
#             for i in range(n):
#                 inp=int(input())
#                 arr.append=(inp)
# 4
# 1
# 2
# 3
# 4
# [1, 2, 3, 4]
# ---------------------------------------------------

# '''
# a="""
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# """
# print(a)
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# print(arr)

print("----------------------------------------------------------------")
print('''
import sys
n = int(sys.stdin.read())
arr = list(map(int,sys.stdin.read().split()))
''')
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.read().split()))
print(arr)

print("----------------------------------------------------------------")
print("""import sys
n = int(sys.stdin.read())
arr = [int(x) for x in sys.stdin.read().split()]
""")

# import sys
# n = int(sys.stdin.read())
# arr = [int(x) for x in sys.stdin.read().split()]
# print(arr)


print("===============================================================")
print("above 3 way input using raw_input()")
n=int(raw_input())
arr=[int(i) for i in raw_input().split()]
print(arr)

print("-----------------------------------------------------")
n=int(raw_input())
arr=list(map(int,raw_input().split()))
print(arr)

print("-----------------------------------------------------")

n=int(raw_input())
arr=[]
for i in range(n):
    inp=int(raw_input())
    arr.append(inp)
print(arr)


"""
STDIN
3
1 2 3
4
12 34 56 5
3
23
45
67
Output:
above 3 way input using raw_input()
[1, 2, 3]
-----------------------------------------------------
[12, 34, 56, 5]
-----------------------------------------------------
[23, 45, 67]
"""

