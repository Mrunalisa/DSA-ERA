def frequency_map(arr):
    freq_map = {}
    # freq_map = dict() # Another way to initialize an empty dictionary
    # for i in arr:
    #     if(i in freq_map.keys()):
    #         freq_map[i] += 1
    #     else:
    #         freq_map[i] = 1
    # return freq_map

    for i in arr:
        if(i in freq_map):
            freq_map[i] += 1
        else:
            freq_map[i] = 1
    return freq_map

arr=list(map(int,input().split()))
print(frequency_map(arr))

tc_sc='''
time complexity: O(n)
Space complexity: O(n)
'''

print(tc_sc)

def hash_map(arr):
    h_map = {}
    for i in arr:
        h_map[i] = h_map.get(i, 0) + 1
    return h_map
arr=list(map(int,input().split()))
print(hash_map(arr))
tc_sc='''
time complexity: O(n)
Space complexity: O(n)
'''
print(tc_sc)