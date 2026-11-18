year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

'''
2027
2027 is not leap year

2026
2026 is not leap year

2008
2008 is leap year
'''