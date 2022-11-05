# Midium

# Write a function that takes in two strings and returns the minimum number of edit operations that need to be
# performed on the first string to obtain the second string.

# There are three edit operations: insertion of a character, deletion of a character, and substitution of a character
# for another.

# Sample Input
# str1 = "abc"
# str2 = "yabd"

# Sample Output
# 2

def levenshteinDistance(str1, str2):
    # Write your code here.
    memo = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0 or j == 0:
                memo[i][j] = max(i, j)
                continue
            if str1[i - 1] == str2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1]
            else:
                memo[i][j] = min(memo[i-1][j-1], memo[i-1][j], memo[i][j-1]) + 1

    return memo[-1][-1]
## T = O(n * m); S = O(n * m)


def levenshteinDistance(str1, str2):
    # Write your code here.
    if len(str1) < len(str2):
        short, long = str1, str2
    else:
        short, long = str2, str1

    prev = [x for x in range(len(short) + 1)]
    cur = [None for i in range(len(short) + 1)]

    for i in range(1, len(long) + 1):
        tempPrev = prev
        tempCur = cur
        tempCur[0] = i
        for j in range(1, len(short) + 1):
            if long[i-1] == short[j-1]:
                tempCur[j] = tempPrev[j-1]
            else:
                tempCur[j] = min(tempPrev[j-1], tempPrev[j], tempCur[j-1]) + 1
        prev = tempCur
        cur = tempPrev
    return prev[-1]
## T = O(n * m); S = O(min(m, n))
