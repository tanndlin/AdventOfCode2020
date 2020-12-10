data = open("Day 10\\Day10.txt", 'r').read().split('\n')
data = [int(i) for i in data]


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partOne(arr):
    ones = 0
    threes = 1  # Account for last one
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] == 1:
            ones += 1
        elif arr[i+1] - arr[i] == 3:
            threes += 1

    return ones * threes


insertionSort(data)
print(partOne(data))
