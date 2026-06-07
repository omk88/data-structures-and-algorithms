def minimumRecolors(blocks: str, k: int) -> int:
    current_whites = blocks[:k].count('W')
    min_operations = current_whites

    for i in range(k, len(blocks)):
        if blocks[i] == 'W':
            current_whites += 1

        if blocks[i - k] == 'W':
            current_whites -= 1

        if current_whites < min_operations:
            min_operations = current_whites

    return min_operations

print(minimumRecolors("WBBWWBBWBW", 7))