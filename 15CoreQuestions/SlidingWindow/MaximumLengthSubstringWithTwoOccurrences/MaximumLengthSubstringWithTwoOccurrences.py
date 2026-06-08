def maximumLengthSubstring(s: str) -> int:
    start = 0
    max_length = 0
    char_counts = {}

    for end in range(len(s)):
        incoming_char = s[end]

        char_counts[incoming_char] = char_counts.get(incoming_char, 0) + 1

        while char_counts[incoming_char] > 2:
            outgoing_char = s[start]
            char_counts[outgoing_char] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length