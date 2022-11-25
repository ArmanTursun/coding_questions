# Easy

# Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with
# nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.
#
#
#
# Example 1:
#
# Input: nums = [34,23,1,24,75,33,54,8], k = 60
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.

# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000
# 1 <= k <= 2000

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        maxSum = -1

        while i < j:
            if nums[i] + nums[j] < k and nums[i] + nums[j] > maxSum:
                maxSum = nums[i] + nums[j]
            if nums[i] + nums[j] <= maxSum:
                i += 1
            else:
                j -= 1
        return maxSum
## T = O(nlog(n)); S = O(1)