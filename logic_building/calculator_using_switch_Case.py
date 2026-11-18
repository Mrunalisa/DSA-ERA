menu=""""
1.add
2.sub
3.mul
4.div
5. mod
"""
print(menu)
value=int(input("enter your no: "))

match(value):
  case 1:
        a,b=map(int,input().split())
        print(a+b)
    case 2:
        a,b=map(int,input().split())
        print(a-b)
    case 3:
        a,b=map(int,input().split())
        print(a*b)
    case 4:
        a,b=map(int,input().split())
        print(a//b)
    case 5:
        a,b=map(int,input().split())
        print(a%b)
    case _:
        result = "unknown"
        print(result)


"""
1.add
2.sub
3.mul
4.div
5. mod

enter your no: 6
unknown

""""