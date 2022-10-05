# Write a function that takes in two strings and checks if the first string
# contains the second one using the Knuth-Morris-Pratt algorithm. The function
# should return a boolean.

# Sample Input
# string = 'aefoaefcdaefcdaed'
# substring = 'aefcdaed'

# Sample Output
# True

def knuthMorrisPrattAlgorithm(string, substring):
    pattern = buildPattern(substring)
    return doesMatch(string, substring, pattern)


def buildPattern(substring):
    pattern = [-1 for _ in substring]
    i = 1
    j = 0

    while i < len(substring):
        if substring[j] == substring[i]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern


def doesMatch(string, substring, pattern):
    i = 0
    j = 0

    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False


## T = O(m + n); S = O(m) where n is the length of the main string and m is
## the length of the potential substring