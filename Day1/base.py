import numpy as np


data = np.loadtxt('input.txt')


value = 2020
val2 = 0
data2 = value - data

c = np.in1d(data, data2)
indPair = np.where(c == True)[0]
print(np.prod(data[indPair]))
