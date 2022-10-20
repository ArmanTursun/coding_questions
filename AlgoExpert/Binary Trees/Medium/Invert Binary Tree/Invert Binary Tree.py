# Medium

# Write a function that takes in a Binary Tree and inverts it. In other words, the function should
# swap every left node in the tree for its corresponding right node.

# Sample Input
#  tree      =       1
#                  /   \
#                 2     3
#                / \   / \
#               4   5 6   7
#              / \
#             8   9

#  tree      =       1
#                  /   \
#                 3     2
#                / \   / \
#               7   6 5   4
#                        / \
#                       9   8

from collections import deque
def invertBinaryTree(tree):
    # Write your code here.
    q = deque()
    q.append(tree)

    while q:
        root = q.popleft()
        if not root:
            continue
        root.left, root.right = root.right, root.left
        q.append(root.left)
        q.append(root.right)
    return tree

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# T = O(n); S = O(n)



def invertBinaryTree(tree):
    # Write your code here.
    if not tree:
        return

    temp = tree.left
    tree.left = tree.right
    tree.right = temp

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# T = O(n); S = O(d) where d is the depth
