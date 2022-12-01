# Easy

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
# magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Constraints:
#
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)

        for letter in ransomNote:
            if letter not in counts:
                return False
            counts[letter] -= 1

        for letter in counts:
            if counts[letter] < 0:
                return False
        return True

## T = O(n); S = O(n + m)


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # Reverse sort the note and magazine. In Python, we simply
    # treat a list as a stack.
    ransomNote = sorted(ransomNote, reverse=True)
    magazine = sorted(magazine, reverse=True)

    # While there are letters left on both stacks:
    while ransomNote and magazine:
        # If the tops are the same, pop both because we have found a match.
        if ransomNote[-1] == magazine[-1]:
            ransomNote.pop()
            magazine.pop()
        # If magazine's top is earlier in the alphabet, we should remove that
        # character of magazine as we definitely won't need that letter.
        elif magazine[-1] < ransomNote[-1]:
            magazine.pop()
        # Otherwise, it's impossible for top of ransomNote to be in magazine.
        else:
            return False
            # Return true iff the entire ransomNote was built.
    return not ransomNote
## T = O(mlog(m) + nlog(n)); S = O(m + n)