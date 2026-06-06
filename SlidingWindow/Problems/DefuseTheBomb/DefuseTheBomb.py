def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)

    if k == 0:
        return [0] * n
    
    result = [0] * n

    if k > 0:
        left = 1
        right = k
    else:
        left = n + k
        right = n - 1

    current_sum = 0
    for i in range(left, right + 1):
        current_sum += code[i % n]

    for i in range(n):
        result[i] = current_sum

        current_sum -= code[left % n]
        current_sum += code[(right + 1) % n]

        left += 1
        right += 1
    
    return result

print(decrypt([5,7,1,4], 3))