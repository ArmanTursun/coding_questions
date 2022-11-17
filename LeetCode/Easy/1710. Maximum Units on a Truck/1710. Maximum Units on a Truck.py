# Easy

# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
# where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.

# Example 1:
# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of the third type.
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

# Constraints:
# 1 <= boxTypes.length <= 1000
# 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
# 1 <= truckSize <= 10^6

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda x : x[1])
        #boxTypes.sort(reverse = True, key = operator.itemgetter(1))
        print (boxTypes)
        maximumUnits = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            if truckSize >= boxTypes[i][0]:
                maximumUnits += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                maximumUnits += boxTypes[i][1] * truckSize
                truckSize = 0
            i += 1
        return maximumUnits
## T = O(nlogn); S = O(1)


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = [0 for i in range(1001)]
        maximumUnits = 0

        for i in range(len(boxTypes)):
            boxes[boxTypes[i][1]] += boxTypes[i][0]

        for i in range(len(boxes) - 1, -1, -1):
            if boxes[i] > 0:
                if truckSize >= boxes[i]:
                    maximumUnits += boxes[i] * i
                    truckSize -= boxes[i]
                else:
                    maximumUnits += truckSize * i
                    break
        return maximumUnits
## T = O(1000); S = O(1000) because of the constraints, there are at most 1000 types of box.