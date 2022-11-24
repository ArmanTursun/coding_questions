# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                j = i
                while nums[j - 1] == 0 and j - 1 >= 0:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1
## T = O(n ^ 2); S = O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mostLeftZero = 0
        for i in range(len(nums)):
            if nums[mostLeftZero] == 0 and nums[i] != 0:
                nums[mostLeftZero], nums[i] = nums[i], nums[mostLeftZero]
            if nums[mostLeftZero] != 0:
                mostLeftZero += 1
        return nums
## T = O(n); S = O(1)
