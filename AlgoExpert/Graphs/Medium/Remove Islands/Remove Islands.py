# Medium

# You're given a two-dimensional array of potentially unequal height and width containing only 0 and 1.
# The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An
# island is defined as any number of 1 that are horizontally or vertically adjacent and that don't touch
# the border of the image. In other words, a group of horizontally or vertically adjacent 1 isn't an island
# if any of those 1 are in the first row, last row, first column or last column of the input matrix.

# Write a function that returns a modified version of the input matrix, where all of the islands are
# removed. You remove an island by replacing it with 0.

# Sample Input
# matrix = [
#   [1, 0, 0, 0, 0, 0],
#   [0, 1, 0, 1, 1, 1],
#   [0, 0, 1, 0, 1, 0],
#   [1, 1, 0, 0, 1, 0],
#   [1, 0, 1, 1, 0, 0],
#   [1, 0, 0, 0, 0, 1] ]

# Sample Output
# [ [1, 0, 0, 0, 0, 0],
#   [0, 0, 0, 1, 1, 1],
#   [0, 0, 0, 0, 1, 0],
#   [1, 1, 0, 0, 1, 0],
#   [1, 0, 0, 0, 0, 0],
#   [1, 0, 0, 0, 0, 1] ]

from copy import deepcopy


def removeIslands(matrix):
    # Write your code here.
    memo = deepcopy(matrix)
    markBorder(memo)
    remove(memo, matrix)
    return matrix


def markBorder(memo):
    for j in range(len(memo[0])):
        markVisited(memo, 0, j)
        markVisited(memo, len(memo) - 1, j)
    for i in range(len(memo)):
        markVisited(memo, i, 0)
        markVisited(memo, i, len(memo[0]) - 1)


def markVisited(memo, i, j):
    if i < 0 or i >= len(memo) or j < 0 or j >= len(memo[0]) or memo[i][j] != 1:
        return
    memo[i][j] = 0
    markVisited(memo, i + 1, j)
    markVisited(memo, i - 1, j)
    markVisited(memo, i, j + 1)
    markVisited(memo, i, j - 1)


def remove(memo, matrix):
    for i in range(len(memo)):
        for j in range(len(memo[0])):
            if memo[i][j] == 1:
                matrix[i][j] = 0

## T = O(MxN); S = O(MxN + MxN) where second MxN is for recursion


def removeIslands(matrix):
    # Write your code here.
    markBorder(matrix)
    remove(matrix)
    return matrix


def markBorder(matrix):
    for j in range(len(matrix[0])):
        markVisited(matrix, 0, j)
        markVisited(matrix, len(matrix) - 1, j)
    for i in range(len(matrix)):
        markVisited(matrix, i, 0)
        markVisited(matrix, i, len(matrix[0]) - 1)


def markVisited(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1:
        return
    matrix[i][j] = 2
    markVisited(matrix, i + 1, j)
    markVisited(matrix, i - 1, j)
    markVisited(matrix, i, j + 1)
    markVisited(matrix, i, j - 1)


def remove(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            if matrix[i][j] == 2:
                matrix[i][j] = 1

## T = O(MxN); S = O(MxN) where MxN is for recursion

