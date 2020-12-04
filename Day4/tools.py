# Created by cascphys
""" Testing line scanning count.
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
key,value = open('filename.txt').read().strip().split(':')
"""


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


def datatoDictionary(filename):
    f = open(filename, "r")

    passports = []
    reset = True

    fl = f.readlines()

    for x in fl:
        if reset:
            pepDict = my_dictionary()
            passports.append(pepDict)
        if (len(x) > 1):
            reset = False
            enteries = x.split(' ')
            for entry in enteries:
                key, value = entry.split(':')
                passports[-1].add(key, value)
        if (len(x) == 1):
            reset = True

    return passports
