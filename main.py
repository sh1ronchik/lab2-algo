from rectangle import Rectangle
from find_algorithms import BruteForceFind, MapFind, TreeFind

if __name__ == "__main__":
    rectangles = [
        Rectangle(2, 2, 6, 8),
        Rectangle(5, 4, 9, 10),
        Rectangle(4, 0, 11, 6),
        Rectangle(8, 2, 12, 12)
    ]

    test_points = [(2, 2), (12, 12), (10, 4), (5, 5), (2, 10), (2, 8)]

    points_x = sorted(set(rec.x1 for rec in rectangles) | set(rec.x2 for rec in rectangles))
    points_y = sorted(set(rec.y1 for rec in rectangles) | set(rec.y2 for rec in rectangles))

    print("\nBrute Force:\n")
    for point in test_points:
        result = BruteForceFind.count_rects_with_point_brute(rectangles, *point)
        print(f"({point[0]}, {point[1]}) -> {result}")

    c_map = MapFind.prepare_map(rectangles, points_x, points_y)

    print("\nMap Algorithm:\n")
    for point in test_points:
        result = MapFind.count_rects_with_point_map(c_map, points_x, points_y, *point)
        print(f"({point[0]}, {point[1]}) -> {result}")

    persistent_trees, points_x, points_y = TreeFind.preprocessing(rectangles)

    print("\nPersistent Tree Algorithm:\n")
    TreeFind.algorithm(test_points, persistent_trees, points_x, points_y)