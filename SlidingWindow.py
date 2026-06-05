
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

print(naive_max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3))

print(optimal_max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3))

print(multiplication_max_subarray_sum_size_k([1, 4, 1, 6, -3, 3, -5, 2, 26], 4))
