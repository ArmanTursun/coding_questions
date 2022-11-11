# Hard

# Write a function that takes in a big stirng and an array of small strings, all of which are smaller in length
# than the big string. The function should return an array of booleans, where each boolean represents whether
# the small string at that index in the array of small strings is contained in the big string.
# Note that you can't use language-built-in string-matching methods.

# Sample Input
# bigString = 'this is a big string'
# smallStrings = ['this', 'yo', 'is', 'a', 'bigger', 'string', 'kappa']

# Sample Output
# [true, false, true, true, false, true, false]

# Sample Input
# bigString = 'abcdefghijklmnopqrstuvwxyz'
# smallStrings = ['abc', 'mnopqr', 'wyz', 'no', 'e', 'tuuv']

# Sample Output
# [true, true, false, true, true, false]

## SuffixTrie
def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    result = [False for string in smallStrings]

    Trie = SuffixTrie(bigString)

    for i in range(len(smallStrings)):
        curString = smallStrings[i]
        #print (curString)
        result[i] = Trie.contains(curString)
    return result


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            cur = self.root
            for j in range(i, len(string)):
                letter = string[j]
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]

    def contains(self, string):
        # Write your code here.
        i = 0
        cur = self.root
        while i < len(string):
            if string[i] not in cur:
                return False
            cur = cur[string[i]]
            i += 1
        return True
## T = O(b^2 + ns); S = O(n^2 + n)



## PrefixTrie
def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    trie = Trie()
    for i, string in enumerate(smallStrings):
        trie.add(string, i)

    result = [False for string in smallStrings]
    isMatch(trie.root, bigString, result)
    return result


def isMatch(root, bigString, result):
    for i in range(len(bigString)):
        cur = root
        j = i
        while j < len(bigString) and bigString[j] in cur:
            cur = cur[bigString[j]]
            if not cur:
                break
            if '#' in cur:
                result[cur['#']] = True
            j += 1


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, string, idx):
        cur = self.root
        for ch in string:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['#'] = idx
## T = O(ns + bs); S = O(ns)
## where n is the number of smallStrings, s is the length of smallstring
## b is the length of bigString