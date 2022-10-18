# Medium

# Write a function that takes in a potentially invalid Binary Search Tree and returns a
# boolean representing whether the BST is valid.

# Sample Usage
#              10
#          /        \
#         5          15
#       /  \       /   \
#      2    5     13   22
#     /            \
#    1             14

# Sample Output
# True

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return helper(tree, float("-inf"), float("inf"))


def helper(tree, minValue, maxValue):
    if not tree:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False

    return helper(tree.left, minValue, tree.value) and helper(tree.right, tree.value, maxValue)

## T = O(n); S = O(d) where d is the height of BST


################################################
###### Only works with non-equal elements ######
################################################

def validateBst(tree):
    # Write your code here.
    #          4
    #        /   \
    #       2     5
    #      / \
    #     1   6
    # inorder traverse: 1, 2, 6, 4, 5  ==>  6 appear before 4 ==> False

    # Keep tracking the previous max value after every round after vesited left child.
    # prev_max contains the max value of left sub tree.
    # After visited left sub tree, refresh it with root.value
    # Then go to right sub tree
    return inorder(tree)

pre_max = float("-inf")
def inorder(tree):
    global pre_max, array

    if not tree:
        return True
    if not inorder(tree.left):
        return False
    if tree.value <= pre_max:
        return False
    pre_max = tree.value
    return inorder(tree.right)
