data = open("Day 3\\Day3.txt", 'r').read().split('\n')
del data[-1]


def getTree(pos):
    x = pos[0]
    y = pos[1]
    return data[y][x] == '#'


def multiply(arr):
    total = 1
    for i in arr:
        total *= i
    return total


def partOne(slope):
    total = 0
    x = 0
    y = 0

    while y < len(data):
        pos = (x, y)
        if getTree(pos):
            total += 1
        x += slope[0]
        x = x % len(data[0])
        y += slope[1]
    # print(total)
    return total


def partTwo():
    slopes = ((1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2),)
    return multiply([partOne(slope) for slope in slopes])


print(partOne((3, 1)))
print(partTwo())
