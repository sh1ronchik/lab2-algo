class LinearSearch:
    def __init__(self, rectangles_file_path, points_file_path):
        self.rectangles_file_path = rectangles_file_path
        self.points_file_path = points_file_path
        self.rectangles = []
        self.points = []

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return [[int(x) for x in line.split()] for line in file]

    def read_rectangles(self):
        self.rectangles = self.read_file(self.rectangles_file_path)

    def read_points(self):
        self.points = self.read_file(self.points_file_path)

    def preprocessing(self):
        pass

    def algorithm(self):
        self.read_rectangles()
        self.read_points()
        for point in self.points:
            counter = sum(1 for rectangle in self.rectangles if rectangle[0] <= point[0] < rectangle[2] and rectangle[1] <= point[1] < rectangle[3])