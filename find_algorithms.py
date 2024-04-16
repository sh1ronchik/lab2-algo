from typing import List
from rectangle import Rectangle
from bin_search import bin_search
from tree import Tree

class BruteForceFind:

    @staticmethod
    def count_rects_with_point_brute(rectangles: List[Rectangle], x: float, y: float) -> int:
        """
        Counts the number of rectangles that contain the given point using a brute force approach.

        :param rectangles: A list of Rectangle objects.
        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        :return: The number of rectangles containing the point.
        """
        return sum(1 for rec in rectangles if rec.contains(x, y))

class MapFind:

    @staticmethod
    def prepare_map(rectangles: List[Rectangle], points_x: List[float], points_y: List[float]) -> List[List[int]]:
        """
        Prepares a map for efficient point containment queries.

        :param rectangles: A list of Rectangle objects.
        :param points_x: A sorted list of x-coordinates.
        :param points_y: A sorted list of y-coordinates.
        :return: A 2D list representing the map.
        """
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
        """
        Counts the number of rectangles containing the given point using the prepared map.

        :param c_map: The prepared map.
        :param points_x: A sorted list of x-coordinates.
        :param points_y: A sorted list of y-coordinates.
        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        :return: The number of rectangles containing the point.
        """
        compressed_x, compressed_y = bin_search(points_x, x), bin_search(points_y, y)
        return 0 if compressed_x == -1 or compressed_y == -1 else c_map[len(points_y) - 2 - compressed_y][compressed_x]

class TreeFind:

    @staticmethod
    def preprocessing(rectangles):
        """
        Preprocesses the rectangles to prepare for efficient point containment queries.

        :param rectangles: A list of Rectangle objects.
        :return: A list of persistent trees and the sorted x and y coordinates.
        """
        tree_instance = Tree()
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

    @staticmethod
    def algorithm(points, persistent_trees, points_x, points_y):
        """
        Counts the number of rectangles containing each point using the persistent trees.

        :param points: A list of points to check.
        :param persistent_trees: A list of persistent trees.
        :param points_x: A sorted list of x-coordinates.
        :param points_y: A sorted list of y-coordinates.
        """
        tree_instance = Tree()
        for x, y in points:
            compressed_x = bin_search(points_x, x)
            compressed_y = bin_search(points_y, y)

            if compressed_x == -1 or compressed_y == -1:
                result = 0
            else:
                result = tree_instance.find(persistent_trees[compressed_y + 1], compressed_x)
            
            print(f"({x}, {y}) -> {result}")