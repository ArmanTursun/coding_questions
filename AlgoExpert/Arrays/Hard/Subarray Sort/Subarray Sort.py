# Hard

# Write a function that takes in an array of at least two integers and that returns an array of the starting
# and ending indices of the smallest subarray in the input array that needs to be sorted in place in order
# for the entire input array to be sorted (in ascending order).

# If the input array is already sorted, the function should return [-1, -1].

# Sample Input
# array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 17, 18, 19]

# Sample Output
# [3, 9]

def subarraySort(array):
    # Write your code here.
    left = len(array)
    right = -1

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            for j in range(i):
                if array[j] > array[i] and j < left:
                    left = j
    if left == len(array):
        return [-1, -1]
    for i in range(len(array) - 2, -1, -1):
        if array[i] > array[i + 1]:
            for j in range(len(array) - 1, i, -1):
                if array[j] < array[i] and j > right:
                    right= j
    return [left, right]
## T = O(n^2); S = O(1)


def subarraySort(array):
    # Write your code here.
    temp = sorted(array)
    left = right = -1

    for i in range(len(array)):
        if array[i] != temp[i]:
            left = i
            break
    if left == -1:
        return [left, right]

    for i in range(len(array) - 1, -1, -1):
        if array[i] != temp[i]:
            right = i
            break
    return [left, right]
## T = O(nlog(n)); S = O(n)


def subarraySort(array):
    # Write your code here.
    left = right = -1
    minEle = float('inf')
    maxEle = float('-inf')

    for i, element in enumerate(array):
        if isOutOfOrder(i, element, array):
            minEle = min(minEle, element)
            maxEle = max(maxEle, element)

    for i in range(len(array)):
        if array[i] > minEle:
            left = i
            break
    for i in range(len(array) - 1, -1, -1):
        if array[i] < maxEle:
            right = i
            break
    return [left, right]

def isOutOfOrder(i, element, array):
    if i == 0:
        return element > array[i + 1]
    if i == len(array) - 1:
        return element < array[i - 1]
    return element > array[i + 1] or element < array[i - 1]
## T = O(n); S = O(1)


def subarraySort(array):
    # Write your code here.
    left = right = -1

    curMax = array[0]
    for i in range(1, len(array)):
        if array[i] < curMax:
            right = i
        else:
            curMax = array[i]

    if right == -1:
        return [left, right]

    curMin = array[-1]
    for i in range(len(array) - 2, -1, -1):
        if array[i] > curMin:
            left = i
        else:
            curMin = array[i]
    return [left, right]
## T = O(n); S = (1)
