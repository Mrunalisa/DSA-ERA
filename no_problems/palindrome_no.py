n=int(input())
pal=n
ans=0
while n!=0:
  rev=n%10
  ans=(ans*10)+rev
  n=n//10

if pal==ans:
  print(f"{pal} is palindrome")
else:
   print(f"{pal} is not palindrome")