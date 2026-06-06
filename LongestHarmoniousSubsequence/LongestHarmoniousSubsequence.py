from collections import Counter

def findLHS(nums: List[int]) -> int:
    mp = Counter(nums)
    
    length = 0
    for key in mp:
        if (key + 1) in mp:
            length = max(length, mp[key] + mp[key + 1])
            
    return length

print(findLHS([1,3,2,2,5,2,3,7]))