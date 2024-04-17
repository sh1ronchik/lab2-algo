from find_algorithms import BruteForceFind, MapFind, TreeFind
from input_data import InputData 

if __name__ == "__main__":
    points_file_path = 'points.txt'
    rectangles_file_path = 'rectangles.txt'

    test_points = InputData.read_points(points_file_path) 
    rectangles = InputData.read_rectangles(rectangles_file_path) 

    points_x = sorted(set(rec.x1 for rec in rectangles) | set(rec.x2 for rec in rectangles))
    points_y = sorted(set(rec.y1 for rec in rectangles) | set(rec.y2 for rec in rectangles))

    print("\nBrute Force:\n")
    for point in test_points:
        BruteForceFind.count_rects_with_point_brute(rectangles, point.x, point.y)
    print("Algorithm worked.")

    c_map = MapFind.prepare_map(rectangles, points_x, points_y)

    print("\nMap Algorithm:\n")
    for point in test_points:
        MapFind.count_rects_with_point_map(c_map, points_x, points_y, point)
    print("Algorithm worked.")

    persistent_trees, points_x, points_y = TreeFind.preprocessing(rectangles)

    print("\nPersistent Tree Algorithm:\n")
    TreeFind.algorithm(test_points, persistent_trees, points_x, points_y)
    print("Algorithm worked.")