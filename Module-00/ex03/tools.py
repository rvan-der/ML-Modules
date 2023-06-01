import numpy as np


def add_intercept(x):
    if not isinstance(x, np.ndarray) or x.ndim != 2 or 0 in x.shape:
        return None
    return np.insert(x, 0, 1, axis=1)
