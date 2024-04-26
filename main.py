from algorithms.dataIO import data_gen
from algorithms.dataIO import csv
from tests.test import time_test
from tests.test_graph.make_graph import create_preparation_graph 

def main():
    data_generator = data_gen.DataGenerator()
    algorithm_tester = time_test.AlgorithmTester(data_generator)
    csv_writer = csv.CSVWriter()

    data = []
    data.extend(algorithm_tester.test_lin_alg())
    data.extend(algorithm_tester.test_map_alg_prep_and_run())
    data.extend(algorithm_tester.test_tree_alg_prep_and_run())

    csv_writer.write_to_csv(data)

    create_preparation_graph("time_prep")
    create_preparation_graph("time_answer")
    create_preparation_graph("time_total")

if __name__ == '__main__':
    main()