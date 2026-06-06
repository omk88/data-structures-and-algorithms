def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()

    if k == 1:
        return 0

    min_difference = float("inf")

    for i in range(len(nums) - k + 1):
        left_pointer = i
        right_pointer = i + k - 1

        current_difference = nums[right_pointer] - nums[left_pointer]

        if current_difference < min_difference:
            min_difference = current_difference

    return min_difference