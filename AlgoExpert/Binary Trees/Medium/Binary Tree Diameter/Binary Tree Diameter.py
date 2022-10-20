# Medium

# Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree
# is defined as the length of its longest path, even if that path doesn't pass through the root of tree.

# A path is a collection of connected nodes in a tree, where no node is connected to more than two other
# nodes. The length of a path is the number of edges between the path's first node and its last node.

# Sample Input
#  tree    =     1
#               / \
#              3   2
#             / \
#            7   4
#           /     \
#          8       5
#         /         \
#        9           6

# Sample Output
# 6

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    _, max = helper(tree)
    return max


def helper(tree):
    if not tree:
        return (-1, -1)

    left_height, left_max = helper(tree.left)
    right_height, right_max = helper(tree.right)
    cur_max = max(left_max, right_max, left_height + right_height + 2)
    cur_height = max(left_height, right_height) + 1

    return (cur_height, cur_max)

## T = O(n); S = O(h)