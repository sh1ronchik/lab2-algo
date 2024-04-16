from typing import List
from rectangle import Rectangle

class BruteForceFind:
    @staticmethod
    def count_rects_with_point_brute(rectangles: List[Rectangle], x: float, y: float) -> int:
        return sum(1 for rec in rectangles if rec.contains(x, y))