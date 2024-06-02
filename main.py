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
    """
    Minimal example of how to use the parallel_function wrapper
    Returns: None

    """
    array_length = 4000
    params = np.arange(1, array_length)


    # With parallelization
    # Control how many parallel processes
    max_cores = 100
    results = parallel_function(some_heavy_algorithm_2, params, max_workers=max_cores)


if __name__ == "__main__":
    main()
