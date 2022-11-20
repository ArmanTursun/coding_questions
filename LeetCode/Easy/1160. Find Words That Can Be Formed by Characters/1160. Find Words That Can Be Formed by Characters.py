# Easy

# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countCharacters = Counter(chars)
        result = 0

        for word in words:
            count = Counter(word)
            flag = True
            for letter in count:
                if letter not in countCharacters or count[letter] > countCharacters[letter]:
                    flag = False
                    break
            if flag:
                result += len(word)
        return result
## T = O(n * m + k); S = O(n * m + k) where n is the number of words, m is the length of each word
## k is the length of chars