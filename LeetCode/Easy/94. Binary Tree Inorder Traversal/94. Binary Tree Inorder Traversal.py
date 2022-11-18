# Easy

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result
    def inorder(self, root, result):
        if not root:
            return
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
## T = O(n); S = O(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        result = []
        while cur:
            if not cur.left:
                result.append(cur.val)
                cur = cur.right
            else:
                rightMost = self.findRightMost(cur.left)
                rightMost.right = cur
                temp = cur
                cur = cur.left
                temp.left = None

        return result

    def findRightMost(self, root):
        while root.right:
            root = root.right
        return root
## T = O(n); S = O(1) if we don't count the result array.