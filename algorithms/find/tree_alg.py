from base_objects.tree import Tree

class TreeAlgorithm:
    def __init__(self):
        self.tree = Tree()

    def preprocessing(self, n):
        if not n:
            return [], [], []

        with open("data/rectangles.txt", "r") as rec_file:
            mas_x_changes = []
            points_x, points_y = set(), set()
            for _ in range(n):
                points = list(map(int, rec_file.readline().split()))
                points_x.update([points[0], points[2]])
                points_y.update([points[1], points[3]])
                mas_x_changes.extend([[points[1], points[0], points[2], 1], [points[3], points[0], points[2], -1]])

            points_x, points_y = sorted(list(points_x)), sorted(list(points_y))
            mas_x_changes.sort(key=lambda x: x[0])

            tree = self.tree.create_tree(0, len(points_x) - 1)
            persistent_trees = [tree]
            new_tree = None

            for change in mas_x_changes:
                if not persistent_trees or change[0] != persistent_trees[-1][0]:
                    persistent_trees.append(new_tree)
                new_tree = self.tree.change_tree(persistent_trees[-1] if not new_tree else new_tree,
                                                 points_x.index(change[1]), points_x.index(change[2]),
                                                 change[3])

            persistent_trees.append(tree)
            return persistent_trees, points_x, points_y

    def algorithm(self, m, persistent_trees, points_x, points_y):
        if not persistent_trees:
            return

        with open("data/points.txt", "r") as rec_file:
            for _ in range(m):
                x, y = list(map(int, rec_file.readline().split()))
                compressed_x = self.tree.bin_search(points_x, x)
                compressed_y = self.tree.bin_search(points_y, y)

                if compressed_x == -1 or compressed_y == -1:
                    continue

                self.tree.find(persistent_trees[compressed_y + 1], compressed_x)