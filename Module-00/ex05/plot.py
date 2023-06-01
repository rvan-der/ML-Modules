import matplotlib.pyplot as plt
import numpy as np


def arg_verif(arg):
    if not isinstance(arg, np.ndarray) or arg.ndim != 2 or 0 in arg.shape or arg.shape[1] != 1:
        return False
    if any([not isinstance(x, (np.int64, np.float64)) for x in arg.flat]):
        return False
    return True


def plot(x, y, theta):
    if not arg_verif(x) or not arg_verif(y) or not arg_verif(theta):
        return
    if x.shape[0] != y.shape[0] or theta.shape[0] != 2:
        return
    x = list(x.flatten())
    y = list(y.flatten())
    theta = list(theta.flatten())
    plt.scatter(x, y, marker='.')
    lineX = [x[0], x[-1]]
    lineY = [x[0] * theta[1] + theta[0], x[-1] * theta[1] + theta[0]]
    plt.plot(lineX, lineY, c="red")
    plt.show()
