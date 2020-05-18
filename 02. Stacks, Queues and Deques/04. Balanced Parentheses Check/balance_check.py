def balance_check(s: str) -> bool:
    stack = []

    # Check for even number
    if len(s) % 2 != 0:
        return False

    # set up pairs so that keys are closing and values are opening
    pairs = {
        "]": "[",
        "}": "{",
        ")": "(",
    }

    for char in s:
        # if it's an opening
        if char in pairs.values():
            # add to the stack
            stack.append(char)
        # if it's a closing
        elif char in pairs:
            # if the stack is not empty, and the closing corresponds to the last opening
            if len(stack) != 0 and stack[-1] == pairs[char]:
                # remove the respective opening
                stack.pop()
            else:
                return False

    return len(stack) == 0
