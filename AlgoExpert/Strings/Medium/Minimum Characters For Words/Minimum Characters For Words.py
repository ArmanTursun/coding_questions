# Medium

# Write a function that takes in an array of words and returns the smallest array of characters needed to form
# all of the words. The characters don't need to be in any particular order.

# For example, the characters [y, r, o, u] are needed to form the words [your, you, or, yo].
# Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

# Sample Input
# words = [this, that, did, deed, them!, a]

# Sample Output
# [t, t, h, i, s, a, d, d, e, e, m, !]

from collections import defaultdict
def minimumCharactersForWords(words):
    # Write your code here.
    chs = defaultdict(list)
    for word in words:
        sub_chs = defaultdict(list)
        for ch in word:
            sub_chs[ch].append(ch)

        for letter in sub_chs:
            if letter not in chs or len(sub_chs[letter]) > len(chs[letter]):
                chs[letter] = sub_chs[letter]

    result = []
    for item in chs:
        for characters in chs[item]:
            result.append(characters)
    return result

## T = O(wn); S = O(wn) where w is average length of each word and n is the
## number of words.


def minimumCharactersForWords(words):
    # Write your code here.
    chs = {}
    for word in words:
        sub_chs = {}
        for ch in word:
            if ch not in sub_chs:
                sub_chs[ch] = 1
            else:
                sub_chs[ch] += 1

        for letter in sub_chs:
            if letter not in chs or sub_chs[letter] > chs[letter]:
                chs[letter] = sub_chs[letter]

    result = []
    for item in chs:
        for i in range(chs[item]):
            result.append(item)
    return result

## T = O(wn); S = O(c) where w is average length of each word and n is the
## number of words. c is the number of unique characters.
