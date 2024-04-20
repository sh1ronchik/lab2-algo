from base_objects.node import Node

class TreeAlgorithm:
    def __init__(self):
        self.root = None

    def create_tree(self, left, right):
        node = Node(left, right)
        if left + 1 < right:
            mid = (right + left) // 2
            node.left_child = self.create_tree(left, mid)
            node.right_child = self.create_tree(mid, right)
        return node

    def change_tree(self, node, left, right, value):
        if left <= node.left_border and node.right_border <= right:
            return node.copy_of_node(value)
        if right <= node.left_border or node.right_border <= left:
            return node
        new_node = node.copy_without_children()
        new_node.left_child = self.change_tree(node.left_child, left, right, value)
        new_node.right_child = self.change_tree(node.right_child, left, right, value)
        return new_node

    def find(self, node, target):
        if not node.right_child and not node.left_child:
            return node.value
        mid = (node.right_border + node.left_border) // 2
        if target < mid:
            return node.value + self.find(node.left_child, target)
        return node.value + self.find(node.right_child, target)

    def bin_search(self, mass, target):
        if target < mass[0] or target > mass[-1]:
            return -1
        left, right = 0, len(mass)
        while right - left > 1:
            mid = (right + left) // 2
            if mass[mid] >= target:
                right = mid
            else:
                left = mid
        if mass[right] == target:
            return right
        return left

    def preprocessing(self, n):
        if n:
            rec_file = open("data/rectangles.txt", "r")
            mas_x_changes = []
            points_x, points_y = set(), set()
            for _ in range(n):
                points = [int(x) for x in rec_file.readline().split()]

                points_x.add(points[0])
                points_x.add(points[2])
                points_y.add(points[1])
                points_y.add(points[3])

                mas_x_changes.append([points[1], points[0], points[2], 1])
                mas_x_changes.append([points[3], points[0], points[2], -1])

            points_x, points_y = list(points_x), list(points_y)
            points_x.sort()
            points_y.sort()
            mas_x_changes = sorted(mas_x_changes, key=lambda x: x[0])

            tree = self.create_tree(0, len(points_x) - 1)
            persistent_trees = [tree]
            new_tree = None

            pref, ind = mas_x_changes[0][0], 0
            while ind <= len(mas_x_changes) - 1:
                if mas_x_changes[ind][0] != pref:
                    persistent_trees.append(new_tree)
                    pref = mas_x_changes[ind][0]

                while ind != len(mas_x_changes) and pref == mas_x_changes[ind][0]:
                    new_tree = self.change_tree(persistent_trees[-1] if not new_tree else new_tree,
                                        points_x.index(mas_x_changes[ind][1]), points_x.index(mas_x_changes[ind][2]),
                                        mas_x_changes[ind][3])
                    ind += 1

            persistent_trees.append(tree)
            return persistent_trees, points_x, points_y

    def algorithm(self, m, persistent_trees, points_x, points_y):
        rec_file = open("data/points.txt", "r")
        if persistent_trees is not False:
            for _ in range(m):
                x, y = [int(x) for x in rec_file.readline().split()]

                compressed_x = self.bin_search(points_x, x)
                compressed_y = self.bin_search(points_y, y)

                if compressed_x == -1 or compressed_y == -1:
                    c = 0
                else:
                    c = self.find(persistent_trees[compressed_y + 1], compressed_x)
        else:
            for _ in range(m):
                x, y = [int(x) for x in input().split()]