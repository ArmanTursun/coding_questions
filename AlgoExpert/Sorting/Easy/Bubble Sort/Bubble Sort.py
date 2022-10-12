# Easy

# Write a function to sort with Bubble Sort

# Sample Input
# array = [8, 5, 2, 9, 5, 6, 3]

# Sample Output
# [2, 3, 5, 5, 6, 8, 9]

def bubbleSort(array):
    # Write your code here.
    flag = True

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break
    return array