# Easy

# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray
# of arr and reverse it. You are allowed to make any number of steps.
# Return true if you can make arr equal to target or false otherwise.

# Example 1:
# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true
# Explanation: You can follow the next steps to convert arr to target:
# 1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
# 2- Reverse subarray [4,2], arr becomes [1,2,4,3]
# 3- Reverse subarray [4,3], arr becomes [1,2,3,4]
# There are multiple ways to convert arr to target, this is not the only way to do so.

# Constraints:
# target.length == arr.length
# 1 <= target.length <= 1000
# 1 <= target[i] <= 1000
# 1 <= arr[i] <= 1000

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
## T = O(n); S = O(n)