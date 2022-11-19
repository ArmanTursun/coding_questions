# Easy

# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.
#
# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.insert(nums, 0, len(nums) - 1)

    def insert(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        return TreeNode(nums[mid], self.insert(nums, left, mid - 1), self.insert(nums, mid + 1, right))
# T = O(n); S = O(log(n))