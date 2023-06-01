import numpy as np


def arg_verif(arg):
    if not isinstance(arg, np.ndarray) or arg.ndim != 2 or 0 in arg.shape or arg.shape.count(1) < 1:
        return False
    if any([not isinstance(x, (np.int64, np.float64)) for x in arg.flat]):
        return False
    return True


def loss_(y, y_hat):
    if not arg_verif(y) or not arg_verif(y_hat) or y.shape != y_hat.shape:
        return None
    diff = y_hat.flatten() - y.flatten()
    return float(np.dot(diff, diff) / (2 * diff.shape[0]))
