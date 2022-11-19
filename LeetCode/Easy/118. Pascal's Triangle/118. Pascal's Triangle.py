# Easy

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Constraints:
# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            if not result:
                result.append([1])
                continue
            lastRowLength = len(result[i - 1])
            lastRow = result[i - 1]
            curRow = [1]
            for j in range(lastRowLength - 1):
                curRow.append(lastRow[j] + lastRow[j + 1])
            curRow.append(1)
            result.append(curRow)
        return result
## T = O(n); S = O(1)