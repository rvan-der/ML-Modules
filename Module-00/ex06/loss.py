import numpy as np


def arg_verif(arg):
    if not isinstance(arg, np.ndarray) or arg.ndim != 2 or 0 in arg.shape or arg.shape[1] != 1:
        return False
    if any([not isinstance(x, (np.int64, np.float64)) for x in arg.flat]):
        return False
    return True


def loss_elem_(y, y_hat):
    if not arg_verif(y) or not arg_verif(y_hat) or y.shape[0] != y_hat.shape[0]:
        return None
    y = list(y.flatten())
    y_hat = list(y_hat.flatten())
    return np.array([[(y_hat[i] - y[i]) ** 2] for i in range(len(y))])


def loss_(y, y_hat):
    if not arg_verif(y) or not arg_verif(y_hat) or y.shape[0] != y_hat.shape[0]:
        return None
    lossElem = loss_elem_(y, y_hat)
    return float(sum(lossElem) / (len(lossElem) * 2))
