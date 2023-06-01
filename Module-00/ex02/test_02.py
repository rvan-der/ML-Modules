import numpy as np
from prediction import *

x = np.arange(1,6).reshape((5,1))
print(f"x = {x}")

theta1 = np.array([[5], [0]])
print(f"\ntheta1 = {repr(theta1)}")
print(f"simple_predict(x, theta1) = {repr(simple_predict(x, theta1))}")
print("example: array([5., 5., 5., 5., 5.])")

theta2 = np.array([[0], [1]])
print(f"\ntheta2 = {repr(theta2)}")
print(f"simple_predict(x, theta2) = {repr(simple_predict(x, theta2))}")
print("example: array([1., 2., 3., 4., 5.])")

theta3 = np.array([[5], [3]])
print(f"\ntheta3 = {repr(theta3)}")
print(f"simple_predict(x, theta3) = {repr(simple_predict(x, theta3))}")
print("example: array([ 8., 11., 14., 17., 20.])")

theta4 = np.array([[-3], [1]])
print(f"\ntheta4 = {repr(theta4)}")
print(f"simple_predict(x, theta4) = {repr(simple_predict(x, theta4))}")
print("example: array([-2., -1., 0., 1., 2.])")
