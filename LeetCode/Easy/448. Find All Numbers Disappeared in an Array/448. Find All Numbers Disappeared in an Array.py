# Easy

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
# range [1, n] that do not appear in nums.
#
#
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Constraints:
#
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        temp = [0 for _ in range(len(nums) + 1)]

        for num in nums:
            temp[num] = num

        for i, num in enumerate(temp):
            if i != num:
                result.append(i)
        return result
## T = O(n); S = O(n)


# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count
# as extra space.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)
        return result
## T = O(n); S = O(1)