# Created by cacsphysics
import tools
import re

"""
re.compile('#[0-9,1-f]{6,6}')
"""


def fixNewLine(value):
    data = value
    if (repr(data[-1:]) == repr('\n')):
        data = value[:-1]
    return data


def checkbyr(value):
    value = int(value)
    if (value >= 1920) and (value <= 2002):
        output = True
    else:
        output = False
    return output


def checkiyr(value):
    value = int(value)
    if (value >= 2010) and (value <= 2020):
        output = True
    else:
        output = False
    return output


def checkeyr(value):
    value = int(value)
    if (value >= 2020) and (value <= 2030):
        output = True
    else:
        output = False
    return output


def checkhgt(value):
    key = value[-2:]
    value = int(value[:-2])
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
    if len(color) == 3:
        output = color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    else:
        output = False
    return output


def checkpid(value):
    if len(value) == 9:
        p = re.compile('[0-9]{9,9}')
        check = p.match(value)
        if check == type(None):
            output = False
        else:
            output = True
    else:
        output = False

    return output


def checkcid(value):
    return True


newreq = {'byr': checkbyr,
          'iyr': checkiyr,
          'eyr': checkeyr,
          'hgt': checkhgt,
          'hcl': checkhcl,
          'ecl': checkecl,
          'pid': checkpid,
          'cid': checkcid}


def check(command, arg):
    output = newreq[command](arg)
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


"""newreq = {'byr': checkbyr,
          'iyr': checkiyr,
          'eyr': checkeyr,
          'hgt': checkhgt,
          'hcl': checkhcl,
          'ecl': checkecl,
          'pid': checkpid}"""
phase2 = []
for item in phase1:
    condition = True
    for key, value in item.items():
        value = fixNewLine(value)
        if condition == False:
            break

        condition = condition*check(command=key, arg=value)
    if condition:
        phase2.append(item)
print(len(phase2))
