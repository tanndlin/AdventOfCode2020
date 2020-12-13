from copy import deepcopy

data = open("Day 11\\Day11.txt", 'r').read().split('\n')
data = [[c for c in i] for i in data]

cols = len(data)
rows = len(data[0])


def printData(arr):
    temp = [''.join(i) for i in arr]
    for i in temp:
        print(i)


def iter(arr):
    newData = deepcopy(arr)

    for x in range(cols):
        for y in range(rows):
            if arr[x][y] != '.':
                total = 0

                for i in range(-1, 1+1):
                    for j in range(-1, 1+1):

                        if x + i >= 0 and y + j >= 0 and x + i < cols and y + j < rows:
                            if arr[x+i][y+j] == '#' and not (i == 0 and j == 0):
                                total += 1
                if total == 0:
                    newData[x][y] = '#'
                elif total >= 4:
                    newData[x][y] = 'L'

    return newData


def isEqual(a, b):
    for i in range(cols):
        for j in range(rows):
            if(a[i][j] != b[i][j]):
                return False
    return True


def countOccu(arr):
    temp = [[j == '#' for j in i] for i in arr]
    return sum([sum(i) for i in temp])


def partOne(arr):
    prev = deepcopy(arr)
    arr = iter(arr)

    while not isEqual(prev, arr):
        prev = deepcopy(arr)
        arr = iter(arr)

    # printData(arr)
    return countOccu(arr)


print(partOne(data))
