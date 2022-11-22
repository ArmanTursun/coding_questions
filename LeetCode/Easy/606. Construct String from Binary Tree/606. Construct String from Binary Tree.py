# Easy

# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the
# preorder traversal way, and return it.
#
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and
# the original binary tree.
#
# Example 1:

# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".

# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        if not root.right and not root.left:
            return str(root.val)
        elif not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        elif not root.left:
            return str(root.val) + '()' + '(' + self.tree2str(root.right) + ')'
        else:
            return str(root.val) + '(' + self.tree2str(root.left) + ')(' + self.tree2str(root.right) + ')'
## T = O(n); S = O(h)