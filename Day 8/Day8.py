data = open("Day 8\\Day8.txt", 'r').read().split('\n')


def runCommand(command, acc, index):
    if command.split(' ')[0] == 'acc':
        amount = command.split(' ')[1]
        if amount[0] == '+':
            acc += int(amount[1:])
        else:
            acc -= int(amount[1:])
        index += 1

    if command.split(' ')[0] == 'jmp':
        amount = command.split(' ')[1]
        if amount[0] == '+':
            index += int(amount[1:])
        else:
            index -= int(amount[1:])

    if command.split(' ')[0] == 'nop':
        index += 1

    return acc, index


def isInfinite(commands):
    used = []
    index = 0
    acc = 0
    while index not in used and index < len(data):
        used.append(index)
        acc, index = runCommand(commands[index], acc, index)
    if index in used:
        return True
    return False


def changeInstruct(data, index):
    temp = data.copy()
    if data[index].split(' ')[0] == 'nop':
        temp[index] = 'jmp' + temp[index][3:]
    elif data[index].split(' ')[0] == 'jmp':
        temp[index] = 'nop' + temp[index][3:]
    return temp


def partOne(commands):
    index = 0
    acc = 0
    used = []

    while index not in used and index < len(commands):
        used.append(index)
        acc, index = runCommand(commands[index], acc, index)
    return acc


def partTwo(data):
    changed = 0
    commands = data.copy()
    while isInfinite(commands):
        changed += 1
        commands = changeInstruct(data, changed)
    return partOne(commands)


print(partOne(data))
print(partTwo(data))
