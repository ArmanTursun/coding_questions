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