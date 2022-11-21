# Easy

# Given a string s, return true if a permutation of the string could form a
# palindrome
#  and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "code"
# Output: false

# Constraints:
#
# 1 <= s.length <= 5000
# s consists of only lowercase English letters.

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)

        helper = 0
        for letter in counts:
            if counts[letter] % 2 == 1:
                helper += 1

        return helper == 1 or helper == 0
## T = O(n); S = O(1) hashmap would at most be 26