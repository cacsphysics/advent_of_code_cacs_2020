# Created by cacsphys

import numpy as np


def whichRow(s):
    rows = np.arange(0, 128)
    for c in s:
        if c == 'F':
            rows, _ = np.array_split(rows, 2)
        if c == 'B':
            _, rows = np.array_split(rows, 2)

    return rows[0]


def whichCol(s):
    cols = np.arange(0, 8)
    for c in s:
        if c == 'L':
            cols, _ = np.array_split(cols, 2)
        if c == 'R':
            _, cols = np.array_split(cols, 2)

    return cols[0]


data = np.loadtxt('rawfile.txt', dtype=str)
rows = np.arange(0, 128)
columns = np.arange(0, 8)
first, back = np.array_split(rows, 2)
for line in data:
    print(whichRow(line[:-3]))
    print(whichCol(line[-3:]))
