# Medium

# Given an array of buildings and a direction that all of the buildings face, return an array of the indices of the
# buildings that can see the sunset.

# A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction
# that is faces. The input array named buildings contains positive, non-zero integers representing the heights of
# the buildings. A building at index i thus has a height denoted by buildings[i]. All of the buildings face the same
# direction, and this direction is either east or west, denoted by the input string named direction, which will always
# be equal to either "EAST" or "WEST". In relation to the input array, you can interpret these directions as right
# for east and left for west.

# Important Note: the indices in the output array should be sorted in ascending order.

# Sample Iput
# Buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# Below is a visual representation of the sample input.
#     _
#    | |_ _
#   _| | | |_   _
#  | | | | | | | |_
#  | | | | | |_| | |
#  |_| |_|_|_|_|_|_|

# direction = "EAST"
# Sample Out
# [1, 3, 6, 7]

# direction = "WEST"
# Sample Out
# [0, 1]

def sunsetViews(buildings, direction):
    # Write your code here.
    start, end, step = 0, len(buildings), 1
    if direction == "EAST":
        start, end, step = len(buildings) - 1, -1, -1

    cur_highest = -1
    result = []
    for i in range(start, end, step):
        if buildings[i] > cur_highest:
            result.append(i)
            cur_highest = buildings[i]
    if direction == "EAST":
        result.reverse()
    return result

## Use stack
def sunsetViews(buildings, direction):
    # Write your code here.
    start, end, step = 0, len(buildings), 1
    if direction == "WEST":
        start, end, step = len(buildings) - 1, -1, -1

    buildingStack = []
    for i in range(start, end, step):
        while buildingStack and buildings[buildingStack[-1]] <= buildings[i]:
            buildingStack.pop()
        buildingStack.append(i)

    return  buildingStack[::-1] if direction == "WEST" else  buildingStack

## T = O(n); S = O(n)
