# Easy

# Write a function to sort with Select Sort

# Sample Input
# array = [8, 5, 2, 9, 5, 6, 3]

# Sample Output
# [2, 3, 5, 5, 6, 8, 9]

def selectionSort(array):
    # Write your code here.

    for i in range(len(array)):
        cur = i
        for j in range(i + 1, len(array)):
            if array[cur] > array[j]:
                cur = j
        array[i], array[cur] = array[cur], array[i]

    return array

# T = O(n^2); S = O(1)