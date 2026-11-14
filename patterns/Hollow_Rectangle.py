"""
**********
*        *
*        *
**********

"""
row=int(input())
col=int(input())

for i in range(row):
    if i==0 or i==row-1:
        for j in range(col):
            print("*",end=" ")
    else:
        for j in range(col):
            if j==0 or j==col-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()