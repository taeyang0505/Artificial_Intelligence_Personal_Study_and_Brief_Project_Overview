import numpy as np
# Represent the following system in NumPy matrix/vector form, then solve for x, y, and z

# Given
'''
4x + z = 2
-y + 2z - 3x = 0
.5y - x - 1.5z = -4
'''

A = np.array([[4, 0, 1], [-3, -1, 2], [-1, 0.5, -1.5]])
b = np.array([2, 0, -4])
x, y, z = np.linalg.solve(A,b)
print((x,y,z))
