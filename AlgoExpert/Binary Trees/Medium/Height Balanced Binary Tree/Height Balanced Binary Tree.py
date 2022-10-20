# Medium

# You're given the root node of a Binary Tree. Write a function that returns tru if this Binary
# Tree is height balanced and false if it isn't.

# A Binary Tree is height balanced if for each node in the tree, the difference between the height
# of its left subtree and the height of its right subtree is at most 1.

# # Sample Input
# # tree       =     1
# #                /   \
# #               2     3
# #             /  \
# #            4    5
# #           /
# #          6
# # node = 5

# Sample Output
# False

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.
    isBalance, _ = getHeight(tree)
    return isBalance

def getHeight(tree):
    if not tree:
        return (True, 0)
    leftIsBalance, leftHeight = getHeight(tree.left)
    rightIsBalance, rightHeight = getHeight(tree.right)
    curHeight = max(leftHeight, rightHeight) + 1
    curIsBalance = leftIsBalance and rightIsBalance and abs(leftHeight - rightHeight) <= 1
    return (curIsBalance, curHeight)

# T = O(n); S = O(h)