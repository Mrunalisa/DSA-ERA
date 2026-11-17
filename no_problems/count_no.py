n=int(input())
count=0
while n!=0:
  count+=1
  n=n//10

print(count)


'''
Count Number (Count Digits)
Simple definition: Count how many digits are present in a number.

Example: 12345

Count each digit:
- 1 → First digit
- 2 → Second digit
- 3 → Third digit
- 4 → Fourth digit
- 5 → Fifth digit
\[
Count=5
\]

Answer = 5
Another example:
- 987 → 3 digits
- 56 → 2 digits
- 1234567 → 7 digits

'''