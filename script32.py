# Turning our function into an array 
import numpy as np
from math import sin
import codecademylib3
import matplotlib.pyplot as plt

# our change in x value
dx = 1
def f(x):
    return sin(x) 
sin_x = [x for x in np.arange(0,20,dx)]
sin_y = [f(x) for x in np.arange(0,20,dx)]

plt.plot(sin_x, sin_y)
sin_deriv = np.gradient(sin_y, dx)
plt.plot(sin_x, sin_deriv)
plt.show()
