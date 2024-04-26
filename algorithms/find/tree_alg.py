from base_objects.tree import Tree

class TreeAlgorithm:
    def __init__(self):
        self.tree = Tree()

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

            tree = self.tree.create_tree(0, len(points_x) - 1)
            persistent_trees = [tree]
            new_tree = None

            pref, ind = mas_x_changes[0][0], 0
            while ind <= len(mas_x_changes) - 1:
                if mas_x_changes[ind][0] != pref:
                    persistent_trees.append(new_tree)
                    pref = mas_x_changes[ind][0]

                while ind != len(mas_x_changes) and pref == mas_x_changes[ind][0]:
                    new_tree = self.tree.change_tree(persistent_trees[-1] if not new_tree else new_tree,
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

                compressed_x = self.tree.bin_search(points_x, x)
                compressed_y = self.tree.bin_search(points_y, y)

                if compressed_x == -1 or compressed_y == -1:
                    c = 0
                else:
                    c = self.tree.find(persistent_trees[compressed_y + 1], compressed_x)
        else:
            for _ in range(m):
                x, y = [int(x) for x in input().split()]