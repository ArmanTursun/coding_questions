# Easy

# Given an array of positive integers representing the values of coins in your possession, write a function that returns the
# minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive integer value
# and aren't necessarily unique (i.e., you can have multiple coins of the same value).

# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4.
# If you're given no coins, the minimum amount of change that you can't create is 1.

def nonConstructibleChange(coins):
    # Write your code here.

    if not coins:
        return 1

    coins.sort()
    changes = 0

    for coin in coins:
        if coin > changes + 1:
            return changes + 1

        changes = changes + coin

    return changes + 1

## T = O(nlog(n)); S = O(1)


### bit manipulation

def nonConstructibleChange(coins):
    total = sum(coins)
    possible = 0b1
    for val in coins:
        new = possible << val
        possible = possible | new

    possible = bin(possible)

    count = 0
    for ch in range(len(possible) - 1, 1, -1):
        if possible[ch] == '0':
            break
        count += 1

    return count

## T = O(n); S = O(1)