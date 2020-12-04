# Created by cacsphys
""" Check if password hold to format
"""


def check(x):
    """ Checking for password format
    Format::: (min)-(max) (letter): password
    """
    count = 0
    dashIndex = x.find('-')
    colonIndex = x.find(':')
    minCount = int(x[:dashIndex])
    maxCount = int(x[(dashIndex + 1):(colonIndex - 2)])
    letter = x[colonIndex - 1]
    password = x[(colonIndex + 2):]

    for c in password:
        if (c == letter):
            count += 1
    check = ((count >= minCount) and (count <= maxCount))

    return check


valid = 0
f = open("input.txt", "r")
fl = f.readlines()
for x in fl:
    if (check(x)):
        valid += 1


print(valid)
