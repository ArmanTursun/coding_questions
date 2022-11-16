# Easy

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Constraints:
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            if self.isEven(nums[i]):
                i += 1
            if not self.isEven(nums[j]):
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def isEven(self, num):
        if num % 2 == 0:
            return True
        else:
            return False
## T = O(n); S = O(1)