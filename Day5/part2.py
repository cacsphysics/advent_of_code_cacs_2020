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


def seatID(rowNum, colNum):
    id = rowNum*8 + colNum
    return id


data = np.loadtxt('input.txt', dtype=str)
rows = np.arange(0, 128)
columns = np.arange(0, 8)
R, C = np.meshgrid(rows, columns)
idList = np.transpose(seatID(R, C))
check = np.zeros(idList.shape)
# Create checklist
for line in data:
    idVal = seatID(whichRow(line[:-3]), whichCol(line[-3:]))
    for el, idrow in enumerate(idList):
        check[el] += np.isin(idrow, idVal)
# Search checklist for 101
check = check.flatten()
for i in range(1, check.size - 1):
    if (check[i-1] == 1):
        if (check[i] == 0) and (check[i+1] == 1):
            myID = i
            break
print(myID)
