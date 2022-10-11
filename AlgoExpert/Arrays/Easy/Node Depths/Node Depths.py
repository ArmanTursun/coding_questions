# Easy

# The distance between a node in a Binary Tree and the tree's root is called the node's depth.
# Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

# Sample Input
# tree    =      1
#             /     \
#            2       3
#          /  \    /  \
#         4   5   6    7
#        / \
#       8   9

# Sample output 16 = 1 + 1 + 2 + 2 + 2 + 2 + ... + 3 + 3 = 16

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# DFS recurssive
def nodeDepths(root):
    # Write your code here.
    return helper(root, 0)


def helper(root, depth):
    if not root:
        return 0
    return depth + helper(root.left, depth + 1) + helper(root.right, depth + 1)

# DFS iteration
def nodeDepths(root):
    # Write your code here.
    sum = 0
    stack = [(root, 0)]

    while stack:
        cur_node, cur_depth = stack.pop()
        sum += cur_depth
        if cur_node.left:
            stack.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            stack.append((cur_node.right, cur_depth + 1))

    return sum

# BSF
from collections import deque
def nodeDepths(root):
    # Write your code here.
    sum = 0
    q = deque()
    q.append((root, 0))

    while q:
        cur_node, cur_depth = q.popleft()
        sum += cur_depth
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))

    return sum

# T = O(n); S = O(h);    h is the height of the tree

