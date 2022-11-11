# Hard

# Write a function that takes in a sorted array of integers as well as a target integer. The function should
# use a variation of the Binary Search algorithm to find a range of indices in between which the target number
# is contained in the array and should return this range in the form of an array.

# The first number in the output array should represent the first index at which the target number is located,
# while the second number should represent the last index at which the target number is located. The function
# should return [-1, -1] if the integer isn't contained in the array.

# Sample Input
# array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
# target = 45

# Sample Output
# [4, 9]

def searchForRange(array, target):
    # Write your code here.
    left, right = helper(array, 0, len(array) - 1, target)
    return [left, right]
def helper(array, start, end, target):
    if start > end:
        return [-1, -1]
    mid = (start + end) // 2
    if array[mid] == target:
        leftLeft, leftRight = helper(array, start, mid - 1, target)
        rightLeft, rightRight = helper(array, mid + 1, end, target)
        left = leftLeft if leftLeft != -1 else mid
        right = rightRight if rightRight != -1 else mid
        return [left, right]
    elif array[mid] < target:
        return helper(array, mid + 1, end, target)
    else:
        return helper(array, start, mid - 1, target)
## T = O(log(n)); S = O(log(n))



def searchForRange(array, target):
    # Write your code here.
    range = [-1, -1]
    helper(array, 0, len(array) - 1, target, range, True)
    helper(array, 0, len(array) - 1, target, range, False)
    return range

def helper(array, start, end, target, range, goLeft):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    range[0] = mid
                    return
                else:
                    end = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    range[1] = mid
                    return
                else:
                    start = mid + 1
## T = O(log(n)); S = O(1)
