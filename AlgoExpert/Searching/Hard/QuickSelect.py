# Write a function that takes in an array of distinct integers as well as an
# integer k and that returns the kth smallest integer in that array.

# The function should do this in linear time, on average.

# Sample Input
# array = [8, 5, 2, 9, 7, 6, 3]
# k = 3

# Sample Output
# 5

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def partition(array, start, end, k):
    while True:
        p = start
        left = p + 1
        right = end
        while left <= right:  ## Similar to QuickSearch
            if array[left] > array[p] and array[right] < array[p]:
                swap(left, right, array)
            if array[left] <= array[p]:
                left += 1
            if array[right] >= array[p]:
                right -= 1
        swap(p, right, array)
        if right == k:
            return array[right]
        elif right < k:
            start = right + 1
        else:
            end = right - 1


def quickselect(array, k):
    return partition(array, 0, len(array) - 1, k - 1)

## Best:  T = O(n); S = O(1)
## Average:  T = O(n); S = O(1)
## Worst:  T = O(n^2); S = O(1)

