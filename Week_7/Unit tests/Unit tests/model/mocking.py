import numpy as np

def get_random_numbers(length: int) -> np.ndarray:
    return np.random.randint(1, 100, length)

def get_mean(length: int) -> float:
    arr = get_random_numbers(length)
    return np.mean(arr)