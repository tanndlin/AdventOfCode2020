data = open("Day 1\\Day1.txt", 'r').read().split('\n')
del data[-1]
data = [int(i) for i in data]

table = {'Num' : True}
for i in data:
    table[str(i)] = True

# O(n)
def part1():
    for i in data:
        numNeeded = 2020 - i
        if str(numNeeded) in table:
            return i * numNeeded
# O(n^2)
def part2():
    for i in range(len(data)):
        sumNeeded = 2020 - data[i]
        for j in range(i+1,len(data)):
            numNeeded = sumNeeded - data[j]
            if str(numNeeded) in table:
                return data[i] * data[j] * numNeeded

        

print(part1())
print(part2())