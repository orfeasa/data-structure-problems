from typing import List
import collections


def finder(arr1: List, arr2: List) -> int:
    occurrences_left = collections.defaultdict(int)

    # go through second array
    # populate dictionary with occurrences of each number
    for num in arr2:
        occurrences_left[num] += 1

    # go through second array
    for num in arr1:
        # if num not in dictionary
        if occurrences_left[num] == 0:
            return num
        else:
            # subtract occurrences
            occurrences_left[num] -= 1


def finder2(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num

    return result

