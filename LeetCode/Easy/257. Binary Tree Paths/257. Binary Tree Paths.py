# Easy

# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
#
#
# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.findAllPath(root, result, [])
        return result

    def findAllPath(self, root, result, curPath):
        if not root.left and not root.right:
            result.append('->'.join(curPath + [str(root.val)]))
            return
        if root.left:
            self.findAllPath(root.left, result, curPath + [str(root.val)])
        if root.right:
            self.findAllPath(root.right, result, curPath + [str(root.val)])
## T = O(n); S = O(n)