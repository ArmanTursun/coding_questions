# Easy

# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such
# that their sum is equal to the given target.
#
#
#
# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        tree = []
        self.serialze(root, tree)
        i, j = 0, len(tree) - 1

        while i < j:
            if tree[i] + tree[j] == k:
                return True
            if tree[i] + tree[j] < k:
                i += 1
            else:
                j -= 1
        return False

    def serialze(self, root, tree):
        if not root:
            return
        self.serialze(root.left, tree)
        tree.append(root.val)
        self.serialze(root.right, tree)
## T = O(n); S = O(n)