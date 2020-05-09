# Cheating
def anagram2(s1: str, s2: str) -> bool:
    string1 = "".join(sorted(s1.lower())).strip()
    string2 = "".join(sorted(s2.lower())).strip()
    return string1 == string2


def anagram(s1: str, s2: str) -> bool:
    # initialize strings and ignore spaces
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    # create map of characters in first string
    char_map = {}

    for char in s1:
        char_map.setdefault(char, 0)
        char_map[char] += 1

    # check if the 2nd string has the same characters in the same amounts
    for char in s2:
        if char in char_map:
            char_map[char] -= 1
        else:
            # character does not exist in 1st string
            return False

    for char in char_map:
        if char_map[char] != 0:
            # character has different number of occurrences in 1st string
            return False

    return True
