# Easy

# A tandem bicyble is a bicycle that's operated by two people. THe person that pedals faster dictates the
# speed of the bicycle. You're given tow lists of positive integers: each contains the speeds of riders on
# that team. Write a function that returns the maximum possible total speed if fastest = true, otherwise
# return the minimum total speed.

# Sample Input
# redShirtSpeeds = [5, 5, 3, 9, 2]
# blueShirtSpeeds = [3, 6, 7, 2, 1]
# fastest = True

# Sample Output
# 32

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    i = j = 0
    Sum = 0

    if fastest:
        redShirtSpeeds.sort(reverse = True)
        blueShirtSpeeds.sort(reverse = True)
        while i + j < len(redShirtSpeeds):
            Sum += max(redShirtSpeeds[i], blueShirtSpeeds[j])
            if redShirtSpeeds[i] >= blueShirtSpeeds[j]:
                i += 1
            else:
                j += 1
        return Sum
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        while i < len(redShirtSpeeds):
            Sum += max(redShirtSpeeds[i], blueShirtSpeeds[i])
            i += 1
        return Sum

# T = O(nlog(n)); S = O(1)

