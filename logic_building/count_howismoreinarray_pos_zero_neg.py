n=int(input())
arr=list(map(int,input().split()))
pos,neg,zero=0,0,0
for i in range(n):
    if arr[i]>0:
        pos+=1
    elif arr[i]<0:
        neg+=1
    else:
        zero+=1

if pos>=neg and pos>=zero:
    print(pos)
elif(neg>=pos and neg>=zero):
    print(neg)
else:
    print(zero)


"""

6
0 0 0 0 0 0 
6

5
1 2 3 4 -1
4

5
1 2 -4 -5 0
2

4
-1 -1 -3 0
3

"""
