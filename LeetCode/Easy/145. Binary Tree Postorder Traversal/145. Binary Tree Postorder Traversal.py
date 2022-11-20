# Easy

# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
#
#
# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Constraints:
#
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postOrder(root, result)
        return result

    def postOrder(self, root, result):
        if not root:
            return
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.val)
## T = O(n); S = O(h)




# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [(root, False)]
        result = []

        while stack:
            curNode, flag = stack.pop()
            if not curNode.left and not curNode.right or flag:
                result.append(curNode.val)
            else:
                stack.append((curNode, True))
                if curNode.right:
                    stack.append((curNode.right, False))
                if curNode.left:
                    stack.append((curNode.left, False))
        return result