# Medium

# Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals,
# and returns the new intervals in no particular order.

# Sample Input
# intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

# Sample Output
# [[1, 2], [3, 8], [9, 10]]

import operator
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key = operator.itemgetter(0))
    result = []

    i = 0
    while i < len(intervals):
        if not result:
            result.append(intervals[i])
        elif intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(intervals[i][1], result[-1][1])
        else:
            result.append(intervals[i])
        i += 1
    return result

## T = O(nlog(n)); S = O(n)

# Follow up
# Solve without sorting
# We can use BST of intervals

# TODO

# https://leetcode.com/problems/merge-intervals/discuss/355318/Fully-Explained-and-Clean-Interval-Tree-for-Facebook-Follow-Up-No-Sorting
