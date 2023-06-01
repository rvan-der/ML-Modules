import numpy as np
from vec_loss import *


def fmt(x):
    return str(x).replace('\n', ',')

X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
print(f'X = {fmt(X)}')
Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
print(f'Y = {fmt(Y)}')
print(f"loss_(X, Y) = {loss_(X, Y)}")
print("example = 2.142857142857143")
print(f"loss_(X, X) = {loss_(X, X)}")
print("example = 0.0")
