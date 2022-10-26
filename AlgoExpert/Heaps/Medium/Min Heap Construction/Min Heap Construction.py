# Medium

# Implement a MinHeap class that supports:
#   -- Building a Min Heap from an input array of integers.
#   -- Inserting integers in the heap.
#   -- Removing the heap's minimum/root value.
#   -- Peeking at the heap's minimum/root value.
#   -- Sifting integers up and down the heap, which is to be used when inserting and removing values.

# Note that the heap should represented in the form of an array.

# Sample Usage
# array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
# Minheap(array): - // instantiate a Minheap (calls the buildHeap method and populates the heap)
# buildHeap(array): - // [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
# insert(76): - // [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
# peek(): -5
# remove(): -5 // [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
# peek(): 2
# remove(): 2 // [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
# peek(): 6
# insert(87): - // [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    ## T = O(n); S = O(1)
    def buildHeap(self, array):
        # Write your code here.
        startIdx = len(array) // 2 - 1
        for i in range(startIdx, -1, -1):
            self.siftDown(i, array)
        return array

    ## T = O(log(n)); S = O(1)
    def siftDown(self, idx, heap):
        # Write your code here.
        while idx < len(heap):
            minRoot = idx
            leftIdx = 2 * idx + 1
            rightIdx = 2 * idx + 2
            if leftIdx < len(heap) and heap[idx] > heap[leftIdx]:
                minRoot = leftIdx
            if rightIdx < len(heap) and heap[minRoot] > heap[rightIdx]:
                minRoot = rightIdx
            if minRoot != idx:
                heap[minRoot], heap[idx] = heap[idx], heap[minRoot]
                idx = minRoot
            else:
                break

    ## T = O(log(n)); S = O(1)
    def siftUp(self, idx):
        # Write your code here.
        while (idx - 1) // 2 >= 0:
            parentIdx = (idx - 1) // 2
            if self.heap[parentIdx] > self.heap[idx]:
                self.heap[parentIdx], self.heap[idx] = self.heap[idx], self.heap[parentIdx]
                idx = parentIdx
            else:
                break

    ## T = O(1); S = O(1)
    def peek(self):
        # Write your code here.
        return self.heap[0]

    ## T = O(log(n)); S = O(1)
    def remove(self):
        # Write your code here.
        self.heap[len(self.heap) - 1], self.heap[0] = self.heap[0], self.heap[len(self.heap) - 1]
        minValue = self.heap.pop()
        self.siftDown(0, self.heap)
        return minValue

    ## T = O(log(n)); S = O(1)
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

