# Easy

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number
# is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Constraints:
# 0 <= n <= 30

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        f0 = 0
        f1 = 1
        for i in range(2, n + 1):
            temp = f0 + f1
            f0 = f1
            f1 = temp
        return f1
# T = O(n); S = O(1)
## For more solutions, check on https://leetcode.com/problems/fibonacci-number/solutions/362772/fibonacci-number/