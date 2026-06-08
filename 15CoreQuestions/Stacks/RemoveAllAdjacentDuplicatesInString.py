def removeDuplicates(s: str) -> str:
    stk = []

    for char in s:
        if stk and stk[-1] == char:
            stk.pop()
        else:
            stk.append(char)

    return "".join(stk)