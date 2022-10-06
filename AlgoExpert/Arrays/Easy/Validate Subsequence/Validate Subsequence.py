## Easy

# Given two non-empty arrays of integers, write a function that determines whether
# the second array is a subsequence of the first one.

# A subsequence of an array is a set of numvers that aren't necessarily adjacent in the
# array but that are in the same order as they appear in the array.

# For instance, the numbers [1, 2, 3, 4] form a subsequence of the array [1, 2, 3, 4],
# and so do the numvers [2, 4].

# Note that a single number in an array and the array itself are both valid subsequences
# of the array.

# Sample Input
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# Sample Output
# True

def isValidSubsequence(array, sequence):
    # Write your code here.
    i, j = 0, 0

    while j < len(sequence) and i < len(array):
        if array[i] == sequence[j]:
            j += 1
        i += 1

    return j == len(sequence)

## T = O(n) ; S = O(1)

## Use DP, longest common subsequence. Make it worse, but good to practice DP.

def isValidSubsequence(array, sequence):
    # Write your code here.
    dp = [[0] * (len(sequence) + 1) for _ in range(len(array) + 1)]

    for i in range(1, len(array) + 1):
        for j in range(1, len(sequence) + 1):
            if array[i-1] == sequence[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return True if dp[len(array)][len(sequence)] == len(sequence) else False

## T = O(mn) ; S = O(mn)