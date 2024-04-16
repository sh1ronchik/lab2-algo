from typing import List
from rectangle import Rectangle
from bin_search import bin_search

class BruteForceFind:
    @staticmethod
    def count_rects_with_point_brute(rectangles: List[Rectangle], x: float, y: float) -> int:
        return sum(1 for rec in rectangles if rec.contains(x, y))
    
class MapFind:
    @staticmethod
    def prepare_map(rectangles: List[Rectangle], points_x: List[float], points_y: List[float]) -> List[List[int]]:
        c_map = [[0] * (len(points_x) - 1) for _ in range(len(points_y) - 1)]
        for rec in rectangles:
            compressed_x1, compressed_x2 = map(points_x.index, [rec.x1, rec.x2])
            compressed_y1, compressed_y2 = map(points_y.index, [rec.y1, rec.y2])
            for x in range(compressed_x1, compressed_x2):
                for y in range(compressed_y1, compressed_y2):
                    c_map[len(points_y) - 2 - y][x] += 1
        return c_map

    @staticmethod
    def count_rects_with_point_map(c_map: List[List[int]], points_x: List[float], points_y: List[float], x: float, y: float) -> int:
        compressed_x, compressed_y = bin_search(points_x, x), bin_search(points_y, y)
        return 0 if compressed_x == -1 or compressed_y == -1 else c_map[len(points_y) - 2 - compressed_y][compressed_x]