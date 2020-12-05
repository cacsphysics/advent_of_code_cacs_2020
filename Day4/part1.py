import tools

valid = []
passports = tools.datatoDictionary(filename='input.txt')

for item in passports:
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    keys = []
    check = False
    for key in item:
        keys.append(key)
    if (list(set(req) - set(keys)) == []):
        check = True
    valid.append(check)
print(sum(valid))
