from typing import List

class Rectangle:
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def contains(self, x: float, y: float) -> bool:
        return self.x1 <= x < self.x2 and self.y1 <= y < self.y2

class Node:
    def __init__(self, left=None, right=None):
        self.left_border, self.right_border = left, right
        self.left_child, self.right_child = None, None
        self.value = 0

def create_tree(left, right):
    node = Node(left, right)
    if left + 1 < right:
        mid = (right + left) // 2
        node.left_child = create_tree(left, mid)
        node.right_child = create_tree(mid, right)
    return node

def copy_without_children(node):
    new_node = Node(node.left_border, node.right_border)
    new_node.value = node.value
    return new_node

def copy_of_node(node, v):
    new_node = Node(node.left_border, node.right_border)
    new_node.value = node.value + v
    new_node.left_child = node.left_child
    new_node.right_child = node.right_child
    return new_node

def change_tree(node, left, right, value):
    if left <= node.left_border and node.right_border <= right:
        return copy_of_node(node, value)
    if right <= node.left_border or node.right_border <= left:
        return node
    new_node = copy_without_children(node)
    new_node.left_child = change_tree(node.left_child, left, right, value)
    new_node.right_child = change_tree(node.right_child, left, right, value)
    return new_node

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

    tree = create_tree(0, len(points_x) - 1)
    persistent_trees = [tree]
    new_tree = None

    pref, ind = mas_x_changes[0][0], 0
    while ind <= len(mas_x_changes) - 1:
        if mas_x_changes[ind][0] != pref:
            persistent_trees.append(new_tree)
            pref = mas_x_changes[ind][0]

        while ind != len(mas_x_changes) and pref == mas_x_changes[ind][0]:
            new_tree = change_tree(persistent_trees[-1] if not new_tree else new_tree,
                                   points_x.index(mas_x_changes[ind][1]), points_x.index(mas_x_changes[ind][2]),
                                   mas_x_changes[ind][3])
            ind += 1

    persistent_trees.append(tree)
    return persistent_trees, points_x, points_y

def find(node, target):
    if not node.right_child and not node.left_child:
        return node.value
    mid = (node.right_border + node.left_border) // 2
    if target < mid:
        return node.value + find(node.left_child, target)
    return node.value + find(node.right_child, target)

def algorithm(points, persistent_trees, points_x, points_y):
    for x, y in points:
        compressed_x = bin_search(points_x, x)
        compressed_y = bin_search(points_y, y)

        if compressed_x == -1 or compressed_y == -1:
            print(0, end=" ")
        else:
            print(find(persistent_trees[compressed_y + 1], compressed_x), end=" ")

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

def read_rectangles_from_file(file_path: str) -> List[Rectangle]:
    rectangles = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                x1, y1, x2, y2 = map(float, line.split())
                rectangles.append(Rectangle(x1, y1, x2, y2))
    return rectangles



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

    persistent_trees, points_x, points_y = preprocessing(rectangles)

    c_map = prepare_map(rectangles, points_x, points_y)

    brute_force_results = []
    for point in test_points:
        result = count_rects_with_point_brute(rectangles, *point)
        brute_force_results.append((point, result))

    print("\nBrute Force:")
    for point, result in brute_force_results:
        print(f"({point[0]}, {point[1]}) -> {result}")

    map_algorithm_results = []
    for point in test_points:
        result = count_rects_with_point_map(c_map, points_x, points_y, *point)
        map_algorithm_results.append((point, result))

    print("\nMap Algorithm:")
    for point, result in map_algorithm_results:
        print(f"({point[0]}, {point[1]}) -> {result}")

    persistent_tree_results = []
    for point in test_points:
        compressed_x = bin_search(points_x, point[0])
        compressed_y = bin_search(points_y, point[1])

        if compressed_x == -1 or compressed_y == -1:
            result = 0
        else:
            result = find(persistent_trees[compressed_y + 1], compressed_x)
        persistent_tree_results.append((point, result))

    print("\nPersistent Tree Algorithm:")
    for point, result in persistent_tree_results:
        print(f"({point[0]}, {point[1]}) -> {result}")