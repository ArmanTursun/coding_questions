# Easy

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Constraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = []
        for word in s:
            result.append(word[::-1])
        return ' '.join(result)
## T = O(n); S = O(n)