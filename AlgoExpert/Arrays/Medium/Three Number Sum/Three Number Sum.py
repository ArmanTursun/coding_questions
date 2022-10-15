# Medium

# Write a function takes in non-empty array of distinct integers and an integer representing a
# target sum. The function should find all triplets in the array that sum up to the target sum
# and return a two-dimensional array of all these triplets. The numbers in each triplet should
# be ordered in ascending order, and the triplets themselves should be ordered in ascending
# order with respect to the numbers they hold. If no three numbers sum up to the target sum,
# the function should return an empty array.

# Sample Input
# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0

# Sample Output
# [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

import operator


def threeNumberSum(array, targetSum):
    # Write your code here.
    length = len(array)
    result = []

    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if array[i] + array[j] + array[k] == targetSum:
                    sub_result = [array[i], array[j], array[k]]
                    sub_result.sort()  # O(1) compared to tree nested loop
                    result.append(sub_result)
    result.sort(key=operator.itemgetter(0, 1, 2))  # O(nlog(n))
    return result

## T = O(n^3); S = O(n)

def threeNumberSum(array, targetSum):
    # Write your code here.

    array.sort()  # O(nlog(n))
    result = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[i] + array[left] + array[right] == targetSum:
                # array was sorted, so we don't need to to sort again
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[i] + array[left] + array[right] < targetSum:
                left += 1
            else:
                right -= 1
    return result

## T = O(n^2); S = O(n)
