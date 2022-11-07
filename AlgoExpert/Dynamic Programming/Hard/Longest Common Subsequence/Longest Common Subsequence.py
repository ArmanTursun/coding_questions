# Hard

# Write a function that takes in two strings and returns their longest common subsequence.
# A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in
# the same order as they appear in the string. For instance, the characters ["a", "c", "d"] form a subsequence
# of the string "abcd", and so do the characters ["b", "d"]. Note that a single character in a string and the string
# itself are both valid subsequences of the string.
# You can assume that there will only be one longest common subsequence.

# Sample Input
# str1 = "ZXVVYZW"
# str2 = "XKYKZPW"

# Sample Output
# ["X", "Y", "Z", "W"]

def longestCommonSubsequence(str1, str2):
    # Write your code here.
    lcs = []
    memo = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    i, j = len(memo) - 1, len(memo[0]) - 1
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        else:
            if memo[i-1][j] > memo[i][j-1]:
                i -= 1
            else:
                j -= 1
    return lcs[::-1]
## T = O(n*m); S = O(n*m)
