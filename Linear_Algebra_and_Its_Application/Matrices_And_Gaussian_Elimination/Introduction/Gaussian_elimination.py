# You don't need to add/edit anything to the below solution. 

import numpy as np
from scipy import linalg

# Equation 1x+2y = 3, 4x+5y = 6

# X

a = np.array([[3, 2],
			 [6, 5]])
b = np.array([[1, 2],
			  [ 4, 5]])
c = np.array([[1, 3],
			  [4, 6]])

x = linalg.det(a)/linalg.det(b)
y = linalg.det(c)/linalg.det(b)

print("x value is ",x)
print("y value is ", y)