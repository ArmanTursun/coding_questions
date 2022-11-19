# Easy

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
# unique and you may return the result in any order.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Constraints:
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()
        for num in nums2:
            if num in set1:
                result.add(num)
        return list(result)
# T = O(n + m); S = O(n + m)