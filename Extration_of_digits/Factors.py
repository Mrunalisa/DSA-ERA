from math import sqrt
#Broute Frorce Approach to find factors of a number
class factors:
    def __init__(self, number):
        self.number = number

    def get_factors(self):
        result = []
        for i in range(1, self.number + 1):
            if self.number % i == 0:
                result.append(i) # tc=O(n)
        return result
no = int(input("Enter No: "))
factor_instance = factors(no)
print(f"{no} factors are: {factor_instance.get_factors()}")

tc_sc='''
time complexity:
O(n)

Space Complexity:
O(k) where k = number of factors.
'''

print(tc_sc)


# Better Solution to find factors of a number
def better_factors(no):
    result = []
    num=no
    for i in range(1, (num//2)+ 1):
        if num % i == 0:
            result.append(i)
    result.append(num)  # including the number itself
    return result
print("better soution:\nfactors are", better_factors(no))
tc_sc='''
time complexity:
O(n/2) = O(n)
Space Complexity:
O(k) where k = number of factors.
'''


print(tc_sc)
# optimal approach to find factors of a number

def optimal_factors(no):
    result = []
    num=no
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if i != num // i:  # To avoid adding the square root twice
                result.append(num // i)
    result.sort()  # Sorting the factors  time complexity O(n log n)
    return result
print("optimal soution:\nfactors are",optimal_factors(no))
tc_sc='''
time complexity:
O(sqrt(n))+O(n log n) = O(n log n)
if sorting is not considered then O(sqrt(n))

Space Complexity:
O(k) where k = number of factors.
'''

print(tc_sc)