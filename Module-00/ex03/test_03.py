import numpy as np
from tools import *


# Example 1:
x1 = np.arange(1,6).reshape((-1,1))
print(f"x1 = {repr(x1)}")
print(f"add_intercept(x1) = {repr(add_intercept(x1))}")

# Example 2:
x2 = np.arange(1,10).reshape((3,3))
print(f"\n\nx2 = {repr(x2)}")
print(f"add_intercept(x2) = {repr(add_intercept(x2))}")
