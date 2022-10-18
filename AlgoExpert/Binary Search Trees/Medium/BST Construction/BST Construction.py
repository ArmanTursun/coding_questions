# Medium

# Write a BST class for a Binary Search Tree. The class should support:
#   * Inserting values with the insert method.
#   * Removing values with the remove method; this method should only remove the first instance
#     of a given value.
#   * Searching for values with the contains method.

# Note that you can't remove values from a single-node tree. In other words, calling the remove
# method on a single-node tree should simply not do anything.

# Sample Usage
#              10
#          /        \
#         5          15
#       /  \       /   \
#      2    5     13   22
#     /            \
#    1             14

# insert(12)   10
#          /        \
#         5          15
#       /  \       /   \
#      2    5     13   22
#     /          /  \
#    1         12    14

# remove(10)   12
#          /        \
#         5          15
#       /  \       /   \
#      2    5     13   22
#     /             \
#    1               14

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        root = self
        while True:
            if value >= root.value:
                if root.right:
                    root = root.right
                else:
                    root.right = BST(value)
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = BST(value)
                    break
        return self

    def contains(self, value):
        # Write your code here.
        root = self
        while root:
            if root.value == value:
                return True
            if value > root.value:
                root = root.right
            else:
                root = root.left
        return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if not self or not self.left and not self.right:
            return self
        ## First find the node
        root = self
        prev = None
        while root:
            if root.value == value:
                break
            if value > root.value:
                prev = root
                root = root.right
            else:
                prev = root
                root = root.left

        ## The node need to be removed would have three kinds of cases:
        ## 1. leaf node: attach None to his parent node
        ## 2. have one child: replace it with his child.
        ## 3. have two children: replace it with his successor.

        ## if the node is a leaf node, then its parent's child would be None
        ## None should not be assigned directly, should be attached to cur_node's parent.
        if not root.left and not root.right:
            if root == prev.left:
                prev.left = prev.left.left
            else:
                prev.right = prev.right.right

        ## if the node only have one child, then its succeesor would be his only child
        elif not root.left:
            root.value = root.right.value
            root.right = root.right.right
        elif not root.right:
            root.value = root.left.value
            root.left = root.left.left

        ## if the node have two children, then replace it with the successor.
        else:
            prev = root
            cur = root.right

            while cur.left:
                prev = cur
                cur = cur.left

            root.value = cur.value
            if prev == root:
                prev.right = cur.right
            else:
                prev.left = cur.right

        return self

## All three methods
## Average: T = O(log(n)); S = O(1)
## Worst:   T = O(n);      S = O(1)