# Medium

# Write a function that takes in an array of integers and returns a sorted version of that array. Use the
# Quick Sort algorithm to sort the array.

def quickSort(array):
    # Write your code here.
    QuickSort(array,  0, len(array) - 1)
    return array

def QuickSort(array, left, right):
    if left >= right:
        return
    p = left
    i = left
    j = right
    while i <= j:
        if array[p] >= array[i]:
            i += 1
        if array[p] <= array[j]:
            j -= 1
        if i <= j and array[p] < array[i] and array[p] > array[j]:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    array[p], array[j] = array[j], array[p]

    QuickSort(array, left, j - 1)
    QuickSort(array, j + 1, right)

## Worst: T = O(n ^ 2); S = O(log(n))
## Average and Best: T = O(nlog(n)); S = O(log(n))