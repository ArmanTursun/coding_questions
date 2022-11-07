# Medium

# Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to
# the root node of the trie and should support:
#   - Creating the trie from a string; this will be done by calling the populateSuffixTrieFrom method upon class
#     instruction, which should populate the root of the class.
#   - Searching for strings in the trie.

# Note that every string added to the trie should end with the special endSymbol character: "*".

# Sample Input
# string = "babc"

# Sample Output (Construction)
# {
#  "c": {"*": True},
#  "b": {
#    "c": {"*": True},
#    "a": {"b": {"c": {"*": True}}},
#  },
#  "a": {"b": {"c": {"*": True}}},
# }

# Sample Input (Searching)
# string = 'abc'

# Sample Output
# True


# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    ## T = O(n ^ 2); S = O(n ^ 2) where n is the length of the string
    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
            cur = self.root
            for j in range(i, len(string)):
                letter = string[j]
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur[self.endSymbol] = True

    ## T = O(n); S = O(1) where n is the length of the string
    def contains(self, string):
        # Write your code here.
        i = 0
        cur = self.root
        while i < len(string):
            if string[i] not in cur:
                return False
            cur = cur[string[i]]
            i += 1
        return cur.get(self.endSymbol, False)
