from rectangle import Rectangle
from tree import Tree
from find_algorithms import BruteForceFind, MapFind
from bin_search import bin_search

def preprocessing(rectangles):
    points_x, points_y = set(), set()
    mas_x_changes = []
    for rec in rectangles:
        points_x.add(rec.x1)
        points_x.add(rec.x2)
        points_y.add(rec.y1)
        points_y.add(rec.y2)

        mas_x_changes.append([rec.y1, rec.x1, rec.x2, 1])
        mas_x_changes.append([rec.y2, rec.x1, rec.x2, -1])

    points_x, points_y = list(points_x), list(points_y)
    points_x.sort()
    points_y.sort()
    mas_x_changes = sorted(mas_x_changes, key=lambda x: x[0])

    tree_instance = Tree()
    tree = tree_instance.create_tree(0, len(points_x) - 1)
    persistent_trees = [tree]
    new_tree = None

    pref, ind = mas_x_changes[0][0], 0
    while ind <= len(mas_x_changes) - 1:
        if mas_x_changes[ind][0] != pref:
            persistent_trees.append(new_tree)
            pref = mas_x_changes[ind][0]

        while ind != len(mas_x_changes) and pref == mas_x_changes[ind][0]:
            new_tree = tree_instance.change_tree(persistent_trees[-1] if not new_tree else new_tree,
                                                 points_x.index(mas_x_changes[ind][1]), points_x.index(mas_x_changes[ind][2]),
                                                 mas_x_changes[ind][3])
            ind += 1

    persistent_trees.append(tree)
    return persistent_trees, points_x, points_y


def algorithm(points, persistent_trees, points_x, points_y):
    tree_instance = Tree()
    
    for x, y in points:
        compressed_x = bin_search(points_x, x)
        compressed_y = bin_search(points_y, y)

        if compressed_x == -1 or compressed_y == -1:
            print(0, end=" ")
        else:
            print(tree_instance.find(persistent_trees[compressed_y + 1], compressed_x), end=" ")



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

    tree_instance = Tree()
    persistent_trees, points_x, points_y = preprocessing(rectangles)

    persistent_tree_results = []
    for point in test_points:
        compressed_x = bin_search(points_x, point[0])
        compressed_y = bin_search(points_y, point[1])

        if compressed_x == -1 or compressed_y == -1:
            result = 0
        else:
            result = tree_instance.find(persistent_trees[compressed_y + 1], compressed_x)
        persistent_tree_results.append((point, result))

    print("\nPersistent Tree Algorithm:\n")
    for point, result in persistent_tree_results:
        print(f"({point[0]}, {point[1]}) -> {result}")