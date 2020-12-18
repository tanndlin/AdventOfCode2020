data = open("Day 13\\Day13.txt", 'r').read().split('\n')
earliestTime = int(data[0])
buses = data[1].split(',')


def callback(e):
    return e is not 'x'


trimmed = [i for i in filter(callback, buses)]
times = [int(i) for i in trimmed]
increments = [int(i) for i in trimmed]


def increment():
    for i in range(len(times)):
        increments[i] += times[i]


def partOne():
    keepGoing = True
    while keepGoing:
        increment()
        isValid = [True if i >= earliestTime else False for i in increments]
        keepGoing = not any(isValid)

    arrival = max(increments)
    timeToWait = arrival - earliestTime
    return timeToWait * times[increments.index(arrival)]


print(partOne())
