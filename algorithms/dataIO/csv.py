import csv

class CSVWriter:
    def write_to_csv(self, data):
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['rectangles', 'time_prep', 'time_answer', 'time_total', 'alg'])
            writer.writeheader()
            writer.writerows(data)