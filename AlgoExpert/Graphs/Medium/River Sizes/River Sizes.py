# Medium

# You're given a two-dimensional array of potentially unequal height and width containing only 0 and 1.
# Each 0 represents part of a river. A river consists of any number of 1 that are either horizontally
# or vertically adjacent. The number of adjacent 1 forming a river determines its size.

# Write a function that returns an array of the sizes of all rivers represented in the input matrix.
# The sizes don't need to be in any particular order.

# Sample Input
#  matrix =   [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0] ]

# Sample Output
# [1, 2, 2, 2, 5]

def riverSizes(matrix):
    # Write your code here.
    memo = [[False for _ in matrix[0]] for i in matrix]
    rivers = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and not memo[i][j]:
                rivers.append(findRivers(i, j, matrix, memo))
    return rivers


def findRivers(i, j, matrix, memo):
    if i < 0 or j < 0 or i > len(matrix) - 1 or j > len(matrix[0]) - 1 or memo[i][j] or matrix[i][j] == 0:
        return 0
    memo[i][j] = True
    return 1 + findRivers(i + 1, j, matrix, memo) + findRivers(i - 1, j, matrix, memo) + findRivers(i, j + 1, matrix, memo) + findRivers(i, j - 1, matrix, memo)

## T = O(NxM); S = O(NxM + NxM) where second NxM is for recursion


from collections import deque


def riverSizes(matrix):
    # Write your code here.
    row = len(matrix)
    col = len(matrix[0])

    memo = [[False for _ in range(col)] for k in range(row)]
    rivers = []

    steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1 and not memo[i][j]:
                q = deque()
                q.append((i, j))
                memo[i][j] = True
                length = 0

                while q:
                    idxI, idxJ = q.popleft()
                    length += 1

                    for stepI, stepJ in steps:
                        nextI = idxI + stepI
                        nextJ = idxJ + stepJ
                        if nextI < 0 or nextI > row - 1: continue
                        if nextJ < 0 or nextJ > col - 1: continue
                        if matrix[nextI][nextJ] == 1 and not memo[nextI][nextJ]:
                            q.append((nextI, nextJ))
                            memo[nextI][nextJ] = True
                rivers.append(length)
    return rivers

## T = O(NxM); S = O(NxM + min(N, M))
## If original matrix can be modified, then we don't need extra memo
