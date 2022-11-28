# Easy

# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than
# 25% of the time, return that integer.
#
#
#
# Example 1:
#
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

# Constraints:
#
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = Counter(arr)

        for num in counts:
            if counts[num] > 0.25 * len(arr):
                return num
## T = O(n);  S = O(n)


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = len(arr) / 4
        curCounts = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                curCounts += 1
            elif curCounts > counts:
                return arr[i - 1]
            else:
                curCounts = 1
        if curCounts > counts:
            return arr[-1]
## T = O(n); S = O(1)


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = len(arr) // 4

        for i in range(len(arr) - counts):
            if arr[i] == arr[i + counts]:
                return arr[i]
## T = O(3n/4); S = O(1)


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if self.findIdx(arr, len(arr) // 4):
            return arr[len(arr) // 4]
        elif self.findIdx(arr, len(arr) // 2):
            return arr[len(arr) // 2]
        else:
            return arr[3 * len(arr) // 4]

    def findIdx(self, arr, idx):
        curValue = arr[idx]
        lowBound = self.findLow(arr, idx - len(arr) // 4, idx - 1, curValue)
        highBound = self.findHigh(arr, idx + 1, idx + len(arr) // 4, curValue)

        if highBound - lowBound + 1 > len(arr) // 4:
            return True
        else:
            return False

    def findLow(self, arr, left, right, curValue):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == curValue:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findHigh(self, arr, left, right, curValue):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == curValue:
                left = mid + 1
            else:
                right = mid - 1
        return right
## T = O(4log(n)); S = O(1)


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if self.findIdx(arr, len(arr) // 4):
            return arr[len(arr) // 4]
        elif self.findIdx(arr, len(arr) // 2):
            return arr[len(arr) // 2]
        else:
            return arr[3 * len(arr) // 4]

    def findIdx(self, arr, idx):
        curValue = arr[idx]
        lowBound = self.findLow(arr, idx - len(arr) // 4, idx - 1, curValue)
        if arr[lowBound + len(arr) // 4] == curValue:
            return True
        else:
            return False
    def findLow(self, arr, left, right, curValue):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == curValue:
                right = mid - 1
            else:
                left = mid + 1
        return left
## T = O(2log(n)); S = O(1)