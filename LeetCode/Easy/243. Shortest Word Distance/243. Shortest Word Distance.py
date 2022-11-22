# Easy

# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return
# the shortest distance between these two words in the list.
#
#
#
# Example 1:
#
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3

# Constraints:
#
# 2 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = p2 = -1
        dis = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word == word1:
                p1 = i
            if word == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                dis = min(dis, abs(p1 - p2))
        return dis
## T = O(n * m); S = O(1) where m is the length word, n is the number of words