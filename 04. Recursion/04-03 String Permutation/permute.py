from typing import List


def permute(s: str) -> List[str]:
    # base case
    if len(s) <= 1:
        return [s]

    # Recursively call the permutations of the substring starting after the 1st character
    sublist = permute(s[1:])
    new_list = []
    # for each permutations of the substring create a new one, where the first
    # character is "injected" in between characters of the previous one
    for substr in sublist:
        for pos in range(len(substr)):
            new_list.append(substr[:pos] + s[0] + substr[pos:])
        new_list.append(substr + s[0])

    return new_list
