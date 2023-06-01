import numpy as np


def arg_verif(arg):
    if not isinstance(arg, np.ndarray) or arg.ndim != 2 or 0 in arg.shape or arg.shape[1] != 1:
        return False
    if any([not isinstance(x, (np.int64, np.float64)) for x in arg.flat]):
        return False
    return True


def mse_(y, y_hat):
    if not arg_verif(y) or not arg_verif(y_hat) or y.shape != y_hat.shape:
        return None
    diff = y.flatten() - y_hat.flatten()
    return np.dot(diff, diff) / diff.shape[0]


def rmse_(y, y_hat):
    mse = mse_(y, y_hat)
    if mse == None:
        return None
    return np.sqrt(mse)


def mae_(y, y_hat):
    if not arg_verif(y) or not arg_verif(y_hat) or y.shape != y_hat.shape:
        return None
    m = y.shape[0]
    return sum(abs(y_hat.flat[i] - y.flat[i]) for i in range(m)) / m
    

def r2score_(y, y_hat):
    if not arg_verif(y) or not arg_verif(y_hat) or y.shape != y_hat.shape:
        return None
    m = y.shape[0]
    mean = sum(y) / m
    diff_hat = y.flatten() - y_hat.flatten()
    diff_mean = np.array([Yi - mean for Yi in y]).flatten()
    return 1 - np.dot(diff_hat, diff_hat) / np.dot(diff_mean, diff_mean)
