# Created by cacsphysics
"""https://adventofcode.com/2020/day/1

conjugate pair == (value1, value2) such that value1 + value2 == 2020.
"""
import numpy as np

# load text file as numpy array
data = np.loadtxt('input.txt')


value = 2020  # sum value
val2 = 0
# Create conjugate data array
data2 = value - data

# Check for common elements and find locations
c = np.in1d(data, data2)
"""
produces a Boolean array; where True values are common elements.
The shape is that of data variable.
"""
indPair = np.where(c == True)[0]  # indecies of conjugate pairs.
print(np.prod(data[indPair]))
