# Easy

# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
#
# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2]
# + ... + nums[nums.length-1].
#
# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side
# sum is considered to be 0.
#
# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
#
#
#
# Example 1:
#
# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

# Constraints:
#
# 1 <= nums.length <= 100
# -1000 <= nums[i] <= 1000

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = i - 1
            right = i + 1

            leftSum = 0
            rightSum = 0
            while left >= 0:
                leftSum += nums[left]
                left -= 1
            while right <= len(nums) - 1:
                rightSum += nums[right]
                right += 1

            if leftSum == rightSum:
                return i
        return -1
## T = O(n ^ 2); S = O(1)


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            if leftSum == totalSum - nums[i] - leftSum:
                return i
            leftSum += nums[i]
        return -1
## T = O(n); S = O(1)