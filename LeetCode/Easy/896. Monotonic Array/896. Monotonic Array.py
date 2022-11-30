# Easy

# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing
# if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,3]
# Output: true

# Constraints:
#
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] <= nums[-1]:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
        else:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
        return True
## T = O(n); S = O(1)