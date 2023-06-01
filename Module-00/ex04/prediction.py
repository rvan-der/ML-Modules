import numpy as np


def arg_verif(arg):
    if not isinstance(arg, np.ndarray) or arg.ndim != 2 or 0 in arg.shape or arg.shape[1] != 1:
        return False
    if any([not isinstance(x, (np.int64, np.float64)) for x in arg.flat]):
        return False
    return True


def predict_(x, theta):
    if not arg_verif(x) or not arg_verif(theta) or theta.shape != (2, 1):
        return None
    x = np.insert(x, 0, 1, axis=1)
    return np.dot(x, theta)
