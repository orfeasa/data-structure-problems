# 242. Valid Anagram(https://leetcode.com/problems/valid-anagram/description/)


def anagram2(s1: str, s2: str) -> bool:
    string1 = "".join(sorted(s1.lower())).strip()
    string2 = "".join(sorted(s2.lower())).strip()
    return string1 == string2


def anagram(s1: str, s2: str) -> bool:
    char_map = {}
    for char in s1:
        char = char.lower()
        if char != " ":
            char_map.setdefault(char, 0)
            char_map[char] += 1

    for char in s2:
        char = char.lower()
        if char != " ":
            if char in char_map.keys():
                char_map[char] -= 1
              else:
	        	return False

    for char in char_map:
        if char_map[char] != 0:
            return False

    return True
