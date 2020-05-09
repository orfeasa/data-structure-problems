from typing import List


def pair_sum(arr: List, k: int) -> int:
    seen = set()
    output = set()

    # for each array element
    for num in arr:
        # check if k - num is also in the array
        if k - num in seen:
            output.add((min(num, k - num), max(num, k - num)))

        # add current number to the numbers seen
        # this should be after the check to count pairs of the same value correctly
        seen.add(num)

    print(output)
    return len(output)
