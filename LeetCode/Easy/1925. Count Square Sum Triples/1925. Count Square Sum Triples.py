# Easy

# A square triple (a,b,c) is a triple where a, b, and c are integers and a^2 + b^2 = c^2.
#
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).

# Constraints:
#
# 1 <= n <= 250

class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                c = math.sqrt(i * i + j * j)
                if int(c) == c and c <= n:
                    result += 2
        return result