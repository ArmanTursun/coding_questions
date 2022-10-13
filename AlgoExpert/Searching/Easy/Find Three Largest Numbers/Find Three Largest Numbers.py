# Easy

# Write a function that takes in an array of at least three integers and, without sorting the input
# array, returns a sorted array of the three largest integers in the input array.
# The function should return duplicate integers if necessary; for example, it should return
# [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

# Sample Input
# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

# Sample Output
# [18, 141, 541]

def findThreeLargestNumbers(array):
    # Write your code here.
    result = []
    full = False

    for i, item in enumerate(array):
        if full and item <= result[0]:
            continue

        if not full:
            result.append(item)
            i = len(result) - 1
            while i > 0 and result[i] <= result[i - 1]:
                result[i], result[i - 1] = result[i - 1], result[i]
                i -= 1
            result[i] = item
            if len(result) == 3:
                # print(result)
                full = True
        else:
            i = 0
            while i < 2:
                if item <= result[i + 1]:
                    break
                i += 1
            j = 0
            while j < i:
                result[j] = result[j + 1]
                j += 1
            result[i] = item
        print(result)

    return result


# More clear version
def findThreeLargestNumbers(array):
    # Write your code here.
    result = [None, None, None]
    for num in array:
        update(result, num)
    return result

def update(result, num):
    if not result[2] or num > result[2]:
        shift(result, num, 2)
    elif not result[1] or num > result[1]:
        shift(result, num, 1)
    elif not result[0] or num > result[0]:
        shift(result, num, 0)

def shift(result, num, idx):
    for i in range(idx):
        result[i] = result[i + 1]
    result[idx] = num

## T = O(n); S = O(1)