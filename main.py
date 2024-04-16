from rectangle import Rectangle
from find_algorithms import BruteForceFind, MapFind, TreeFind
from point import Point

if __name__ == "__main__":
    
    rectangles = [
        Rectangle(2, 2, 6, 8),
        Rectangle(5, 4, 9, 10),
        Rectangle(4, 0, 11, 6),
        Rectangle(8, 2, 12, 12)
    ]

    test_points = [Point(2, 2), Point(12, 12), Point(10, 4), Point(5, 5), Point(2, 10), Point(2, 8)]

    points_x = sorted(set(rec.x1 for rec in rectangles) | set(rec.x2 for rec in rectangles))
    points_y = sorted(set(rec.y1 for rec in rectangles) | set(rec.y2 for rec in rectangles))

    print("\nBrute Force:\n")
    for point in test_points:
        result = BruteForceFind.count_rects_with_point_brute(rectangles, point.x, point.y)
        print(f"{point} -> {result}")

    c_map = MapFind.prepare_map(rectangles, points_x, points_y)

    print("\nMap Algorithm:\n")
    for point in test_points:
        result = MapFind.count_rects_with_point_map(c_map, points_x, points_y, point)
        print(f"{point} -> {result}")

    persistent_trees, points_x, points_y = TreeFind.preprocessing(rectangles)

    print("\nPersistent Tree Algorithm:\n")
    TreeFind.algorithm(test_points, persistent_trees, points_x, points_y)