# Easy

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]

# Constraints:
#
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}

        for word in s1.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

        for word in s2.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

        result = []
        for word in count:
            if count[word] == 1:
                result.append(word)
        return result
## T = O(n); S = O(n)