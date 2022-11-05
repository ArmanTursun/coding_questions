# Medium

# Write a function that, given a string, returns its longest palindromic substring.

# A palindrome is defined as a string that's written the same forward and backward. Note that single-character
# strings are palindromes.
# You can assume that there will only be one longest palindromic substring.

# Sample Input
# string = "abaxyzzyxf"

# Sample Output
# "xyzzyx"

def longestPalindromicSubstring(string):
    # Write your code here.
    result = ''
    length = 0
    space = -1
    idx = 0
    while idx < len(string):
        if space == -1:
            left, right = idx - 1, idx + 1
            curLength = 1
        else:
            left, right = idx, idx + 1
            curLength = 0
            idx += 1
        while left > -1 and right < len(string) and string[left] == string[right]:
            curLength += 2
            left -= 1
            right += 1
        if curLength > length:
            length = curLength
            result = string[left + 1 : right]
        space *= -1
    return result
## T = O(n ^ 2); S = O(n)


###################################################
# Manacher's algorithm can do with O(n) and O(n).
# To be UPDATED