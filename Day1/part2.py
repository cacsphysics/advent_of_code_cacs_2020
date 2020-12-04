# Created by cacsphysics
""" Part two of Day1 task...
Find the three numbers in text file that sum to 2020.
"""
import numpy as np
import matplotlib.pyplot as plt

# Loading, sorting and remove ugly big numbers.
data = np.loadtxt('input.txt')
data = np.sort(data)
data = data[data < 2020 - data[0]]

"""
The while loop takes the first element of the array and is added to the rest of the elements.
Then I use the technique for Day1 part1 problem to find conjugate pair, definition in part1.py.
If it results in failure, I remove the first element from the list. I continue until the technique
outputs true.
"""
stop = 0  # Stopping criteria
while (stop != 1):
    Val1 = data[0]
    dumData = 2020 - (data + data[0])
    c = np.in1d(data, dumData)  # Check for common elements and find locations
    if (np.any(c) == True):
        indPair = np.where(c == True)[0]  # indecies of conjugate pairs.
        data = np.append(data[indPair], Val1)
        stop = 1
    else:
        data = data[1:]
print(data)
print(np.prod(data))
