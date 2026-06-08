from collections import Counter
"""
def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)
"""

"""
def anagrams(s1, s2):
    return char_count(s1) == char_count(s2) # Checks if they have the same keys and same values
"""


"""
def char_count(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0

        count[char] += 1

    return count

print(char_count("catss"))
"""

"""
print(anagrams("catss", "sastc"))

"""
"""
def most_frequent_char(s):
    s_count = Counter(s)
    best = None

    for char in s:
        if best is None or s_count[char] > s_count[best]:
            best = char

    return best
    


print(most_frequent_char("abby"))
"""
"""
def pair_sum(nums, target_sum):
    previous_nums = {}
    
    for index, num in enumerate(nums):
        complement = target_sum - num

        if complement in previous_nums:
            return (previous_nums[complement], index)
        
        previous_nums[num] = index


print(pair_sum([5,2,6,4,2], 100))
"""
"""
def pair_product(nums, target):
    previous_nums = {}

    for index, num in enumerate(nums):
        complement = target / num

        if complement in previous_nums:
            return (index, previous_nums[complement])
        
        previous_nums[num] = index

print(pair_product([7,3,8,3,2,5], 35))
"""
"""
def intersection(a, b):
    result = []
    items_set = set(a)

    for ele in b:
        if ele in items_set:
            result.append(ele)


    return result

def intersection2(a, b):
    items_set = set(a)
    return [ i for i in b if i in items_set ]

print(intersection2([1,2,3,4,5],[3,4,5,6,7,8]))

"""

