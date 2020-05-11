from typing import List


def large_cont_sum(arr: List) -> int:
    # Potential starting points are positive numbers following a negative number (or start of the array if positive)
    # Potential ending points are positive numbers followed by a negative number (or end of the array if positive)
    potential_start_points = []
    potential_end_points = []

    if arr[0] > 0:
        potential_start_points.append(0)

    for ind in range(len(arr)):
        if ind == 0:
            continue

        if arr[ind - 1] < 0 and arr[ind] > 0:
            potential_start_points.append(ind)

        if arr[ind] < 0 and arr[ind - 1] > 0:
            potential_end_points.append(ind - 1)

    if arr[-1] > 0:
        potential_end_points.append(len(arr) - 1)

    # Check all potential starting and ending points
    max_sum = arr[0]
    max_range = (0, 0)
    for start in potential_start_points:
        for end in potential_end_points:
            current_sum = sum(arr[start : end + 1])
            if current_sum > max_sum:
                max_sum = current_sum
                max_range = (start, end)

    # the range is available to return (variable max_range)
    return max_sum
