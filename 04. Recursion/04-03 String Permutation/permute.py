from typing import List


def permute(s: str) -> List[str]:
    # base case
    if len(s) <= 1:
        return [s]

    # Recursively call the permutations of the substring starting after the 1st character
    sublist = permute(s[1:])
    out = []
    # for each permutations of the substring create a new one, where the first
    # character is "injected" in between characters of the previous one
    for substr in sublist:
        for pos in range(len(substr)):
            out.append(substr[:pos] + s[0] + substr[pos:])
        out.append(substr + s[0])

    return out


def permute2(s: str) -> List[str]:
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, letter in enumerate(s):

            # For every permutation without that letter
            for perm in permute(s[:i] + s[i + 1 :]):

                # Add it to output
                out += [letter + perm]

    return out
