# Very Hard

# Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged
# list of all of those arrays.

# The integers in the merged list should be in sorted order.

# Sample Input
# arrays = [
#   [1, 5, 9, 21],
#   [-1, 0],
#   [-124, 81, 121],
#   [3, 6, 12, 20, 150]]

# Sample Output
# [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]

from heapq import heappush, heappop, heapify
def mergeSortedArrays(arrays):
    # Write your code here.
    hp = []
    ## Create heap --- T = O(k); S = (k)
    for i, array in enumerate(arrays):
        hp.append((array[0], 0, i))

    heapify(hp) ## Heapify --- T = O(k); S = (1)

    result = []
    ## T = O(n * log(k))
    while hp:
        curValue, curIdx, curArrayIdx = heappop(hp)
        curArray = arrays[curArrayIdx]
        result.append(curValue)
        if curIdx < len(curArray) - 1:
            heappush(hp, (curArray[curIdx + 1], curIdx + 1, curArrayIdx))
    return result
## T = O(n * log(k) + k); S = (n + k) where n is the total number of nums
## k is the number of arrays