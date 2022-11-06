# Medium

# Write a function that takes in an array of unique integers and returns an array of all permutations of those
# integers in no particular order.

# If the input array is empty, the function should return an empty array.

# Sample Input
# array = [1, 2, 3]

# Sample Output
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def getPermutations(array):
    # Write your code here.
    permutations = []
    helper(array, [], permutations)
    return permutations

def helper(array, curPermutation, permutations):
    if not array and curPermutation:
        permutations.append(curPermutation)
        return

    for i in range(len(array)):
        newArray = array[:i] + array[i + 1:]
        helper(newArray, curPermutation + [array[i]], permutations)
## T = (n^2 * n!); S = (n * n!)


def getPermutations(array):
    # Write your code here.
    permutations = []
    helper(array, 0, permutations)
    return permutations

def helper(array, firstIdx, permutations):
    if firstIdx == len(array) - 1:
        permutations.append(array[:])
        return

    for i in range(firstIdx, len(array)):
        swap(array, firstIdx, i)
        helper(array, firstIdx + 1, permutations)
        swap(array, firstIdx, i)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
## T = (n * n!); S = (n * n!)