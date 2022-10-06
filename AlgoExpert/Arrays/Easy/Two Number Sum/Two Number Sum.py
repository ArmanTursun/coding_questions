## Easy

# Write a function that takes in a non-empty array of distinct integers and an integer
# representing a target sum. If any two numbers in the input array sum up to the target
# sum, the function should return them in an array, in any order. If no two numbers sum
# up to the target sum, the function should return an empty array.

# Note that the target sum has to be obtained by summing two different integers in the array;
# you can't add a single integer to itself in order to obtain the target sum.

# You can assume that there will be at most one pair of numbers summing up to the target sum.

# Sample Input
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Sample Output
# [-1, 11]

################
## Solution 1

def twoNumberSum(array, targetSum):
    # Write your code here.
    length = len(array)
    result = []

    for i in range(length):
        for j in range(i + 1, length):
            if array[i] + array[j] == targetSum:
                result = [array[i], array[j]]

    return result

## T = O(n^2) ; S = O(1)

################
## Solution 2

def twoNumberSum(array, targetSum):
    # Write your code here.
    map = {}
    result = []

    for item in array:
        map[item] = True

    for item in array:
        if (targetSum - item) in map and (targetSum - item) != item:
            result = [item, targetSum - item]

    return result

#   map = {}
#    for num in array:
#        num2 = targetSum - num
#        if num2 in map:
#            return [num, num2]
#        else:
#            map[num] = True
#    return []

## T = O(n) ; S = O(n)

################
## Solution 3

def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        cur_sum = array[left] + array[right]
        if cur_sum == targetSum:
            return [array[left], array[right]]
        elif cur_sum < targetSum:
            left += 1
        else:
            right -= 1

    return []

## T = O(nlog(n)); S = O(1)