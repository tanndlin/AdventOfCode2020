data = open("Day 5\\Day5.txt", 'r').read().split('\n')


def getRow(seatData):
    rowNarrower = seatData[0:7]
    colNarrower = seatData[7:10]
    minPos = 0
    maxPos = 127
    for i in rowNarrower:
        if i == 'B':
            rowLength = maxPos - minPos
            minPos += int(rowLength/2+1)
        else:
            rowLength = maxPos - minPos
            maxPos -= int(rowLength/2+1)

    row = minPos
    minPos = 0
    maxPos = 7

    for i in colNarrower:
        if i == 'R':
            colLength = maxPos - minPos
            minPos += int(colLength/2+1)
        else:
            colLength = maxPos - minPos
            maxPos -= int(colLength/2+1)

    col = minPos
    return (row, col)


def getID(seatData):
    row, col = getRow(seatData)
    return row * 8 + col


def partOne():
    ids = [getID(i) for i in data]
    print(max(ids))


def partTwo():
    ids = [getID(i) for i in data]
    for i in range(32, len(ids)):
        if not i in ids:
            print(i)


partOne()
partTwo()
