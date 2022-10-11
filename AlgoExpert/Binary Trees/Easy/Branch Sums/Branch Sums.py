# Easy

# Write a function that takes in a Binary Tree and returns a list of its branch sums ordered
# from leftmost branch sum to rightmost branch sum.

# A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a
# path of nodes in a tree that starts at the root node and ends at any leaf node.

# Sample Input
# tree =           1
#              /      \
#             2        3
#           /   \    /   \
#          4     5  6     7
#         / \   /
#        8   9 10

# Sample Output
# [15, 16, 18, 19, 11]
# 15 == 1 + 2 + 4 + 8
# 16 == 1 + 2 + 4 + 9
# 18 == 1 + 2 + 5 + 10
# 10 == 1 + 3 + 6
# 11 == 1 + 3 + 7

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    result = []
    helper(root, result, 0)
    return result


def helper(root, result, cur_sum):
    cur_sum += root.value

    if not root.left and not root.right:
        result.append(cur_sum)
        return

    if root.left:
        helper(root.left, result, cur_sum)
    if root.right:
        helper(root.right, result, cur_sum)

# T = O(n); S = O(n)