from concurrent.futures import ProcessPoolExecutor
import multiprocessing
cpu_count = multiprocessing.cpu_count()
def small_func(num):
    return num + 2
test_data = [1,2,3,4,5]
def split_workload(func, args, workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    print("Ready to return data")
    return list(res)
temp_res = split_workload(small_func, test_data, cpu_count)
temp_res