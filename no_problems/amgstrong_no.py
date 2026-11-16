n=int(input())
amg=n
ans=0
count=0

while n!=0:
  count+=1
  n=n//10
n=amg
while n!=0:
  rev=n%10
  ans+=(rev**count)
  n=n//10

if amg==ans:
    print(f"{amg} is amstrong")
else:
    print(f"{amg} is not amstrong")