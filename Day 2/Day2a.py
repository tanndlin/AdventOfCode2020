data = open("Day 2\\Day2.txt", 'r').read().split('\n')
del data[-1]
parsed = []


def prepData():
    for i in data:
        temp = i.split(' ')

        nums = temp[0].split('-')
        first = nums[0]
        second = nums[1]

        letter = temp[1][0]
        password = temp[2]

        obj = [first, second, letter, password]
        parsed.append(obj)


def occurances(str, letter):
    total = 0
    while str.find(letter) != -1:
        total += 1
        str = str[str.find(letter)+1:]
    return total


def isValid1(obj):
    occ = occurances(obj[3], obj[2])
    if occ >= int(obj[0]) and occ <= int(obj[1]):
        return True
    return False


def isValid2(obj):
    first = int(obj[0])-1
    second = int(obj[1])-1
    letter = obj[2]
    password = obj[3]

    if password[first] == letter and password[second] != letter:
        return True
    if password[first] != letter and password[second] == letter:
        return True
    return False


def partOne():
    return sum([isValid1(i) for i in parsed])


def partTwo():
    return sum([isValid2(i) for i in parsed])


prepData()
print(partOne())
print(partTwo())
