import numpy as np


def arg_verif(arg):
    if not isinstance(arg, np.ndarray) or arg.ndim != 2 or 0 in arg.shape:
        return False
    if any([not isinstance(x, (np.int64, np.float64)) for x in arg.flat]):
        return False
    return True

def simple_predict(x, theta):
    if not arg_verif(x) or not arg_verif(theta) or theta.shape != (2,1):
        return None
    return np.array([[float(theta[0][0] + theta[1][0] * Xi)] for Xi in x.flat])
