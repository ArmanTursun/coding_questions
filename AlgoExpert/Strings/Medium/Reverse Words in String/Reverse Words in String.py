# Medium

# Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has
# these words in reverse order. For example, given the string "tim is great", your function should return "great is tim".
# For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be
# separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original string.
# For example, given the string "whitespaces     4" you would be expected to return "4     whitespaces".

# Note that you're not allowed to use any built-in split or reverse methods/functions. However, you are allowed to use
# a built-in join method/function.
# Also note that the input string insn't guaranteed to always contains words.

def reverseWordsInString(string):
    # Write your code here.
    strings = list(string)
    reverse(strings, 0, len(strings) - 1)
    i = 0
    while i < len(strings):
        if strings[i] != ' ':
            start = i
            end = i
            while end + 1 < len(strings) and strings[end + 1] != ' ':
                end += 1
            reverse(strings, start, end)
            i = end
        i += 1

    return ''.join(strings)

def reverse(word, left, right):
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

## T = O(n); S = O(n)



## If reversed method and split are allowed to be used.
def reverseWordsInString(string):
    # Write your code here.
    strings = string.split(' ')
    return ' '.join(reversed(strings))
