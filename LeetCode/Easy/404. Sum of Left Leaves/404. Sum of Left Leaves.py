# Easy

# Given the root of a binary tree, return the sum of all left leaves.
#
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
#
#
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.getSum(root, None)

    def getSum(self, root, prev):
        if not root:
            return 0

        if not root.left and not root.right and prev and root == prev.left:
            return root.val
        elif not root.left and not root.right and prev and root == prev.right:
            return 0
        else:
            return self.getSum(root.left, root) + self.getSum(root.right, root)
## T = O(n); S = O(h)


