import csv

class CSVWriter:
    def __init__(self):
        pass

    def write_to_csv(self, data):
        with open('data.csv', 'w', newline='') as csvfile:
            fieldnames = ['rectangles', 'time_prep', 'time_answer', 'time_total', 'alg']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)