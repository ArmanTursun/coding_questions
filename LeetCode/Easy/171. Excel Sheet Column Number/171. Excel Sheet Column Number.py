# Easy

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding
# column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
# Example 1:
#
# Input: columnTitle = "A"
# Output: 1

# Constraints:
#
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for i in range(len(columnTitle)):
            num = ord(columnTitle[i]) - ord('A') + 1
            ex = len(columnTitle) - i - 1
            number += num * 26 ** ex
        return number
## T = O(n); S = O(1)