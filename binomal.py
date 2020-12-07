# Write some python code that simulates flipping a coin 100 times.
#ref https://www.w3schools.com/python/numpy_random_binomial.asp
import numpy as np

#from numpy import random

x = np.random.binomial(n=10, p=0.5, size=10)

print(x)