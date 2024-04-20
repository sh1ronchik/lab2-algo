class DataGenerator:
    def __init__(self):
        pass

    def create_rectangles(self, number):
        with open("data/rectangles.txt", "w") as rec_file:
            for i in range(number):
                rec_file.write(f"{10 * i} {10 * i} {10 * (2 * number - i)} {10 * (2 * number - i)}\n")

    def create_points(self, number):
        with open("data/points.txt", "w") as points_file:
            for i in range(number):
                points_file.write(f"{pow(1009 * i, 31) % (20 * number)} {pow(1013 * i, 31) % (20 * number)}\n")