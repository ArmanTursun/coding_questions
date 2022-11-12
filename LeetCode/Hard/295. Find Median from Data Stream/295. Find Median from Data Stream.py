# Hard

# The median is the middle value in an ordered integer list. If the size of the list is even,
# there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
#
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Follow up
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

## Min/Max Heap
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = None

    ## T = O(log(n)); S = O(n)
    def addNum(self, num: int) -> None:
        if not self.minHeap or num > self.minHeap[0]:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            self.keepBalance(self.minHeap, self.maxHeap)
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            self.keepBalance(self.maxHeap, self.minHeap)

    ## T = O(1); S = O(1)
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            self.median = (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]
        else:
            self.median = -self.maxHeap[0]

        return self.median

    def keepBalance(self, bigHeap, smallHeap):
        while len(bigHeap) - len(smallHeap) > 1:
            heappush(smallHeap, -heappop(bigHeap))

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()