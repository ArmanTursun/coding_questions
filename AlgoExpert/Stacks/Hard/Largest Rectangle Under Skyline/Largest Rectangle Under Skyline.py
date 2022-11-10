# Hard

# Write a function that takes in an array of positive integers representing the heights of adjacent buildings
# and returns the area of the largest rectangle that can be created by any number of adjacent buildings, including
# just one building. Note that all buildings have the same width of 1 unit.

# For example, given buildings = [2, 1, 2], the area of the largest rectangle that can be created is 3, using all
# three buildings is 1, you can create a rectangle that has a height of 1 and a width of 3. You could also create
# rectangles of area 2 by using only the first building or the last building, but these clearly wouldn't be the
# largest rectangles. Similarly, you could create rectangles of area 2 by using the first and second buliding
# or the second and third building.

# To clarify, the width of a created rectangle is the number of buildings used to create the rectangle, and its
# height is the height of the smallest building used to create it.

# Note that if no rectangles can be created, your function should return 0.

# Sample Input
# buildinsg = [1, 3, 3, 2, 4, 1, 5, 3, 2]
#             _
#         _  | |
#   _ _  | | | |_
#  | | |_| | | | |_
# _| | | | |_|_| | |
#|_|_| |_|_|_|_|_|_|

## Brute Force
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    maxRec = 0

    for i, building in enumerate(buildings):
        left = i - 1
        right = i + 1
        curRec = building
        while left > -1 and buildings[left] >= building:
            curRec += building
            left -= 1
        while right < len(buildings) and buildings[right] >= building:
            curRec += building
            right += 1
        maxRec = max(maxRec, curRec)

    return maxRec
## T = O(n ^ 2); S = O(1)


## Divide and conquer
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    return helper(buildings, 0, len(buildings) - 1)

def helper(buildings, left, right):
    if left > right:
        return 0

    minHeight = buildings[left]
    minIdx = left
    for i in range(left, right + 1):
        if minHeight > buildings[i]:
            minIdx = i
            minHeight = buildings[i]

    curRec = minHeight * (right - left + 1)
    leftMin = helper(buildings, left, minIdx - 1)
    rightMin = helper(buildings, minIdx + 1, right)

    return max(curRec, leftMin, rightMin)
## Average/Best: T = O(nlog(n)); S = (n)
## Worst: T = O(n ^ 2); S = (n) when buildings are sorted.
## Time complexity can be reduced to O(nlog(n)) using segment tree
## To be Updated!


## Use stack
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    stack = []
    maxRec = 0
    buildings.append(0)
    for i in range(len(buildings)):
        while stack and buildings[stack[-1]] >= buildings[i]:
            height = buildings[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            curRec = width * height
            maxRec = max(curRec, maxRec)
        stack.append(i)
    return maxRec
## T = O(n); S = O(n)