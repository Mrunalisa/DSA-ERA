'''
*********
 *     *
  *   *
   * *
    *
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        if j==0 or i==0:
            print("*",end=" ")
        else:
             print(" ",end=" ")
    for j in range(n-i-1):
        if j==n-i-2 or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()