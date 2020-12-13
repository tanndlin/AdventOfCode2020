import math

data = open("Day 12\\Day12.txt", 'r').read().split('\n')
# data = open("Day 12\\small.txt", 'r').read().split('\n')


def dist(a, b, c, d):
    return abs(a-c) + abs(d-b)


def partOne(dirs):

    direction = 0
    x = 0
    y = 0

    for i in dirs:
        command = i[0:1]
        value = int(i[1:])

        if command == 'N':
            y += value
        elif command == 'S':
            y -= value
        elif command == 'E':
            x += value
        elif command == 'W':
            x -= value
        elif command == 'L':
            direction += value
        elif command == 'R':
            direction -= value
        elif command == 'F':
            x += value * math.cos(math.radians(direction))
            y += value * math.sin(math.radians(direction))

    return dist(0, 0, x, y)


def partTwo(dirs):
    shipX = 0
    shipY = 0
    wayX = 10
    wayY = 1

    for i in dirs:
        command = i[0:1]
        value = int(i[1:])

        if command == 'N':
            wayY += value
        elif command == 'S':
            wayY -= value
        elif command == 'E':
            wayX += value
        elif command == 'W':
            wayX -= value
        elif command == 'L':
            for k in range(int(value/90)):
                wayX, wayY = -wayY, wayX
        elif command == 'R':
            for k in range(int(value/90)):
                wayX, wayY = wayY, -wayX
        elif command == 'F':
            shipX += wayX * value
            shipY += wayY * value
    return dist(0, 0, shipX, shipY)


print(partOne(data))
print(partTwo(data))
