# Easy

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

# Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Constraints:
# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ''.join(word1)
        string2 = ''.join(word2)

        if len(string1) != len(string2):
            return False
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return False
        return True
## T = O(n); S = O(n)


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordpointer1 = 0
        wordpointer2 = 0
        stringpointer1 = 0
        stringpointer2 = 0
        length1 = len(word1)
        length2 = len(word2)

        while wordpointer1 < length1 and wordpointer2 < length2:
            if word1[wordpointer1][stringpointer1] != word2[wordpointer2][stringpointer2]:
                return False
            if stringpointer1 == len(word1[wordpointer1]) - 1:
                wordpointer1 += 1
                stringpointer1 = 0
            else:
                stringpointer1 += 1
            if stringpointer2 == len(word2[wordpointer2]) - 1:
                wordpointer2 += 1
                stringpointer2 = 0
            else:
                stringpointer2 += 1
        if wordpointer1 != length1 or wordpointer2 != length2:
            return False
        return True
## T = O(n); S = O(1)