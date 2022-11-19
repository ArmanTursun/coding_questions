# Easy

# Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
# If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
#
# Example 1:
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Constraints:
#
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []

        for num in counts:
            result.append([num, counts[num]])

        result.sort(key=lambda x: (x[1], -x[0]))
        ans = []

        for item in result:
            while item[1] > 0:
                ans.append(item[0])
                item[1] -= 1
        return ans
## T = O(nlog(n)); S = O(n)


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return sorted(nums, key = lambda x : (counts[x], -x))