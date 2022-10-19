# Medium

# Write a function that takes in a non-empty sorted arrayof distinct integers, and returns the root
# of the BST. The function should minimize the height of the BST.

# Sample Input
# array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

# Sample Output
#              10
#          /        \
#         2          14
#       /  \       /   \
#      1    5     13    15
#            \           \
#             7           22

## Using Insert method and recersion
def minHeightBst(array):
    left = 0
    right = len(array) - 1

    mid = (left + right) // 2
    root = BST(array[mid])
    construct(root, array, left, mid - 1)
    construct(root, array, mid + 1, right)
    return root

def construct(root, array, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    root.insert(array[mid])
    construct(root, array, left, mid - 1)
    construct(root, array, mid + 1, right)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

## T = O(nlog(n)); S = O(n)

## Using insert method with iteration
from collections import deque
def minHeightBst(array):
    q = deque()

    left = 0
    right = len(array) - 1
    mid = (left + right) // 2

    q.append((left, mid - 1))
    q.append((mid + 1, right))

    root = BST(array[mid])

    while q:
        left, right = q.popleft()
        if left > right:
            continue

        mid = (left + right) // 2
        root.insert(array[mid])
        q.append((left, mid - 1))
        q.append((mid + 1, right))

    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

## T = O(nlog(n)); S = O(n)


## Not using insert method with recursion
def minHeightBst(array):
    left = 0
    right = len(array) - 1

    return construct(array, left, right)

def construct(array, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    root = BST(array[mid])
    root.left = construct(array, left, mid - 1)
    root.right = construct(array, mid + 1, right)
    return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

## T = O(n); S = O(n)

