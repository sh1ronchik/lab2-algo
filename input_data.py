from rectangle import Rectangle
from point import Point

class InputData:
    @staticmethod
    def read_points(file_path):
        points = []
        with open(file_path, 'r') as file:
            for line in file:
                x, y = map(float, line.strip().split())
                points.append(Point(x, y))
        return points

    @staticmethod
    def read_rectangles(file_path):
        rectangles = []
        with open(file_path, 'r') as file:
            for line in file:
                x1, y1, x2, y2 = map(float, line.strip().split())
                rectangles.append(Rectangle(x1, y1, x2, y2))
        return rectangles