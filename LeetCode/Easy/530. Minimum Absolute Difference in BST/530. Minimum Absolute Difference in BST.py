# Easy

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two
# different nodes in the tree.
#
# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Constraints:
#
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.getMin(root, float("-inf"), float("inf"))

    def getMin(self, root, low, high):
        if not root:
            return (high - low)

        left = self.getMin(root.left, low, root.val)
        right = self.getMin(root.right, root.val, high)
        return min(left, right)
## T = O(n); S = O(h)