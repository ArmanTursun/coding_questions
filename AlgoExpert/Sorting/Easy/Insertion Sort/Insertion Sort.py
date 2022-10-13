# Easy

# Write a function to sort with Insertion Sort

# Sample Input
# array = [8, 5, 2, 9, 5, 6, 3]

# Sample Output
# [2, 3, 5, 5, 6, 8, 9]

def insertionSort(array):
    # Write your code here.
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array

# Best: T = O(n); S = O(1)
# Average/Worst: T = O(n^2); S = O(1)