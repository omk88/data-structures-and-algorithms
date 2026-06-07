def maximumStrongPairXor(nums: List[int]) -> int:
    nums.sort()

    max_xor = 0
    start = 0

    for end in range(len(nums)):

        while nums[end] > 2 * nums[start]:
            start += 1


        for i in range(start, end + 1):
            current_xor = nums[end] ^ nums[i]

            if current_xor > max_xor:
                max_xor = current_xor


    return max_xor

print(maximumStrongPairXor([1,2,3,4,5]))