# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true

# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
## T = O(nlog(n)); S = O(1)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)

        for num in counts:
            if counts[num] > 1:
                return True
        return False
## T = O(n); S = O(n)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
## T = O(n); S = O(n)