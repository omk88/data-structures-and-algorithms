class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        k_beauty = 0

        for i in range(len(num_str) - k + 1):
            window_str = num_str[i : i + k]

            window_int = int(window_str)

            if window_int != 0 and num % window_int == 0:
                k_beauty += 1

        return k_beauty