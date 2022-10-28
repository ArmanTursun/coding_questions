# Medium

# Given an array of positive integers representing coin denominations and a single non-negative integer n
# representing a target amount of money, write a function that returns the smallest number of coins needed
# to make change for that target amount using the given coin denominations.

# Note that you have access to an unlimited amount of coins. In other words, if the denominations are [1, 5, 10],
# you have access to an unlimited amount of 1, 5, 10. If it's impossible to make change for the target amount, return -1.

# Sample Input
# n = 7
# denoms = [1, 5, 10]

# Sample Output
# 3

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    memo = [[float("inf") for k in range(n + 1)] for _ in range(len(denoms) + 1)]
    for i in range(len(denoms) + 1):
        for j in range(n + 1):
            if j == 0:
                memo[i][j] = 0
                continue
            if j >= denoms[i-1]:
                memo[i][j] = min(memo[i][j - denoms[i-1]] + 1, memo[i - 1][j])
            else:
                memo[i][j] = memo[i - 1][j]
    print (memo)
    return memo[-1][-1] if memo[-1][-1] != float("inf") else -1
# T = O(nd); S = O(nd) where d is the number of denominations



def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    memo = [float("inf") for _ in range(n + 1)]
    memo[0] = 0

    for denom in denoms:
        for i in range(n + 1):
            if i >= denom:
                memo[i] = min(memo[i - denom] + 1, memo[i])
    return memo[-1] if memo[-1] != float("inf") else -1
# T = O(nd); S = O(n) where d is the number of denominations