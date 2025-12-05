def palindrome(no):
    num=no
    rev=0
    while(num>0):
        last_digit=num%10
        rev=(rev*10)+last_digit
        num//=10
    return no==rev
no=int(input("Enter No: "))
res=palindrome(no)
if(res):
    print(f"{no} is Palindrome")
else:
    print(f"{no} is not Palindrome")

tc_sc='''
time complexity:
O(log 10(n))

Space Complexity:
O(1)
'''

print(tc_sc)