# Medium

# You're given two positve integers representing the width and height of a grid-shaped, rectangular graph. Write a
# function that returns the number of ways to reach the bottom right corner of the graph when starting at the top
# left corner. Each move you take must either go down or right. In other words, you can never move up or left in
# the graph.
# For example, given the graph illustrated blow, with width = 2 and height = 3, there are three ways to reach the
# bottom right corner when starting at the top left corner:

#  _ _
# |_|_|
# |_|_|
# |_|_|

# 1. Down, Down, Right
# 2. Right, Down, Down
# 3. Down, Right, Down

# Note: You may assume that width * height >= 2. In other words, the graph will never be a 1x1 grid.

# Sample Input
# width = 4, height = 3
# Sample Output
# 10

## Top-to-Down Recursive method
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    if width < 1 or height < 1:
        return 0
    if width == 1 and height == 1:
        return 1

    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)
## T = O(2^(n + m)); S = O(n + m)
## each position has two options, can it takes (n + m) calls to get to the edge.


## Top-to-Down Recursive DP with memo
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    memo = [[0 for i in range(width)] for j in range(height)]

    return dfs(memo, width - 1, height - 1)

def dfs(memo, width, height):
    if width < 0 or height < 0:
        return 0
    if width == 0 and height == 0:
        return 1

    if memo[height][width]:
        return memo[height][width]

    memo[height][width] = dfs(memo, width - 1, height) + dfs(memo, width, height - 1)
    return memo[height][width]
## T = O(n * m); S = O(n * m)

## Bottom-up DP with memo
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    memo = [[0 for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[-1][-1]
## T = O(n * m); S = O(n * m)


## Mathematical method
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    return factorial(width - 1 + height - 1) / (factorial(width - 1) * factorial(height - 1))

def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac
## T = O(n + m); S = O(1)
