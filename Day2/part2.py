def check(x):
    """ Checking for password format
    Format::: (min)-(max) (letter): password
    """
    count = 0
    dashIndex = x.find('-')
    colonIndex = x.find(':')
    minCount = int(x[:dashIndex]) - 1
    maxCount = int(x[(dashIndex + 1):(colonIndex - 2)]) - 1
    letter = x[colonIndex - 1]
    password = x[(colonIndex + 2):]
    check = ((password[minCount] == letter and password[maxCount] != letter) or (
        password[maxCount] == letter and password[minCount] != letter))
    return check


valid = 0
f = open("input.txt", "r")
fl = f.readlines()
for x in fl:
    if (check(x)):
        valid += 1


print(valid)
