# Hard

# Write a function that takes in a sorted array of distinct integers and returns the first index in the array
# that is equal to the value at that index. In other words, your function should return the minimum index where
# index == array[index]. If there is no such index, your function should return -1.

# Sample Input
# array = [-5, -3, 0, 3, 4, 5, 9]

# Sample Output
# 3

def indexEqualsValue(array):
    # Write your code here.
    for i, num in enumerate(array):
        if i == num:
            return i
    return -1
## T = O(n); S = O(1)


def indexEqualsValue(array):
    # Write your code here.
    start, end = 0, len(array) - 1

    idx = -1
    while start <= end:
        #print (start, end)
        mid = (start + end) // 2
        if array[mid] == mid:
            idx = mid
            end = mid - 1
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return idx
## T = O(log(n)); S = O(1)
