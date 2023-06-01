import numpy as np
from plot import *


def fmt(x):
    return str(x).replace('\n', ',')

x = np.arange(1,6).reshape((-1, 1))
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568]).reshape((-1, 1))
print(f"x = {fmt(x)}")
print(f"y = {fmt(y)}")


theta1= np.array([[18],[-1]])
print(f"\ntheta1 = {fmt(theta1)}")
print("plot_with_loss(x, y, theta1)")
plot_with_loss(x, y, theta1)

theta2 = np.array([[14], [0]])
print(f"\ntheta2 = {fmt(theta2)}")
print("plot_with_loss(x, y, theta2)")
plot_with_loss(x, y, theta2)

theta3 = np.array([[12], [0.8]])
print(f"\ntheta3 = {fmt(theta3)}")
print("plot_with_loss(x, y, theta3)")
plot_with_loss(x, y, theta3)
