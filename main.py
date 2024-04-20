import time
from find_algorithms import BruteForceFind, MapFind, TreeFind
from input_data import InputData 

if __name__ == "__main__":
    points_file_path = 'points.txt'
    rectangles_file_path = 'rectangles.txt'

    InputData.create_rectangles(2**8)
    InputData.create_points(100000)

    test_points = InputData.read_points(points_file_path) 
    rectangles = InputData.read_rectangles(rectangles_file_path) 

    points_x = sorted(set(rec.x1 for rec in rectangles) | set(rec.x2 for rec in rectangles))
    points_y = sorted(set(rec.y1 for rec in rectangles) | set(rec.y2 for rec in rectangles))

    print("\nBrute Force:\n")
    start_time = time.time()
    for point in test_points:
        BruteForceFind.algorithm(rectangles, point.x, point.y)
    end_time = time.time()
    print(f"Algorithm worked. Time taken: {end_time - start_time} seconds.")

    print("\nMap Algorithm:\n")
    start_time = time.time()
    c_map = MapFind.prepairing(rectangles, points_x, points_y)
    for point in test_points:
        MapFind.algorithm(c_map, points_x, points_y, point)
    end_time = time.time()
    print(f"Algorithm worked. Time taken: {end_time - start_time} seconds.")

    print("\nPersistent Tree Algorithm:\n")

    start_time = time.time()
    persistent_trees, points_x, points_y = TreeFind.preprocessing(rectangles)
    TreeFind.algorithm(test_points, persistent_trees, points_x, points_y)
    end_time = time.time()
    print(f"Algorithm worked. Time taken: {end_time - start_time} seconds.")