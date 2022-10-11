# Easy

# Write a function that takes in a Find Closest Value in BST (BST) and a target integer value
# and returns the closet value to that target value contained in the BST.

# You can assume that there will only be one closest value.

# Each BST node has an integer value, a left child node, and a right child node. A node
# is said to be a valid BST node if and only if it satisfies the BST property: its value
# is strictly greater than the values of every node to its left; its value is less than or
# equal to the values of every node to its right; and its children nodes are either valid
# BST nodes themselves or None/Null.

# Sample Input
# tree =       10
#            /    \
#           5     15
#         /  \   /  \
#        2   5  13  22
#       /        \
#      1         14
# target = 12

# Sample Output
# 13

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# recurssive
def findClosestValueInBst(tree, target):
    # Write your code here.
    return helper (tree, target, tree.value)

def helper (tree, target, cur_close):
    if not tree:
        return cur_close
    if tree.value == target:
        return tree.value

    if abs(target - cur_close) > abs(tree.value - target):
        cur_close = tree.value

    if target < tree.value:
        return helper(tree.left, target, cur_close)
    else:
        return helper(tree.right, target, cur_close)


# iterative
def findClosestValueInBst(tree, target):
    # Write your code here.
    cur_close = tree.value
    cur_diff = abs(tree.value - target)

    while tree:
        if tree.value == target:
            return tree.value
        if abs(tree.value - target) < cur_diff:
            cur_close = tree.value
            cur_diff = abs(tree.value - target)
        if target < tree.value:
            tree = tree.left
        else:
            tree = tree.right

    return cur_close

# T = O(log(n)); S = O(1)
# Worst: T = O(n; S = O(1)






