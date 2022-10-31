# Medium

# Given an array of distinct positive integers representing coin denominations and a single non-negative
# integers n representing a target amount of money, write a function that returns the number of ways to
# make change for that target amount using the given coin denominations.

# Sample Input
# n = 6
# denoms = [1, 5]

# Sample Output
# 2

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    memo = [0 for _ in range(n + 1)]
    memo[0] = 1
    for i in range(len(denoms)):
        for j in range(1, n + 1):
            if j == denoms[i]:
                memo[j] = memo[j] + 1
            if j > denoms[i]:
                memo[j] = memo[j - denoms[i]] + memo[j]
    return memo[-1]


def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    memo = [0 for i in range(n + 1)]
    memo[0] = 1

    for denom in denoms:
        for j in range(n + 1):
            if j >= denom:
                memo[j] += memo[j - denom]
    return memo[-1]

## T = O(nd); S = O(n)