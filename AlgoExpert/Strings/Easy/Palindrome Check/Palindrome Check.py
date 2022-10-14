# Easy

# Write a function that takes in a non-empty string and that returns a boolean representing
# whether the string is a palindrome.

# Sample Input
# string = 'abcdcba'

# Sample Output
# True

def isPalindrome(string):
    # Write your code here.
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True
