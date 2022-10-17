# Medium

# Write a function that takes in an array of integers and returns the length of the longest peak in
# the array. A peak is defined as adjacent integers in the array that are strictly increasing until
# they reach a tip, at which point they become strictly decreasing. At least there integers are
# required to form a peak.

# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do
# the integers 1, 2, 2, 0.

# Sample Input
# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

# Sample Output
# 6

def longestPeak(array):
    # Write your code here.
    reachPeak = False
    cur_length = 0
    max_length = 0
    max = []

    for i in range(len(array) - 1):
        if not reachPeak and array[i] < array[i + 1]:  # otherwise reachPeach or array[i] >= array[i+1]
            cur_length += 1
        elif not reachPeak and array[i] > array[i + 1] and i > 0 and array[i - 1] < array[i]:
            # incase peak starts at index 0: [5, 4, 3, 2, 1, 2, 1]
            reachPeak = True
            cur_length += 1
        elif reachPeak and array[i] > array[i + 1]:
            cur_length += 1
        elif reachPeak and array[i] <= array[i + 1]:
            cur_length += 1
            if cur_length > max_length:
                max_length = cur_length
            if array[i] < array[i + 1]:
                cur_length = 1
                max = [array[i]]
            else:
                cur_length = 0
                max = []
            reachPeak = False
        else:
            cur_length = 0
            reachPeak = False
            max = []
    if reachPeak and array[-1] != array[-2]:
        cur_length += 1
        if cur_length > max_length:
            max_length = cur_length
    return max_length

##################################
###### More clear method #########
##################################

def longestPeak(array):
    # Write your code here.
    max_length = 0

    for i in range(1, len(array) - 1):
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            continue

        left = right = i
        while left > 0 and array[left] > array[left - 1]:
            left -= 1
        while right < len(array) - 1 and array[right] > array[right + 1]:
            right += 1

        max_length = max(right - left + 1, max_length)

    return max_length

## T = O(n); S = O(1)
