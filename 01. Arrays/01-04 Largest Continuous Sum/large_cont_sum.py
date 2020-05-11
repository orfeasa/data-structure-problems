from typing import List


def large_cont_sum(arr: List) -> int:
    max_sum = arr[0]
    current_range = max_range = (0, 0)
    current_sum = 0

    for ind, num in enumerate(arr):
        if current_sum <= 0:
            # start a new sequence at the current element
            current_sum = num
            current_range = (ind, ind)
        else:
            # extend current sequence
            current_sum += num
            current_range = (current_range[0], ind)

        if current_sum > max_sum:
            max_sum = current_sum
            max_range = current_range

    # the range is available to return (variable max_range)
    return max_sum
