from typing import List


def finder(arr1: List, arr2: List) -> int:
    occurrences_left = {}

    # go through first array
    # populate dictionary with occurrences of each number
    for num in arr1:
        occurrences_left.setdefault(num, 0)
        occurrences_left[num] += 1

    # go through second array
    for num in arr2:
        # subtract occurrences
        occurrences_left[num] -= 1
        if occurrences_left[num] == 0:
            # if occurrence is 0 remove from dict
            del occurrences_left[num]

    missing_element = next(iter(occurrences_left))

    return missing_element
