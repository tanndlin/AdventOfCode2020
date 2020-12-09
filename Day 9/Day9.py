data = open("Day 9\\Day9.txt", 'r').read().split('\n')
# data = open("Day 9\\small.txt", 'r').read().split('\n')
data = [int(i) for i in data]


def sumOf2Nums(nums, preambleLength, target):
    start = target - preambleLength
    for i in range(preambleLength):
        for j in range(i+1, preambleLength):
            # print(
            # f'Target: {target} Sum: {nums[i+start] + nums[j+start]} indexes: {i+start}, {j+start}')
            if nums[i+start] + nums[j+start] == nums[target]:
                # print('returning')
                return True

    return False


def getExtremes(nums):
    smallest = nums[0]
    largest = nums[0]
    for i in nums:
        smallest = min(smallest, i)
        largest = max(largest, i)
    return smallest + largest


def partOne(nums, preambleLength):
    for i in range(preambleLength, len(nums)):
        if not sumOf2Nums(nums, preambleLength, i):
            return nums[i]


def partTwo(nums, target):
    for lower in range(len(nums)):
        stop = False
        for upper in range(lower, len(nums)):
            if not stop:
                total = sum(nums[lower: upper+1])

                if total == target:
                    return getExtremes(nums[lower:upper+1])
                elif total > target:
                    stop = True

    return False


print(partOne(data, 25))
ans = partOne(data, 25)
print(partTwo(data, ans))
