p=int(input("enter p: "))
r=int(input("enter r: "))
n=int(input("enter n: "))
simple_interset=(p*r*n)/100

amount=p*((1+r/100)**n)
compund_interset=amount-p
print("Simple Interest:", round(simple_interest, 2))
print("Compound Interest:", round(compound_interest, 2))


'''
enter p: 12
enter r: 4
enter n: 4
Simple Interest: 1.92
Compound Interest: 2.04

'''