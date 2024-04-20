from rectangle import Rectangle
from point import Point

class InputData:
    @staticmethod
    def create_rectangles(number):
        rec_file = open("rectangles.txt", "w")
        for i in range(number):
            rec_file.write(str(10 * i) + " " + str(10 * i) + " " + str(10 * (2 * number - i)) +
                        " " + str(10 * (2 * number - i)) + "\n")

    @staticmethod
    def create_points(number):
        points_file = open("points.txt", "w")
        for i in range(number):
            points_file.write(str(pow(1009 * i, 31) % (20 * number)) + " " + str(pow(1013 * i, 31) % (20 * number)) + "\n")

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