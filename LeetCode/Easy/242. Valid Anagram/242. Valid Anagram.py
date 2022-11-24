# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true

# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = Counter(s)
        counts2 = Counter(t)

        for letter in counts1:
            if letter not in counts2 or counts1[letter] != counts2[letter]:
                return False
        for letter in counts2:
            if letter not in counts1 or counts2[letter] != counts1[letter]:
                return False
        return True
## T = O(n); S = O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)
        sList.sort()
        tList.sort()
        return sList == tList
# T = O(nlog(n)); S = O(n)