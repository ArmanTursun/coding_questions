# Easy

# Write a function that takes in a string of lowercase English-alphabet letters and returns
# the index of the string's first non-repeating character.

# If the input string doesn't have any non-repeating characters, your function should return -1.

# Sample Input
# string = "abcdcaf"

# Sample Output
# 1

def firstNonRepeatingCharacter(string):
    # Write your code here.
    map = {}
    for i, ch in enumerate(string):
        if ch not in map:
            map[ch] = i
        else:
            map[ch] = -1

    min = len(string)
    for ch in map:
        if map[ch] == -1:
            continue
        if map[ch] < min:
            min = map[ch]

    return -1 if min == len(string) else min

# T = O(n); S = O(1). The constance space is because O(26) = O(1)