from typing import List


def pair_sum(arr: List, k: int) -> int:
    count = 0
    pairs = []
    # for each array element
    for ele in arr:
        # check if k - element is also in the array
        # check if we already counted that pair
        if (
            k - ele in arr
            and (ele, k - ele) not in pairs
            and (k - ele, ele) not in pairs
        ):
            count += 1
            pairs += [(ele, k - ele)]
    print(pairs)
    return count
