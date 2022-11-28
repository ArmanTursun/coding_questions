# Easy

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
#
#
# Example 1:
#
# Input: s = "leetcode"
# Output: 0

# Constraints:
#
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i, letter in enumerate(s):
            if letter not in count:
                count[letter] = [1, i]
            else:
                count[letter][0] += 1

        minIdx = -1
        for letter in count:
            if count[letter][0] == 1 and (count[letter][1] < minIdx or minIdx < 0):
                minIdx = count[letter][1]
        return minIdx if minIdx > -1 else -1
## T = O(n); S = O(n)