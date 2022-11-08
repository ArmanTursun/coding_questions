# Hard

# Write a ContinuousMedianHandler class that supports:
#   - The Continuous insertion of numbers with the insert method.
#   - The instant (O(1) time) retrieval of the median of the numbers that have been inserted thus fat with the
#     getMedian method.

# The getMedian method has already been written for you. You simply have to write the insert method.
# The median of a set of numbers is the "middle" number when the numbers are ordered from smallest to greatest.
# If there's an odd number of numbers in the set, as in {1, 3, 7}, the median is the number in the middle; if
# there's an even number of numbers in the set, as in {1, 3, 7, 8}, the median is the average of the two middle
# numbers ( (3 + 7) / 2 == 5 ).

# Sample Usage
# ContinuousMedianHandler(): -
# insert(5): -
# insert(10): -
# getMedian(): 7.5
# insert(100): -
# getMedian(): 10

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
from heapq import heappush, heappop


class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.minHeap = []
        self.maxHeap = []

    def insert(self, number):
        # Write your code here.
        if not self.minHeap or number > self.minHeap[0]:
            heappush(self.minHeap, number)
        else:
            heappush(self.maxHeap, -number)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            self.keepBalance(self.minHeap, self.maxHeap)
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            self.keepBalance(self.maxHeap, self.minHeap)

        if len(self.minHeap) == len(self.maxHeap):
            self.median = (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]
        else:
            self.median = -self.maxHeap[0]

    def getMedian(self):
        return self.median

    def keepBalance(sefl, large, small):
        while len(large) - len(small) > 1:
            heappush(small, -heappop(large))
