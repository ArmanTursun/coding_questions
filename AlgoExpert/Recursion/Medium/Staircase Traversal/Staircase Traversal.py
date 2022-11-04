# Medium

# You're given two positive integers representing the height of a staircase and the maximum number of steps that you can
# advance up the staircase at a time. Write a function that returns the number of ways in which you can climb the staricase.
# For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways.
# You could take 1 step, 1 step, then 1 step, you can also take 1 step, then 2 steps, and you could take 2 steps, tehn 1 step.

# Note that maxSteps <= height will always be true.

def staircaseTraversal(height, maxSteps):
    # Write your code here.
    if height == 0:
        return 1
    curNum = 0
    for i in range(1, min(maxSteps, height) + 1):
        curNum += staircaseTraversal(height - i, maxSteps)
    return curNum

## T = O(k ^ n); S = O(n) where k is the maxSteps, n is the height


def staircaseTraversal(height, maxSteps):
    # Write your code here.
    memo = {}
    return helper(height, maxSteps, memo)

def helper(height, maxSteps, memo):
    if height == 0:
        return 1
    if height in memo:
        return memo[height]
    memo[height] = 0
    for i in range(1, min(maxSteps, height) + 1):
        memo[height] += staircaseTraversal(height - i, maxSteps)
    return memo[height]

## T = O(n * k; S = O(n) where k is the maxSteps, n is the height
## different from Fibonacci because this is k-way tree.


def staircaseTraversal(height, maxSteps):
    # Write your code here.
    ways = [1, 1]

    for curHeight in range(2, height + 1):
        curWays = 0
        for i in range(1, min(maxSteps, curHeight) + 1):
            curWays += ways[curHeight - i]
        ways.append(curWays)
    return ways[-1]

## T = O(n * k; S = O(n) where k is the maxSteps, n is the height
## different from Fibonacci because this is k-way tree.

def staircaseTraversal(height, maxSteps):
    # Write your code here.
    ways = [1, 1]

    for curHeight in range(2, height + 1):
        windowStart = curHeight - maxSteps - 1
        windowEnd = curHeight - 1

        curWays = ways[-1]
        if windowStart >= 0:
            curWays -= ways[windowStart]
        curWays += ways[windowEnd]
        ways.append(curWays)
    return ways[-1]

## T = O(n); S = O(n)