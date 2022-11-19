# Easy

# Given a string array words, return an array of all characters that show up in all strings within the words
# (including duplicates). You may return the answer in any order.

# Example 1:
#
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = defaultdict(list)

        for i in range(len(words)):
            curWord = words[i]
            for s in curWord:
                if s in counts and i == len(counts[s]) - 1:
                    counts[s][i] += 1
                elif i - 1 == len(counts[s]) - 1:
                    counts[s].append(1)

        result = []
        for letter in counts:
            if len(counts[letter]) == len(words):
                num = min(counts[letter])
                while num > 0:
                    result.append(letter)
                    num -= 1
        return result
## T = O(n * m); S = O(n * m)


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count1 = Counter(words[0])

        for i in range(1, len(words)):
            count2 = Counter(words[i])
            for letter in count2:
                if letter in count1:
                    count1[letter] = min(count1[letter], count2[letter])
            for letter in count1:
                if letter not in count2:
                    count1[letter] = 0
        result = []
        for letter in count1:
            while count1[letter] > 0:
                result.append(letter)
                count1[letter] -= 1
        return result

