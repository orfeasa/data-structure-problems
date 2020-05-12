def uni_char(s: str) -> bool:
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True
