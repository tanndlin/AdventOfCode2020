data = open("Day 15\\Day15.txt", 'r').read().split(',')
data = [int(i) for i in data]
nums = data.copy()


def timesIn(nums, targ):
    return targ in nums[0:len(nums)-1]


def lastOcc(nums, targ):
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] == targ:
            return len(nums) - (i + 1)
    return -1


def partOne(targLen):
    while len(nums) < targLen:
        last = nums[-1]
        if timesIn(nums, last):
            nums.append(lastOcc(nums, last))
        else:
            nums.append(0)
    return nums[-1]


# For the sake of consistency
def partTwo(targLen):
    return partOne(targLen)


print(partOne(2020))
# print(partOne(30000000))
