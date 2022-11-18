# Easy

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
# in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
## T = O(nlog(n)); S = O(nlog(n))



class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        idx = 0
        absMin = abs(nums[0])
        idxMin = 0
        while idx < len(nums):
            if abs(nums[idx]) < absMin:
                absMin = abs(nums[idx])
                idxMin = idx
            idx += 1
        result = [nums[idxMin] ** 2]
        left, right = idxMin - 1, idxMin + 1

        while left > -1 and right < len(nums):
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[right] ** 2)
                right += 1
            else:
                result.append(nums[left] ** 2)
                left -= 1
        if left > -1:
            while left > -1:
                result.append(nums[left] ** 2)
                left -= 1
        if right < len(nums):
            while right < len(nums):
                result.append(nums[right] ** 2)
                right += 1
        return result
## T = O(n); S = O(n)



class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for _ in nums]

        left, right = 0, len(nums) - 1
        for i in range(len(result) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result
## T = O(n); S = O(n)