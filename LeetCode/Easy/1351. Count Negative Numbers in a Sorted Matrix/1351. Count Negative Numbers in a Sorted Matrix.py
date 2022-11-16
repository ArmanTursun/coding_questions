# Easy

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number
# of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i, j = len(grid) - 1, len(grid[0]) - 1
        total = 0

        while i > -1:
            if j > -1 and grid[i][j] < 0:
                total += 1
                j -= 1
                continue
            j = len(grid[0]) - 1
            i -= 1
        return total
## T = O(m * n); S = O(1)


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rowLength = len(grid[0])
        total = 0
        i = len(grid) - 1
        j = 0

        while i > -1:
            while j < len(grid[0]) and grid[i][j] >= 0:
                j += 1
            total += (rowLength - j)
            i -= 1
        return total
## T = O(m + n); S = O(1)