import numpy as np
import matplotlib.pyplot as plt


def arg_verif(arg):
    if not isinstance(arg, np.ndarray) or arg.ndim != 2 or 0 in arg.shape or arg.shape[1] != 1:
        return False
    if any([not isinstance(x, (np.int64, np.float64)) for x in arg.flat]):
        return False
    return True


def loss_(y, y_hat):
    diff = y_hat.flatten() - y.flatten()
    return float(np.dot(diff, diff) / (2 * diff.shape[0]))


def predict_(x, theta):
    x = np.insert(x, 0, 1, axis=1)
    return np.dot(x, theta)


def plot_with_loss(x, y, theta):
    if not arg_verif(x) or not arg_verif(y) or not arg_verif(theta):
        return
    if x.shape[0] != y.shape[0] or theta.shape[0] != 2:
        return
    y_hat = predict_(x.reshape(-1, 1), theta.reshape(2,1))
    cost = loss_(y, y_hat)
    y_hat = y_hat.flatten()
    x = x.flatten()
    y = y.flatten()
    theta = theta.flatten()
    plt.title(f"loss: {cost}")
    plt.scatter(x, y)
    plt.plot([x[0], x[-1]], [y_hat[0], y_hat[-1]], c="red")
    for i in range(len(x)):
        plt.plot([x[i], x[i]], [y_hat[i], y[i]], linestyle="--", c="orange")
    plt.show()
