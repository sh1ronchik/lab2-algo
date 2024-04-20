class DataGenerator:
    def create_rectangles(self, number):
        with open("data/rectangles.txt", "w") as rec_file:
            rec_file.writelines(f"{10 * i} {10 * i} {10 * (2 * number - i)} {10 * (2 * number - i)}\n" for i in range(number))

    def create_points(self, number):
        with open("data/points.txt", "w") as points_file:
            points_file.writelines(f"{pow(1009 * i, 31) % (20 * number)} {pow(1013 * i, 31) % (20 * number)}\n" for i in range(number))