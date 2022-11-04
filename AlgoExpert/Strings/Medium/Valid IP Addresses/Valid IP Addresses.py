# Medium

# You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible IP
# addresses that can be vreated by inserting three '.' in the string.

# An IP isn't valid if any of the individual integers contains leading 0s.
# Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can
# be created from the string, your function should return an empty list.

# Sample Input
# string = "1921680"

# Sample Output
# [
#  "1.9.216.80",
#  "1.92.16.80",
#  "1.92.168.0",
#  "19.2.16.80",
#  "19.2.168.0",
#  "19.21.6.80",
#  "19.21.68.0",
#  "19.216.8.0",
#  "192.1.6.80",
#  "192.1.68.0",
#  "192.16.8.0" ]

def validIPAddresses(string):
    # Write your code here.
    result = []
    validHelper(string, result, 0, '')
    return result

def validHelper(string, result, numberOfDots, ip):
    if numberOfDots == 3:
        if isValid(string):
            result.append(ip + string)
        return
    for i in range(1, len(string)):
        subString = string[:i]
        if isValid(subString):
            validHelper(string[i:], result, numberOfDots + 1, ip + subString + '.')

def isValid(string):
    if len(string) == 1:
        return True
    elif string[0] != '0' and int(string) <= 255:
        return True
    else:
        return False

## T = O(1); S = O(1) because at most there are 2^32 possibilities of ip addresses and it's
## constant. It does not depend on the input.


def validIPAddresses(string):
    # Write your code here.
    result = []
    for i in range(1, 4):
        firstPart = string[:i]
        if not isValid(firstPart):
            continue

        for j in range(i + 1, i + 4):
            secondPart = string[i:j]
            if not isValid(secondPart):
                continue

            for k in range(j + 1, j + 4):
                thirdPart = string[j:k]
                fourthPart = string[k:]
                if isValid(thirdPart) and isValid(fourthPart):
                    result.append('.'.join([firstPart, secondPart, thirdPart, fourthPart]))
    return result

def isValid(string):
    if not string:
        return False
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt))
