n=int(input())
ans=0
while n!=0:
  rev=n%10
  ans+=rev
  n=n//10

print(ans)