def uni_char(s: str) -> bool:
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True


def uni_char2(s: str) -> bool:
    return len(set(s)) == len(s)
