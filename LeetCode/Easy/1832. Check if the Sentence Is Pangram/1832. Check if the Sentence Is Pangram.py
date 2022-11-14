# Easy

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Constraints:
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for ch in sentence:
            s.add(ch)
        return len(s) == 26
# T = O(n); S = (1) set is at most 26 so O(1)


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        bitmap = 0

        for ch in sentence:
            move = ord(ch) - ord('a')
            bitmap |= 1 << move

        return bitmap == 2 ** 26 - 1