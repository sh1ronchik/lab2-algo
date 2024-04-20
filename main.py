from algorithms.dataIO import data_gen
from algorithms.dataIO import csv
from tests import time_test

def main():
    data_generator = data_gen.DataGenerator()
    algorithm_tester = time_test.AlgorithmTester(data_generator)
    csv_writer = csv.CSVWriter()

    data = []
    # data.extend(algorithm_tester.test_lin_alg())
    # data.extend(algorithm_tester.test_map_alg_prep_and_run())
    data.extend(algorithm_tester.test_tree_alg_prep_and_run())

    csv_writer.write_to_csv(data)

if __name__ == '__main__':
    main()