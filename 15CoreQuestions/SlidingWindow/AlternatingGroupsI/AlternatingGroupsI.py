def numberOfAlternatingGroups(colors: List[int]) -> int:
    n = len(colors)
    alternating_groups = 0

    for i in range(n):
        left_tile = colors[i - 1]

        mid_tile = colors[i]

        right_tile = colors[(i + 1) % n]

        if mid_tile != left_tile and mid_tile != right_tile:
            alternating_groups += 1

    return alternating_groups