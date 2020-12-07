# Created by cacsphys
import numpy as np


def common(group):
    for el, s in enumerate(group):
        if (el == 0):
            count = set(s)
        else:
            count = count & set(s)
    return len(list(count))


f = open("input.txt", "r")
fl = f.readlines()
groupList = []
count = []
for el, x in enumerate(fl):
    x = x.strip('\n')
    if len(x) != 0:
        groupList.append(x)
    else:
        count.append(common(groupList))
        groupList = []
    if (el == len(fl) - 1):
        count.append(common(groupList))
        groupList = []
print(sum(count))
