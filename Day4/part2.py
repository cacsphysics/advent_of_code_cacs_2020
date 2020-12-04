# Created by cacsphysics
import tools
import re

"""
re.compile('#[0-9,1-f]{6,6}')
"""


def fixNewLine(dictionary, key, value):
    data = dictionary[key][()]
    if (data[-2] == '\\'):
        dictionary[key] = data[:-2]
        fix = True
    else:
        fix = False
    return fix, data, key, dictionary


def checkbyr(value):
    if (value >= 1920) and (value <= 2002):
        output = True
    else:
        output = False
    return output


def checkiyr(value):
    if (value >= 2010) and (value <= 2020):
        output = True
    else:
        output = False
    return output


def checkeyr(value):
    if (value >= 2020) and (value <= 2030):
        output = True
    else:
        output = False
    return output


def checkhgt(key, value):
    if key == 'cm':
        if (value >= 150) and (value <= 193):
            output = True
        else:
            output = False
    elif key == 'in':
        if (value >= 59) and (value <= 76):
            output = True
        else:
            output = False
    else:
        output = False

    return output


def checkhcl(s):
    if len(s) == 7:
        p = re.compile('#[0-9,1-f]{6,6}')
        check = p.match(s)
        if check != None:
            output = True
        else:
            output = False
    else:
        output = False

    return output


def checkecl(color):
    output = color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return output


def checkpid(value):
    p = re.compile('[0-9]{9,9}')
    check = p.match(value)
    if check != None:
        output = True
    else:
        output = False

    return output


phase1 = []
passports = tools.datatoDictionary(filename='input.txt')
req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for item in passports:
    keys = []
    for key in item:
        keys.append(key)
    if (list(set(req) - set(keys)) == []):
        phase1.append(item)
#
newreq = {'byr': checkbyr,
          'iyr': checkiyr,
          'eyr': checkeyr,
          'hgt': checkhgt,
          'hcl': checkhcl,
          'ecl': checkecl,
          'pid': checkpid}
for item in phase1:
    reset = False
    while reset == False:
        keyList = item.keys()
        check
