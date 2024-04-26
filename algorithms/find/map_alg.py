class MapAlgorithm:
    def __init__(self, rectangles_file_path, points_file_path):
        self.rectangles_file_path = rectangles_file_path
        self.points_file_path = points_file_path
        self.rectangles = []
        self.points = []
        self.c_map = []
        self.points_x = []
        self.points_y = []

    def bin_search(self, mass, target):
        if target < mass[0] or target >= mass[-1]:
            return -1
        left, right = 0, len(mass)
        while right - left > 1:
            mid = (right + left) // 2
            if mass[mid] > target:
                right = mid
            else:
                left = mid
        return left

    def read_rectangles(self):
        with open(self.rectangles_file_path, "r") as rec_file:
            self.rectangles = [[int(x) for x in rec_file.readline().split()] for _ in range(len(self.rectangles))]

    def read_points(self):
        with open(self.points_file_path, "r") as points_file:
            self.points = [[int(x) for x in points_file.readline().split()] for _ in range(len(self.points))]

    def preprocessing(self):
        self.read_rectangles()
        self.read_points()
        self.points_x, self.points_y = list(set(point[0] for point in self.points)), \
                                        list(set(point[1] for point in self.points))
        self.points_x.sort()
        self.points_y.sort()
        self.c_map = [[0] * (len(self.points_x) - 1) for _ in range(len(self.points_y) - 1)]
        for rec in self.rectangles:
            compressed_x1 = self.points_x.index(rec[0])
            compressed_y1 = self.points_y.index(rec[1])
            compressed_x2 = self.points_x.index(rec[2])
            compressed_y2 = self.points_y.index(rec[3])
            for x in range(compressed_x1, compressed_x2):
                for y in range(compressed_y1, compressed_y2):
                    self.c_map[len(self.points_y) - 2 - y][x] += 1

    def algorithm(self):
        for point in self.points:
            compressed_x = self.bin_search(self.points_x, point[0])
            compressed_y = self.bin_search(self.points_y, point[1])
            c = 0 if compressed_x == -1 or compressed_y == -1 \
                  else self.c_map[len(self.points_y) - 2 - compressed_y][compressed_x]