# Hard

# You're given an array of arrays where each subarray holds two integer values and represents an item;
# the first integer is the item's value, and the second integer is the item's weight. You're also given
# an integer representing the maximum capacity of a knapsack that you have.

# Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's
# capacity, all the while maximizing their combined value. Note that you only have one of wach item at your
# disposal.
# Write a function that returns the maximized comnbined value of the items that you should pick as well
# as an array of the indices of each item picked.

# Sample Input
# items = [[1, 2], [4, 3], [5, 6], [6, 7]]
# capacity = 10

# Sample Output
# [10, [1, 3]] // items [4, 3], [6, 7]

def knapsackProblem(items, capacity):
    # Write your code here.

    memo = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        itemValue, itemWeight = items[i - 1]
        for j in range(1, capacity + 1):
            if j < itemWeight:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j - itemWeight] + itemValue, memo[i - 1][j])

    k = len(memo) - 1
    l = len(memo[0]) - 1
    selectedItems = []
    while k > 0:
        if memo[k][l] != memo[k - 1][l]:
            selectedItems.append(k - 1)
            l -= items[k - 1][1]
            k -= 1
        else:
            k -= 1

    return [memo[-1][-1], selectedItems]
## T = O(nc); S = O(nc) where n is the number of items, and c is capacity