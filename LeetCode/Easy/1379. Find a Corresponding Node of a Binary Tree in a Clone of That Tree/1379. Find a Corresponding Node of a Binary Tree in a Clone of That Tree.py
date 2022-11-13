# Easy

# Given two binary trees original and cloned and given a reference to a node target in the original tree.
# The cloned tree is a copy of the original tree.
# Return a reference to the same node in the cloned tree.
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to
# a node in the cloned tree.

# Example 1:
# Input: tree = [7,4,3,null,null,6,19], target = 3
# Output: 3
# Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original
# tree. The answer is the yellow node from the cloned tree.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# The values of the nodes of the tree are unique.
# target node is a node from the original tree and is not null.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned:
            return None

        if cloned.val == target.val:
            return cloned

        left = self.getTargetCopy(original, cloned.left, target)
        if left:
            return left
        else:
            return self.getTargetCopy(original, cloned.right, target)


# Follow up: Could you solve the problem if repeated values on the tree are allowed?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None

        if original == target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        else:
            return self.getTargetCopy(original.right, cloned.right, target)