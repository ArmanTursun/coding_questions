# Medium

# Write a function that takes in an integer matrix of potentially unqual height and width and returns the minimum
# number of passes required to convert all negative integers in the matrix to positive integers.

# A negetive integer in the matrix can only be converted to a positive integer if one or more of its adjacent elements
# is positive. An adjacent element is an element that is to the left, to the right, above, or below the current element
# in the matrix. Converting a negative to a positive simply involves multiplying it by -1.

# A single pass through the matrix involves converting all the negative integers that can be converted at a particular
# point in time. For example, consider the following input matrix:
# [ [0, -2, -1],
#   [-5, 2, 0],
#   [-6, -2, 0] ]
# After the first pass, only 3 values can be converted to positives:
# [ [0, 2, -1],
#   [5, 2, 0],
#   [-6, 2, 0] ]
# After a second pass
# [ [0, 2, 1],
#   [5, 2, 0],
#   [6, 2, 0] ]

## If the input matrix can't all be converted to positives, regardless of how many passes are run, your function should
# return -1.

from collections import deque
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    q = deque()
    steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    total_pass = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                q.append([(i, j), total_pass])

    while q:
        (idx_i, idx_j), round = q.popleft()
        for step_i, step_j in steps:
            next_i, next_j = idx_i + step_i, idx_j + step_j
            if stepValid(next_i, next_j, matrix) and matrix[next_i][next_j] < 0:
                matrix[next_i][next_j] *= -1
                q.append([(next_i, next_j), round + 1])

        if round > total_pass:
            total_pass = round

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                return -1
    return total_pass

def stepValid(next_i, next_j, matrix):
    if next_i < 0 or next_j < 0 or next_i >= len(matrix) or next_j >= len(matrix[0]):
        return False
    return True

## T = O(NxM); S = O(NxM)
