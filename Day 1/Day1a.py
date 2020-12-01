data = open("Day 1\\Day1.txt", 'r').read().split('\n')
del data[-1]
data = [int(i) for i in data]

# Naive approach
# O(n^2)
def part1():
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == 2020:
                return (data[i] * data[j])

# O(n^3)
def part2():
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            for k in range(j+1,len(data)):
                if(data[i] + data[j] + data[k]) == 2020:
                    return data[i] * data[j] * data[k]


print(part1())
print(part2())

