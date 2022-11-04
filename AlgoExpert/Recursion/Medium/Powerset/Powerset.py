# Medium

# Write a function that takes in an array of unique integers and returns its powerset.
# The powerset P(X) of a set X is the set of all subsets of X. For example, the powerset of [1, 2] is [[], [1], [2], [1, 2]].
# Note that the sets in the powerset do not need to be in any particular order.

# Sample Input
# array = [1, 2, 3]

# Sample Output
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

def powerset(array):
    # Write your code here.
    result = [[]]
    helper(array, 0, result)
    return result


def helper(array, idx, result):
    if idx == len(array):
        return
    num = array[idx]
    for i in range(len(result)):
        subSet = result[i]
        result.append(subSet + [num])
    helper(array, idx + 1, result)


def powerset(array):
    # Write your code here.
    result = [[]]
    for num in array:
        for i in range(len(result)):
            subSet = result[i]
            result.append(subSet + [num])
    return result
## T = O(n * 2^n); S = O(n * 2^n)