import numpy as np
from typing import Callable, Optional
from multiprocessing import Pool, cpu_count

def parallel_function(func: Callable, data: np.ndarray, max_workers: Optional[int] = cpu_count()):
    """
    A wrapper function for parallelizing any function 'func' over a set of parameters 'data'
    Args:
        func (callable): The function to be parallelized. Must accept a single argument
        data (iterable): An iterable containing the parameters to apply 'func' to
        max_workers (int): The maximum number of worker processes to use

    Returns:
        list: A list containing the results of applying 'func' to each item in 'data

    """
    if max_workers > cpu_count():
        max_workers = cpu_count()
    print(f"Parallelize with {max_workers} cores")
    with Pool(processes=max_workers) as pool:
        result = pool.map(func, data)
        return result
