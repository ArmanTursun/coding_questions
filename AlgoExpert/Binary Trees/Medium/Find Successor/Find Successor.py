# Medium

# Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent)
# node) as well as a ndoe contained in that tree and returns the given node's successor.

# A node's successor is the next ndoe to be visited (immediately after the given node) when traversing
# its tree using the in-order tree-traversal technique. A node has no success if it's the last node to
# be visited in the in-order traversal.

# If a node has no successor, your function should return None/null.

# Sample Input
# tree       =     1
#                /   \
#               2     3
#             /  \
#            4    5
#           /
#          6
# node = 5

# Sample Output
# 1

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right:
        return successor(node.right)
    while node.parent and node != node.parent.left:
        node = node.parent
    return node.parent

def successor(tree):
    while tree.left:
        tree = tree.left
    return tree

# T = O(h); S = O(1)
