# Hard

# Write a function that takes in an array of integers and returns a sorted version of that array. Use
# the Heap Sort algorithm to sort the array.

from heapq import heappush, heappop, heapify
def heapSort(array):
    # Write your code here.
    heapify(array)
    result = []
    while array:
        result.append(heappop(array))
    return result

# T = O(nlog(n)); S = O(n)


####### Write Heap byself ########
def heapSort(array):
    # Write your code here.
    buildHeap (array)
    i = len(array) - 1
    while i > 0:
        array[0], array[i] = array[i], array[0]
        siftDown(0, array, i - 1)
        i -= 1
    return array

def buildHeap(array):
    i = len(array) // 2 - 1
    while i >= 0:
        siftDown(i, array, len(array) - 1)
        i -= 1

def siftDown(i, array, right):
    curIdx = i
    while curIdx < right + 1:
        curMax = curIdx
        if 2 * curIdx + 1 < right + 1 and array[2 * curIdx + 1] > array[curIdx]:
            curMax = 2 * curIdx + 1
        if 2 * curIdx + 2 < right + 1 and array[2 * curIdx + 2] > array[curMax]:
            curMax = 2 * curIdx + 2
        array[curIdx], array[curMax] = array[curMax], array[curIdx]
        if curMax == curIdx:
            break
        curIdx = curMax

# T = O(nlog(n)); S = O(1)