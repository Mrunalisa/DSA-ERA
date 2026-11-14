# Online Python compiler (interpreter)
# Write and run Python online using this editor.

# n=int(input())
# for i in range(n):
#      for j in range(n):
#          print("*",end=" ")
#      print()

# n=int(input())
# for i in range(n):
#      for j in range(i+1):
#          print("*",end=" ")
#      print()

# n=int(input())
# for i in range(n):
#      for j in range(n-i):
#          print("*",end=" ")
#      print()

# n=int(input())
# for i in range(n+1):
#   for j in range(n-i):
#          print(" ",end=" ")
#   for j in range(i):
#          print("*",end=" ")
#   print()


# n=int(input())
# for i in range(n+1):
#   for j in range(n-i):
#          print(" ",end=" ")
#   for j in range(i):
#          print("*",end=" ")
#   for j in range(i-1):
#          print("*",end=" ")
#   for j in range(n-i):
#          print(" ",end=" ")
#   print()


# n=int(input())
# for i in range(n+1):
#   for j in range(n-i):
#          print(" ",end=" ")
#   for j in range(i):
#          print("*",end=" ")
#   for j in range(i-1):
#          print("*",end=" ")
#   for j in range(n-i):
#          print(" ",end=" ")
#   print()

n=int(input())
for i in range(n+1):
  for j in range(n-i):
         print(" ",end=" ")
  for j in range(i):
         print("*",end=" ")
  for j in range(i-1):
         print("*",end=" ")
  for j in range(n-i):
         print(" ",end=" ")
  print()
for i in range(n-1,0,-1):
  for j in range(n-i):
         print(" ",end=" ")
  for j in range(i):
         print("*",end=" ")
  for j in range(i-1):
         print("*",end=" ")
  for j in range(n-i):
         print(" ",end=" ")
  print()