# Easy

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
#
# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            curNum = matrix[i][0]
            row, col = i, 0
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != curNum:
                    return False
                row += 1
                col += 1
        for j in range(len(matrix[0])):
            curNum = matrix[0][j]
            row, col = 0, j
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != curNum:
                    return False
                row += 1
                col += 1
        return True

# Follow up 1:
# What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the
# matrix into the memory at once?

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True


# Follow up 2:
# What if the matrix is so large that you can only load up a partial row into the memory at once?

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))