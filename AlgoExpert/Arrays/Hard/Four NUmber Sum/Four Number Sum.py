# Hard

# Write a function that takes in a non-empty array of distinct integers and an integer representing a target
# sum. The function should find all quadruplets in the array that sum up to the target sum and return a
# two-dimensional array of all these quadruplets in no particular order.
# If not four numbers sum up to the target sum, the function should return an empty array.

# Sample Input
# array = [7, 6, 4, -1, 1, 2]
# targetSum = 16

# Sample Output
# [[7, 6, 4, -1], [7, 6, 1, 2]]

def fourNumberSum(array, targetSum):
    # Write your code here.
    result = []
    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):
            for k in range(j + 1, len(array) - 1):
                for m in range(k + 1, len(array)):
                    if array[i] + array[j] + array[k] + array[m] == targetSum:
                        result.append([array[i], array[j], array[k], array[m]])
    return result
## T = (n ^ 4); S = O(1)


def fourNumberSum(array, targetSum):
    # Write your code here.
    result = []
    memo = {}

    for i in range(2, len(array) - 1):
        for k in range(0, i - 1):
            curSum = array[i - 1] + array[k]
            if curSum not in memo:
                memo[curSum] = [[array[i - 1], array[k]]]
            else:
                memo[curSum].append([array[i - 1], array[k]])
        for j in range(i + 1, len(array)):
            rest = targetSum - array[i] - array[j]
            if rest in memo:
                for restPair in memo[rest]:
                    curSet = [array[i], array[j]] + restPair
                    result.append(curSet)
    return result
## T = O(n^2); S = O(n^2)