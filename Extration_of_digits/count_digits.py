def count_digits(no):
    num=no
    count=0
    while(num>0):
        count+=1
        num//=10 #quotient
    return count

no=int(input("Enter No: "))
res=count_digits(no)
print(f"Count of Digits in Number is {res}")

tc_sc='''
time complexity:
O(log 10(n))

Space Complexity:
O(1)
'''

print(tc_sc)