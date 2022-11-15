# Easy

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0
        for num in counts:
            if counts[num] == 1:
                result += num
        return result
## T = O(n); S = O(n)