import re
data = open("Day 4\\Day4.txt", 'r').read().split('\n\n')


def checkPassport(passport):
    parsed = re.split(r'[\n ]', passport)
    if len(parsed) > 7:
        return True
    elif len(parsed) == 7:
        if ' '.join(parsed).find('cid:') == -1:
            return True

    return False


def hasCondition(passport, regex):
    parsed = re.split(r'[\n ]', passport)
    test = [re.search(regex, i) for i in parsed]
    for i in test:
        if i:
            return True
    return False


def getAttr(attr, passport):
    for i in passport:
        if i.find(attr) != -1:
            return i.split(':')[1]
    return -1


def testAllConditions(passport):
    parsed = re.split(r'[\n ]', passport)

    byr = getAttr('byr', parsed)
    iyr = getAttr('iyr', parsed)
    eyr = getAttr('eyr', parsed)
    hgt = getAttr('hgt', parsed)
    hcl = getAttr('hcl', parsed)
    ecl = getAttr('ecl', parsed)
    pid = getAttr('pid', parsed)

    # print(pid)

    if byr == -1:
        return False
    if iyr == -1:
        return False
    if eyr == -1:
        return False
    if hgt == -1:
        return False
    if hcl == -1:
        return False
    if ecl == -1:
        return False
    if pid == -1:
        return False

    flags = [int(byr) >= 1920 and int(byr) <= 2002,
             int(iyr) >= 2010 and int(iyr) <= 2020,
             int(eyr) >= 2020 and int(eyr) <= 2030,
             re.search(r'[0-9]+((cm)|(in)){1}', hgt),
             re.search(r'#[0-9a-f]{6}', hcl) and len(hcl) == 7,
             re.search(r'((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))',
                       ecl) and len(ecl) == 3,
             re.search(r'[0-9]{9}', pid) and len(pid) == 9]

    if hgt.find('cm') != -1:
        if len(hgt) != 5:
            return False
        flags.append(int(hgt[0:3]) >= 150 and int(hgt[0:3]) <= 193)
    else:
        if len(hgt) != 4:
            return False
        flags.append(int(hgt[0:2]) >= 59 and int(hgt[0:2]) <= 76)

    for i in flags:
        if not i:
            return False
    return True


def partOne():
    return sum([checkPassport(i) for i in data])


def partTwo():
    return sum([testAllConditions(i) for i in data])


print(partTwo())
# print(testAllConditions(data[-1]))
