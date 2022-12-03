# Easy

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curMax = 0
        overallMax = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curMax += 1
                if curMax > overallMax:
                    overallMax = curMax
            else:
                curMax = 0
        return overallMax
## T = O(n); S = O(1)