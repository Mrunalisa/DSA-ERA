def amstrong(no):
    num=no
    count=0
    add=0
    while(num>0):
        count+=1
        num//=10
    num=no
    while(num>0):
        last_digit=num%10
        add=add+(last_digit**count)
        num//=10
    return add==no

no=int(input("Enter No: "))
res=amstrong(no)
if(res):
    print(f"{no} is Amstrong")
else:
    print(f"{no} is not Amstrong")


tc_sc='''
time complexity:
O(log 10(n))

Space Complexity:
O(1)
'''

print(tc_sc)