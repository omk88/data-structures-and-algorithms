
# Sliding window with fixed size k

# 1. Process first k elements into some 'collection'.

# 2. Move window to the right.

#    a) Remove trailing element from 'collection'.

#    b) Add leading element to 'collection'.

# 3. Do the business logic ( max, min, etc ).




# Naive sliding window
def naive_max_subarray_sum_size_k(nums, k):
    max_sum = float('-inf')
    for i in range(0, len(nums) - k + 1):
        current_sum = sum(nums[i:i + k])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Optimal sliding window
def optimal_max_subarray_sum_size_k(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Optimal sliding window multiplication
def multiplication_max_subarray_sum_size_k(nums, k):
    current_product = 1
    for i in range(0, k):
        current_product *= nums[i]
    max_product = current_product

    for i in range(0, len(nums) - k):
        current_product /= nums[i]
        current_product *= nums[i + k]
        if current_product > max_product:
            max_product = current_product

    return max_product

# Check that this is correct!
def subarray_target_sum_size_k(nums, target, k):
    current_sum = 0
    for i in range(0, k):
        current_sum += nums[i]

    count = 1 if current_sum == target else 0

    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]

        if current_sum == target:
            count += 1
    
    return count


def has_substring_anagram(s, anagram):
    k = len(anagram)
    window_set = set(s[:k])
    anagram_set = set(anagram)
    if window_set == anagram_set:
        return True
    
    for i in range(0, len(s) - k):
        window_set.remove(s[i])
        window_set.add(s[i + k])
        if window_set == anagram_set:
            return True
        
    return False

print(naive_max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3))

print(optimal_max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3))

print(multiplication_max_subarray_sum_size_k([1, 4, 1, 6, -3, 3, -5, 2, 26], 4))

print(subarray_target_sum_size_k([1, 2, 1, 5, 2, 3, 10, 1, 9, 4, 3, 3, 7], 10, 3))

print(has_substring_anagram("greyhounds", "hoy"))