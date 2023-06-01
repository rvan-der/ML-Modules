import numpy as np
from loss import *


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


def fmt(x):
    return str(x).replace('\n', ',')


x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
print(f"x1 = {fmt(x1)}")
theta1 = np.array([[2.], [4.]])
print(f"theta1 = {fmt(theta1)}")
y_hat1 = predict_(x1, theta1)
print(f"y_hat1 = {fmt(y_hat1)}")
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print(f"y1 = {fmt(y1)}")
print(f"loss_elem_(y1, y_hat1) = {fmt(loss_elem_(y1, y_hat1))}")
print("example = array([[0.], [1], [4], [9], [16]])")
print(f"loss_(y1, y_hat1) = {loss_(y1, y_hat1)}")
print("example = 3.0")


x2 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(-1, 1)
print(f"\n\nx2 = {fmt(x2)}")
theta2 = np.array([[0.], [1.]])
print(f"theta2 = {fmt(theta2)}")
y_hat2 = predict_(x2, theta2)
print(f"y_hat2 = {fmt(y_hat2)}")
y2 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)
print(f"y2 = {fmt(y2)}")
print(f"loss_(y2, y_hat2) = {loss_(y2, y_hat2)}")
print("example = 2.142857142857143")
print(f"loss_(y2, y2) = {loss_(y2, y2)}")
print("example = 0.0")
