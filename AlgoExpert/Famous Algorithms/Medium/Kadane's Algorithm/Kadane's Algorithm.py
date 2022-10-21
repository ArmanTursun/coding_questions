# Medium
# LC 53

# Write a function that takes in a non-empty array of integers and returns the maximum sum that can be
# obtained by summing up all of the integers in a non-empty subarray of the input array. A subarray must
# only contain adjacent numbers.

# Sample Input
# array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

# Sample Output
# 19

### Divide and Conquer
def kadanesAlgorithm(array):
    # Write your code here.
    return maxSub (array, 0, len(array) - 1)

def maxSub(array, left, right):
    if left > right:
        return float("-inf")

    mid = (left + right) // 2

    cur_sum = sub = array[mid]
    for i in range(mid - 1, left - 1, -1):
        sub += array[i]
        cur_sum = max(cur_sum, sub)

    sub = cur_sum
    for j in range(mid + 1, right + 1):
        sub += array[j]
        cur_sum = max(cur_sum, sub)

    leftSum = maxSub(array, left, mid - 1)
    rightSum = maxSub(array, mid + 1, right)

    return max(leftSum, rightSum, cur_sum)

## T = O(nlog(n)); S = O(log(n))



# Kadane's Algorithm
def kadanesAlgorithm(array):
    # Write your code here.
    max_sum = 0
    final_max = float("-inf")

    for i in range(len(array)):
        max_sum = max(max_sum + array[i], array[i])
        if max_sum > final_max:
            final_max = max_sum
    return final_max

## T = O(n); S = O(1)
