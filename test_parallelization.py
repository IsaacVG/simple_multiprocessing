import pytest
import numpy as np
import time

from simple_multiprocessing import parallel_function
from main import some_heavy_algorithm_2
from secrets import randbelow


@pytest.mark.parametrize("array_length, samples, max_cores", [(3000, 50, 100), (2000, 50, 100), (1000, 50, 100), (3000, 50, 2), (2000, 50, 2), (1000, 50, 2)])
def test_parallelization(array_length, samples, max_cores):

    test_idx = [randbelow(array_length) for _ in range(samples)]
    params = np.arange(1, array_length)

    # Without parallelization
    start_time = time.time()
    results_without_parallelization = [some_heavy_algorithm_2(param) for param in params]
    end_time = time.time()
    time_without_parallelization = end_time - start_time

    # With parallelization
    start_time = time.time()
    results_with_parallelization = parallel_function(some_heavy_algorithm_2, params, max_workers=max_cores)
    end_time = time.time()
    time_with_parallelization = end_time - start_time

    # Check that the results are the same
    for i in range(len(results_without_parallelization)):
        assert results_without_parallelization[i] == results_with_parallelization[i], f"Results differ at index {i}"

    # Check that parallelization is faster
    assert time_with_parallelization < time_without_parallelization, "Parallelization did not improve execution time"
