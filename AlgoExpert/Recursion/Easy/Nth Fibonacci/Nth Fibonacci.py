# Easy

# Write a function that takes in an integer n and returns the nth Fibonacci number.

# Important Note: the Fibonacci sequence is often defined with its first two numbers as
# F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number is F0;
# therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc...

# Sample Input
# n = 2
# Sample Output
# 1

# Sample Input
# n = 6
# Sample Output
# 5

# iteration (Bottom-Up DP)
def getNthFib(n):
    # Write your code here.
    f1 = 0
    f2 = 1
    if n == 1:
        return f1
    if n == 2:
        return f2

    temp1 = f1
    temp2 = f2
    temp = None
    for i in range(n - 2):
        temp = temp1
        temp1 = temp2
        temp2 = temp + temp1

    return temp2

# T = O(n); S = O(1)

# Recursion (Top-Down)
def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib(n-1) + getNthFib(n-2)

# T = O(2^n); S = O(n)

# Recursion(Top-Down with memo / Top-Down DP)
def getNthFib(n):
    # Write your code here.
    memo = {}
    memo[1] = 0
    memo[2] = 1
    return helper (n, memo)

def helper(n, memo):
    if n in memo:
        return memo[n]

    memo[n] = helper(n-1, memo) + helper(n-2, memo)
    return memo[n]

# T = O(n); S = O(n)