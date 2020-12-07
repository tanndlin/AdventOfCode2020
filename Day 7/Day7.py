data = open("Day 7\\Day7.txt", 'r').read().split('\n')
# del data[-1]
# data = open("Day 7\\small.txt", 'r').read().split('\n')

# for i in data:
# print(i)


class Bag:
    name = ''
    contains = []


def getTypeAndNum(string):
    num = string[0]
    name = string[2:].replace(' bags', '').replace(' bag', '').replace(
        '.', '').strip()
    return {'num': num, 'name': name}


def createBag(input):
    newBag = Bag()
    newBag.name = input.split(' bags contain')[0]
    bags = [getTypeAndNum(i.strip())
            for i in input.split(' bags contain')[1].split(',')]

    newBag.contains = bags

    return newBag


def canContain(bag):
    if bag is None:
        return False

    if bag.name == 'shiny gold':
        return True

    if bag.contains[0] is None:
        return False
    return any([canContain(i['name']) for i in bag.contains])


def printBag(bag):
    print(f'Name: {bag.name}')
    print(f'Contains {bag.contains}')


bagDict = {}


def createDict():
    for i in data:
        bag = createBag(i)
        bagDict[bag.name] = bag

    for i in bagDict:
        bag = bagDict[i]

        for j in range(len(bag.contains)):
            contained = bag.contains[j]

            if contained['name'] == 'other':
                bag.contains[j] = None
                continue

            num = contained['num']
            subBag = bagDict[contained['name']]
            bag.contains[j] = {'num': num, 'name': subBag}


def countBags(bag, depth):
    if bag.contains[0] is None:
        return 0

    # printBag(bag)

    total = 0
    for i in bag.contains:
        # print(''.join(['\t' for i in range(depth)]), i['num'])
        total += int(i['num'])
        total += int(i['num']) * countBags(i['name'], depth + 1)
    return total


def partOne():
    # Minus 1 to account for the case where the first bag is gold
    return sum([canContain(bagDict[i]) for i in bagDict]) - 1


def partTwo(bagName):
    return countBags(bagDict[bagName], 0)


createDict()
print(partOne())
print(partTwo('shiny gold'))
