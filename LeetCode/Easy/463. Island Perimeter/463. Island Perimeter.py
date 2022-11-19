# Easy

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there
# is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is
# a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Constraints:
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += self.curPerimeter(grid, i, j)
        return perimeter

    def curPerimeter(self, grid, i, j):
        perimeter = 0
        if i == 0 or grid[i - 1][j] == 0:
            perimeter += 1
        if i == len(grid) - 1 or grid[i + 1][j] == 0:
            perimeter += 1
        if j == 0 or grid[i][j - 1] == 0:
            perimeter += 1
        if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
            perimeter += 1
        return perimeter
## T = O(n * m); S = O(1)


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i >= 1 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j >= 1 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter