import numpy as np

# Given
'''
2a + 3d - 2c = 4
-c + 4b - a = 1
2d - 2c + 3a - b = 2
-2a + 3c - b = -2
'''

A = np.array([[2, 0, -2, 3], [-1, 0, -1, 4], [3, -1, -2, 2], [-2, -1, 3, 0]])
B = np.array([4, 1, 2, -2])
a, b, c, d = np.linalg.solve(A, B)
print((a, b, c, d))
