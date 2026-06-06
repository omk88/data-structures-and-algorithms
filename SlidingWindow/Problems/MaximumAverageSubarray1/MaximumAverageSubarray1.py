def findMaxAverage(nums: List[int], k: int) -> float:
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))

# Fixed size sliding window