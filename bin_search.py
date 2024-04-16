from typing import List

def bin_search(mass: List[float], target: float) -> int:
    """
    Performs a binary search on the given list to find the index of the target value.

    :param mass: The list to search.
    :param target: The value to find.
    :return: The index of the target value in the list, or -1 if not found.
    """
    if target < mass[0] or target >= mass[-1]:
        return -1
    left, right = 0, len(mass)
    while right - left > 1:
        mid = (right + left) // 2
        mid_value = mass[mid]
        left = mid if mid_value <= target else left
        right = mid if mid_value > target else right
    return left