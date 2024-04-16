from typing import List

def bin_search(mass: List[float], target: float) -> int:
    if target < mass[0] or target >= mass[-1]:
        return -1
    left, right = 0, len(mass)
    while right - left > 1:
        mid = (right + left) // 2
        mid_value = mass[mid]
        left = mid if mid_value <= target else left
        right = mid if mid_value > target else right
    return left