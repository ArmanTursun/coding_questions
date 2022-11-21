# Easy

# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
# Note:
#
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a
# signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same,
# whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input
# represents the signed integer. -3.
#
#
# Example 1:
#
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Constraints:
#
# The input must be a binary string of length 32.

class Solution:
    def hammingWeight(self, n: int) -> int:
        compare = 1
        count = 0

        for i in range(32):
            if n & compare == 1:
                count += 1
            n = n >> 1
        return count
 ## T = O(1); S = O(1); O(32) = O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            result += 1
            n &= (n - 1)
        return result
 ## T = O(1); S = O(1)



 ## Follow up: If this function is called many times, how would you optimize it?

class Solution:
    def hammingWeight(self, n: int) -> int:
        lookUpSize = 1 << 8
        lookUpTable = [0 for i in range(lookUpSize)]

        lookUpTable[0] = 0
        for i in range(lookUpSize):
            lookUpTable[i] = lookUpTable[i >> 1] + (i & 1)
        print(lookUpTable)

        count = lookUpTable[n & 255] + lookUpTable[(n >> 8) & 255] + lookUpTable[(n >> 16) & 255] + lookUpTable[
            (n >> 24) & 255]
        return count
