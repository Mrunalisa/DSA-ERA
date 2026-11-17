n=int(input())
for i in range(2,n+1):
  for j in range(2,i):
    if i%j==0:
        print(f"{i} not prime no")
        break
  else:
      print(f"{i} prime no")


'''

10
2 prime no
3 prime no
4 not prime no
5 prime no
6 not prime no
7 prime no
8 not prime no
9 not prime no
10 not prime no

'''

'''
Prime Numbers in a Range
Simple definition: Find all prime numbers between two given numbers.

Example: 1 to 20

Check which numbers have exactly two factors.
Number	Factors	Prime?
2	1, 2	Yes
3	1, 3	Yes
4	1, 2, 4	No
5	1, 5	Yes
6	1, 2, 3, 6	No
7	1, 7	Yes
8	1, 2, 4, 8	No
9	1, 3, 9	No
11	1, 11	Yes
13	1, 13	Yes
17	1, 17	Yes
19	1, 19	Yes

Answer:
\[
2,3,5,7,11,13,17,19
\]

Total prime numbers = 8.

'''