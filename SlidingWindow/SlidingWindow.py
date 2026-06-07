from collections import Counter

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

def count_substring_anagram(s, anagram):
    # Checking if the first elements in the window match the anagram string
    anagram_counter = Counter(anagram)
    window_counter = Counter(s[:len(anagram)])  
    num_matches = 1 if anagram_counter == window_counter else 0

    # Shifting the window along to search for new matches
    for i in range(0, len(s) - len(anagram)):
        trailing_char = s[i]
        leading_char = s[i + len(anagram)] # len(anagram) is the size of the window
        window_counter[trailing_char] -= 1
        window_counter[leading_char] += 1

        if window_counter == anagram_counter:
            num_matches += 1
    return num_matches

# Sliding window with variable size

# 1. Initialise start pointer to 0

# 2. Initialise window 'collection'

# 3. Iterate end pointer through array

#   a) Add leading element to collection

#   b) Remove trailing elements from collection *while* constraint is violated

# 4. Do the business logic (count, max, min, find, etc.)


def variable_find_sum(nums, target_sum):
    start = 0
    window_sum = 0
    for end in range(0, len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        if window_sum == target_sum:
            return (start, end)

def longest_subarray_sum(nums, target_sum):
    start = 0
    longest = -1
    window_sum = 0
    for end in range(0, len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        if window_sum == target_sum:    
            longest = max(end - start + 1, longest)
    return longest

def longest_unique_substring(s):
    start = 0
    longest = 0
    window_counter = Counter()
    for end in range(0, len(s)):
        leading_char = s[end]
        window_counter[leading_char] += 1

        while window_counter[leading_char] > 1:
            trailing_char = s[start]
            window_counter[trailing_char] -= 1
            start += 1
        longest = max(end - start + 1, longest)
    return longest




print(naive_max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3))

print(optimal_max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3))

print(multiplication_max_subarray_sum_size_k([1, 4, 1, 6, -3, 3, -5, 2, 26], 4))

print(subarray_target_sum_size_k([1, 2, 1, 5, 2, 3, 10, 1, 9, 4, 3, 3, 7], 10, 3))

print(has_substring_anagram("greyhounds", "hoy"))

print(count_substring_anagram("tacoctacabcatt", "cat"))

print(variable_find_sum([1, 2, 3, 7, 5], 12))

print(longest_unique_substring("abcabcqbb"))




# Universal variable length sliding window template

# 1. Initialise the pointers
start = 0
max_length = 0
counts = {} # Tracks state of the current window

# 2. Loop with the 'end' pointer to expand
for end in range(len(s)):
    # Add the incoming element to our state
    char = s[end]
    counts[char] = counts.get(char, 0) + 1

    # 3. Use a 'while' loop to contract if state becomes invalid
    while counts[char] > 2: # The condition that breaks the rules
        left_char = s[start]
        counts[left_char] -= 1 # Remove the outgoing element from the state
        start += 1             # Move the anchor forward

        # 4. Once valid, calculate and update your answer
        max_length = max(max_length, end - start + 1)
