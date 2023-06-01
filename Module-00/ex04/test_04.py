import numpy as np
from prediction import *


x = np.arange(1,6).reshape((-1, 1))
print("x = %s"%(str(x).replace('\n' , ',')))

theta1 = np.array([[5], [0]])
print("\ntheta1 = %s"%(str(theta1).replace('\n' , ',')))
print("predict_(x, theta1) = %s"%(str(predict_(x, theta1)).replace('\n' , ',')))
print("example = array([[5.], [5.], [5.], [5.], [5.]])")


theta2 = np.array([[0], [1]])
print("\ntheta2 = %s"%(str(theta2).replace('\n' , ',')))
print("predict_(x, theta2) = %s"%(str(predict_(x, theta2)).replace('\n' , ',')))
print("example = array([[1.], [2.], [3.], [4.], [5.]])")


theta3 = np.array([[5], [3]])
print("\ntheta3 = %s"%(str(theta3).replace('\n' , ',')))
print("predict_(x, theta3) = %s"%(str(predict_(x, theta3)).replace('\n' , ',')))
print("example = array([[ 8.], [11.], [14.], [17.], [20.]])")


theta4 = np.array([[-3], [1]])
print("\ntheta4 = %s"%(str(theta4).replace('\n' , ',')))
print("predict_(x, theta4) = %s"%(str(predict_(x, theta4)).replace('\n' , ',')))
print("example = array([[-2.], [-1.], [ 0.], [ 1.], [ 2.]])")
