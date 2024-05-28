import numpy as np
import time
from simple_multiprocessing import parallel_function

def some_heavy_algorithm(param):
    result = 1
    for i in range(2, param + 1):
        result *= i
    return None

def main():

    params = np.arange(1, 10001)

    # Without parallelization
    start_time = time.time()
    results = [some_heavy_algorithm(param) for param in params]
    end_time = time.time()
    print(f"Time taken without parallelization: {end_time - start_time} seconds")

    # With parallelization
    start_time = time.time()
    # Control how many parallel processes
    max_cores = 100
    results = parallel_function(some_heavy_algorithm, params, max_workers=max_cores)
    end_time = time.time()
    print(f"Time taken with parallelization: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
