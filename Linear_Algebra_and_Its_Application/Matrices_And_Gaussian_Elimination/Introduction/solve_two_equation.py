# You don't need to add/edit anything to the below solution. 

import numpy as np
from scipy.optimize import fsolve

def func(x):

	return [x[0] + 2*x[1] - 3,
			4*x[0] + 5*x[1] - 6]

root = fsolve(func, [1,1])
print(root)