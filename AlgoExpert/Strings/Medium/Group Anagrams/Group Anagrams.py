# Medium

# Write a function that takes in an array of strings and groups anagrams together.
# Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and
# "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.
# Your function should return a list of anagrams groups in no particular order.

# Sample Input
# words = ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']

# Samole Output
# [['yo', 'oy'], ['act', 'cat', 'tac'], ['flop', 'olfp'], ['foo']]

from collections import defaultdict
def groupAnagrams(words):
    # Write your code here.
    sortedWords = defaultdict(list)
    for word in words:
        sortedWord = ''.join(sorted(word))
        sortedWords[sortedWord].append(word)
    return list(sortedWords.values())

# T = O(w * n * log(n)); S = O(w * n)
# where w is the length of each word, n is the number of words

