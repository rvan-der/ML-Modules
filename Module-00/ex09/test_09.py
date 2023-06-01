import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
from other_losses import *


def fmt(x):
    return str(x).replace('\n', ',')

# Example 1:
x = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((-1, 1))
y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
print(f"x = {fmt(x)}")
print(f"y = {fmt(y)}")

print(f"\nmse_(x,y) = {mse_(x,y)}")
print(f"expected = {mean_squared_error(x,y)}")

print(f"\nrmse_(x,y) = {rmse_(x,y)}")
print(f"expected = {sqrt(mean_squared_error(x,y))}")

print(f"\nmae_(x,y) = {mae_(x,y)}")
print(f"expected = {mean_absolute_error(x,y)}")

print(f"\nr2score_(x,y) = {r2score_(x,y)}")
print(f"expected = {r2_score(x,y)}")
