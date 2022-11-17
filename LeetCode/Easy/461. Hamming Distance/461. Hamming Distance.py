# Easy

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

# Example 1:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Constraints:
# 0 <= x, y <= 231 - 1

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
# T = O(1); S = O(1)


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        hammingDistance = 0
        while diff != 0:
            if diff % 2 != 0:
                hammingDistance += 1
            diff = diff >> 1
        return hammingDistance
# T = O(1); S = O(1)


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        hammingDistance = 0
        while diff != 0:
            hammingDistance += 1
            diff = diff & (diff - 1)
        return hammingDistance
# T = O(1); S = O(1)