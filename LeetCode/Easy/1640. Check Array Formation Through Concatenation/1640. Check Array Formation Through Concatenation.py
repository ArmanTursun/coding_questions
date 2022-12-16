# Easy

# You are given an array of distinct integers arr and an array of integer arrays pieces, where the
# integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in
# any order. However, you are not allowed to reorder the integers in each array pieces[i].
#
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: arr = [15,88], pieces = [[88],[15]]
# Output: true
# Explanation: Concatenate [15] then [88]

# Constraints:
#
# 1 <= pieces.length <= arr.length <= 100
# sum(pieces[i].length) == arr.length
# 1 <= pieces[i].length <= arr.length
# 1 <= arr[i], pieces[i][j] <= 100
# The integers in arr are distinct.
# The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in
# this array are distinct).

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hashmap = {}
        for item in pieces:
            hashmap[item[0]] = item

        i = 0
        while i < len(arr):
            num = arr[i]
            if num not in hashmap:
                return False
            curSubarray = hashmap[num]

            j = 0
            while i < len(arr) and j < len(curSubarray):
                if arr[i] != curSubarray[j]:
                    return False
                i += 1
                j += 1
            if j != len(curSubarray):
                return False
        return True
## T = O(n);  S = O(n)