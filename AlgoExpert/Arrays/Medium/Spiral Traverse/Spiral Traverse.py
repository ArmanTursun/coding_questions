# Medium

# Write a function that takes in an NxM two-dimensional array and returns a one-dimensional
# array of all the array's elements in spiral order.

# Spiral order starts at the top left corner of the two-dimensional array, goes to the right,
# and proceeds in a spiral pattern all the way until every elements has been visited.

# Sample Input
# array  =     [[1, 2, 3, 4],
#               [12, 13, 14 ,5],
#               [11, 16, 15, 6],
#               [10, 9, 8, 7]]

# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def spiralTraverse(array):
    # Write your code here.
    result = []
    start_i, end_i = 0, len(array) - 1
    start_j, end_j = 0, len(array[0]) - 1

    while start_i <= end_i and start_j <= end_j:
        for j in range(start_j, end_j + 1):
            result.append(array[start_i][j])
        for i in range(start_i + 1, end_i + 1):
            result.append(array[i][end_j])
        for j in range(end_j - 1, start_j - 1, -1):
            ## edge case: if there is only one row left in the matrix
            ## then we need to avoid double count the elements
            # [1, 2, 3, 4],
            # [10, 11, 12, 5],
            # [9, 8, 7, 6]

            if start_i == end_i:
                break
            result.append(array[end_i][j])
        for i in range(end_i - 1, start_i, -1):
            ## edge case: if there is only one col left in the matrix
            ## then we need to avoid double count the elements
            # [1, 2, 3],
            # [12, 13, 4],
            # [11, 14, 5],
            # [10, 15, 6],
            # [9, 8, 7]

            if start_j == end_j:
                break
            result.append(array[i][start_j])

        start_i += 1
        end_i -= 1
        start_j += 1
        end_j -= 1
    return result

## T = O(n); S = O(n) Space Complexity is O(n) if we count the result.