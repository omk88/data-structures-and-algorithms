def longestAlternatingSubarray(nums: List[int], threshold: int) -> int:
    start = 0
    longest_length = 0

    for end in range(0, len(nums)):

        if nums[end] > threshold:
            start = end + 1
            continue

        if end > start and (nums[end] % 2 == nums[end - 1] % 2):
            start = end

        if nums[start] % 2 != 0:
            start = end + 1
        else:
            longest_length = max(longest_length, end - start + 1)

    return longest_length

print(longestAlternatingSubarray([3,2,5,4], 5))