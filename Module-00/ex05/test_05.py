import numpy as np
from plot import *


x = np.arange(1,6).reshape((-1,1))
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554]).reshape((-1,1))


theta1 = np.array([[4.5],[-0.2]])
plot(x, y, theta1)


theta2 = np.array([[-1.5],[2]])
plot(x, y, theta2)


theta3 = np.array([[3],[0.3]])
plot(x, y, theta3)
