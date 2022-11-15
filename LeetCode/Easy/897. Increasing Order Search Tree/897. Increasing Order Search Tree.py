# Easy

# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is
# now the root of the tree, and every node has no left child and only one right child.

# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

# Constraints:
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = [root]
        prev = None
        newRoot = None

        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur)
                stack.append(cur.left)
                cur.left = None
                continue
            if not prev:
                newRoot = cur
                prev = cur
            else:
                prev.right = cur
                prev = cur
            if cur.right:
                stack.append(cur.right)
                cur.right = None
        return newRoot
## T = O(n); S = O(n)