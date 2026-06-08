def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    zero_count = 0
    max_consecutive_ones = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1

            left += 1


        current_window_size = right - left + 1
        max_consecutive_ones = max(max_consecutive_ones, current_window_size)
    
    return max_consecutive_ones