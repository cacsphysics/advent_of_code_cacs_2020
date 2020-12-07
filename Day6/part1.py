# Created by cacsphys
import numpy as np


f = open("input.txt", "r")
fl = f.readlines()
count = 0
uniq = ''
for x in fl:
    x = x.strip('\n')
    if x == '':
        uniq = ''
    else:
        for c in x:
            if c in uniq:
                pass
            else:
                uniq += c
                count += 1
print(count)
