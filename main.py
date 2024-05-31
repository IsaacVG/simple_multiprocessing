import numpy as np
import time
from simple_multiprocessing import parallel_function
from secrets import randbelow

def some_heavy_algorithm(param):
    result = 1
    for i in range(2, param + 1):
        result *= i
    return result

def some_heavy_algorithm_2(param):
    N=param
    count = 0

    i = 2
    cur_prime = 0
    while not count == N:
        j = 2
        isPrime = True
        while j * j <= i:
            if i % j == 0:
                isPrime = False
            j = j + 1
        if isPrime == True:
            count = count + 1
            cur_prime = i
        i = i + 1

    return cur_prime

def main():

    array_length = 3000
    samples = 3
    test_idx = [randbelow(array_length) for _ in range(samples)]
    params = np.arange(1, array_length)

    # Without parallelization
    start_time = time.time()
    results = [some_heavy_algorithm_2(param) for param in params]
    end_time = time.time()
    for test in test_idx:
        print(f"{results[test]}")
    print(f"Time taken without parallelization: {end_time - start_time} seconds")

    # With parallelization
    start_time = time.time()
    # Control how many parallel processes
    max_cores = 100
    results = parallel_function(some_heavy_algorithm_2, params, max_workers=max_cores)
    for test in test_idx:
        print(f"{results[test]}")
    end_time = time.time()
    print(f"Time taken with parallelization: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
