from collections import Counter

def countGoodSubstrings(s: str) -> int:
    
    if len(s) < 3:
        return 0

    window_counter = Counter(s[:3])

    count = 1 if len(window_counter) == 3 else 0

    for i in range(0, len(s) - 3):
        trailing_char = s[i]
        leading_char = s[i + 3]

        window_counter[trailing_char] -= 1
        if window_counter[trailing_char] == 0:
            del window_counter[trailing_char]

        window_counter[leading_char] += 1

        if len(window_counter) == 3:
            count += 1

    return count

print(countGoodSubstrings("xyzzaz"))