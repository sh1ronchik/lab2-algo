from time import perf_counter
from algorithms.find import lin_search, map_alg, tree_alg

class AlgorithmTester:
    def __init__(self, data_generator):
        self.data_generator = data_generator

    def test_lin_alg(self):
        data = []
        for i in range(3):
            self.data_generator.create_rectangles(2 ** i)
            time_prep_sum = 0
            time_answer_sum = 0
            begin = perf_counter()
            lin_search_instance = lin_search.LinearSearch("data/rectangles.txt", "data/points.txt")
            lin_search_instance.preprocessing()
            time_prep_sum += perf_counter() - begin
            begin = perf_counter()
            lin_search_instance.algorithm()
            time_answer_sum += perf_counter() - begin  
            data.append({
                'rectangles': 2 ** i,
                'time_prep': time_prep_sum,
                'time_answer': time_answer_sum,
                'time_total': time_prep_sum + time_answer_sum,
                'alg': 'lin'
            })
        return data

    def test_map_alg_prep_and_run(self):
        data = []
        for i in range(3):
            self.data_generator.create_rectangles(2 ** i)
            time_prep_sum = 0
            time_answer_sum = 0
            begin = perf_counter()
            map_algorithm = map_alg.MapAlgorithm("data/rectangles.txt", "data/points.txt")
            map_algorithm.preprocessing()
            time_prep_sum += perf_counter() - begin
            begin = perf_counter()
            map_algorithm.algorithm()
            time_answer_sum += perf_counter() - begin 
            data.append({
                'rectangles': 2 ** i,
                'time_prep': time_prep_sum,
                'time_answer': time_answer_sum,
                'time_total': time_prep_sum + time_answer_sum,
                'alg': 'map'
            })
        return data

    def test_tree_alg_prep_and_run(self):
        data = []
        tree_algorithm = tree_alg.TreeAlgorithm() 
        for i in range(3):
            self.data_generator.create_rectangles(2 ** i)
            time_prep_sum = 0
            time_answer_sum = 0
            begin = perf_counter()
            t_map, points_x, points_y = tree_algorithm.preprocessing(2 ** i) 
            time_prep_sum += perf_counter() - begin
            begin = perf_counter()
            tree_algorithm.algorithm(100000, t_map, points_x, points_y) 
            time_answer_sum += perf_counter() - begin
            data.append({
                'rectangles': 2 ** i,
                'time_prep': time_prep_sum,
                'time_answer': time_answer_sum,
                'time_total': time_prep_sum + time_answer_sum,
                'alg': 'tree'
            })
        return data