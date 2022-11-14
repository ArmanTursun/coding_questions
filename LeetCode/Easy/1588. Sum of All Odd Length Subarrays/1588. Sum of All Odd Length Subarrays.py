# Easy

# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.

# Example 1:
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

# Constraints:
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subLength = 3
        resultSum = sum(arr)

        while subLength <= len(arr):
            for i in range(len(arr) - subLength + 1):
                for j in range(i, i + subLength):
                    resultSum += arr[j]
            subLength += 2
        return resultSum
## T = O(n ^ 3); S = O(1)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subLength = 3
        resultSum = sum(arr)

        while subLength <= len(arr):
            prev = sum(arr[:subLength])
            resultSum += prev
            for i in range(1, len(arr) - subLength + 1):
                cur = prev - arr[i - 1] + arr[i + subLength - 1]
                resultSum += cur
                prev = cur
            subLength += 2
        return resultSum
## T = O(n^2); S = O(n)


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subLength = 1
        resultSum = 0
        first = 0

        while subLength <= len(arr):
            first += arr[subLength - 2] if subLength > 1 else 0
            first += arr[subLength - 1]
            resultSum += first
            prev = first
            for i in range(1, len(arr) - subLength + 1):
                cur = prev - arr[i - 1] + arr[i + subLength - 1]
                resultSum += cur
                prev = cur
            subLength += 2
        return resultSum
## T = O(n^2); S = O(1)


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        resultSum = 0
        for i in range(len(arr)):
            curNum = 0
            for j in range(i, len(arr)):
                curNum += arr[j]
                resultSum += curNum if (j - i + 1) % 2 == 1 else 0
        return resultSum
## T = O(n^2); S = O(1)


# Follow up:
# Could you solve this problem in O(n) time complexity?

## https://leetcode.com/problems/sum-of-all-odd-length-subarrays/solutions/2773805/sum-of-all-odd-length-subarrays/
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0

        for i, a in enumerate(arr):
            left, right = i, n - i - 1
            answer += a * (left // 2 + 1) * (right // 2 + 1)
            answer += a * ((left + 1) // 2) * ((right + 1) // 2)
        return answer
## T = O(n); S = O(1)