def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    smallest_minimum_length = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            current_window_size = right - left + 1
            smallest_minimum_length = min(smallest_minimum_length, current_window_size)

            current_sum -= nums[left]
            left += 1

    return smallest_minimum_length if smallest_minimum_length != float("inf") else 0
    