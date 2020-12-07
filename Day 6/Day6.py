data = open("Day 6\\Day6.txt", 'r').read().split('\n\n')
# del data[-1]


def removeDupes(arr):
    temp = []
    for i in arr:
        if not i in temp and i != '\n':
            temp.append(i)
    return temp


def isInAll(el, arr):
    for i in arr:
        if not el in i:
            return False
    return True


def partOne():
    return sum([len(removeDupes(i)) for i in data])


def partTwo():
    inAll = []
    for i in data:
        seperated = i.split('\n')
        print(seperated)

        for question in seperated[0]:
            if isInAll(question, seperated):
                inAll.append(question)
    return len(inAll)


print(partOne())
print(partTwo())
