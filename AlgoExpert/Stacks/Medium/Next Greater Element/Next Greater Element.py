# Medium

# Write a function that takes in an array of integers and returns a new array of integers and returns a new
# array containing, at each index, the next lelement in the input array that's greater than the element at
# that index in the input array.

# In other words, your function should return a new array where outputArray[i] is the next element in the input
# array that's greater than inputArray[i]. If there's no such next greater element for a particular index, the
# value at that index in the output array should be -1. For example, given array = [1, 2], your function should
# return [2, -1].

# Additionally, your function should treat the input array as a circular array. A circular array wraps around
# itself as if it were connected end-to-end. So the next index after the last index in a circular array is the
# first index. This means that, for our problem, given array = [0, 0, 5, 0, 0, 3, 0, 0], the next greater element
# after 3 is 5, since the array is circular.

# Sample Input
# array = [2, 5, -3, -4, 6, 7, 2]

# Sample Output
# [5, 6, 6, 6, 7, -1, 5]

def nextGreaterElement(array):
    # Write your code here.
    result = []
    length = len(array)
    for i, num in enumerate(array):
        cur_idx = (i + 1)
        while cur_idx % length != i:
            if array[cur_idx % length] > num:
                break
            cur_idx += 1

        if cur_idx % length != i:
            result.append(array[cur_idx % length])
        else:
            result.append(-1)
    return result

# T = O(n ^ 2); S = O(n) space is for result.


def nextGreaterElement(array):
    # Write your code here.
    stack = []
    result = [-1 for _ in array]

    for i in range(2 * len(array)):
        idx = i % len(array)

        while stack and array[stack[-1]] < array[idx]:
            result[stack.pop()] = array[idx]
        stack.append(idx)

    return result

## T = O(n); S = O(n)



def nextGreaterElement(array):
    # Write your code here.
    stack = []
    result = [-1 for _ in array]

    for i in range(2 * len(array) - 1, -1, -1):
        idx = i % len(array)

        while stack:
            if stack[-1] > array[idx]:
                result[idx] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(array[idx])

    return result

## T = O(n); S = O(n)
