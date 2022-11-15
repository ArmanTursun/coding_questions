# Easy

# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the
# integers that appeared in all three arrays.

# Example 1:
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.

# Constraints:
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000

## Three pointers
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        result = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                if arr1[i] < arr2[j]:
                    i += 1
                elif arr2[j] < arr3[k]:
                    j += 1
                else:
                    k += 1
        return result
## T = O(n); S = O(1) where n is the total number in all arrays.


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hp = []
        arrs = {1: arr1, 2: arr2, 3: arr3}
        heappush(hp, (arr1[0], 0, 1))
        heappush(hp, (arr2[0], 0, 2))
        heappush(hp, (arr3[0], 0, 3))
        result = []
        while len(hp) == 3:
            curNum = hp[0][0]
            count = 0
            while hp and hp[0][0] == curNum: ## don't forget to check whether hp is empty
                _, idx, arr = heappop(hp)
                count += 1
                if idx + 1 < len(arrs[arr]):
                    heappush(hp, (arrs[arr][idx + 1], idx + 1, arr))
            if count == 3:
                result.append(curNum)
        return result
## T = O(n); S = O(1)