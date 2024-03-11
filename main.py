from typing import List

class Rectangle:
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def contains(self, x: float, y: float) -> bool:
        return self.x1 <= x < self.x2 and self.y1 <= y < self.y2

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

def prepare_map(rectangles: List[Rectangle], points_x: List[float], points_y: List[float]) -> List[List[int]]:
    c_map = [[0] * (len(points_x) - 1) for _ in range(len(points_y) - 1)]
    for rec in rectangles:
        compressed_x1, compressed_x2 = map(points_x.index, [rec.x1, rec.x2])
        compressed_y1, compressed_y2 = map(points_y.index, [rec.y1, rec.y2])
        for x in range(compressed_x1, compressed_x2):
            for y in range(compressed_y1, compressed_y2):
                c_map[len(points_y) - 2 - y][x] += 1
    return c_map

def count_rects_with_point_map(c_map: List[List[int]], points_x: List[float], points_y: List[float], x: float, y: float) -> int:
    compressed_x, compressed_y = bin_search(points_x, x), bin_search(points_y, y)
    return 0 if compressed_x == -1 or compressed_y == -1 else c_map[len(points_y) - 2 - compressed_y][compressed_x]

def count_rects_with_point_brute(rectangles: List[Rectangle], x: float, y: float) -> int:
    return sum(1 for rec in rectangles if rec.contains(x, y))

if __name__ == "__main__":
    rectangles = [
        Rectangle(2, 2, 6, 8),
        Rectangle(5, 4, 9, 10),
        Rectangle(4, 0, 11, 6),
        Rectangle(8, 2, 12, 12)
    ]

    points_x = sorted(set(rec.x1 for rec in rectangles) | set(rec.x2 for rec in rectangles))
    points_y = sorted(set(rec.y1 for rec in rectangles) | set(rec.y2 for rec in rectangles))

    c_map = prepare_map(rectangles, points_x, points_y)

    test_points = [(2, 2), (12, 12), (10, 4), (5, 5), (2, 10), (2, 8)]

    print("Brute Force:")
    for point in test_points:
        result = count_rects_with_point_brute(rectangles, *point)
        print(f"({point[0]}, {point[1]}) -> {result}")

    print("\nMap Algorithm:")
    for point in test_points:
        result = count_rects_with_point_map(c_map, points_x, points_y, *point)
        print(f"({point[0]}, {point[1]}) -> {result}")