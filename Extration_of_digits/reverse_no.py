def reverse_number(no):
    num=no
    rev=0
    while num>0:
        last_digit=num%10 #reminder
        rev=(rev*10)+last_digit 
        num=num//10 # quotient
    return rev

no=int(input("Enter a number: "))
res=reverse_number(no)
print(f"Reversed Number is: {res}")
print()

tc_sc='''
time complexity:
O(log 10(n))

Space Complexity:
O(1)
'''

print(tc_sc)