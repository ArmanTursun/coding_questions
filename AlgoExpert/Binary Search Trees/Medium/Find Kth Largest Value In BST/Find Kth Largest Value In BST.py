# Medium
## LC 230

# Write a function that takes in a BST and a positive integer k and returns the kth largest
# integer contained in the BST.

# You can assume that there will only be integer values in the BST and that k is less than or
# equal to the number to the number of nodes in the tree.

# Also, for the purpose of this question, duplicate integers will be treated as distinct values.
# In other words, the second largest value in a BST containing values {5, 7, 7} will be 7.

# Sample Input
#              10
#          /        \
#         2          14
#       /  \       /   \
#      1    5     13    15
#            \           \
#             7           22
# k = 3

# Sample Output
# 14

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []
    reversedInorder(tree, array, k)
    print (array)
    return array[k-1]

def reversedInorder(tree, array, k):
    if tree.right:
        reversedInorder(tree.right, array, k)
    array.append(tree.value)
    if tree.left:
        reversedInorder(tree.left, array, k)

## T = O(n); S = O(n)


#######################################
############# Method 2 ################
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class count:
    def __init__(self):
        self.count = 0


def findKthLargestValueInBst(tree, k):
    cnt = count()
    return findKth(tree, k, cnt)


def findKth(tree, k, count):
    # Write your code here.
    if tree.right:
        kth = findKth(tree.right, k, count)
        if kth is not None:
            return kth
    count.count += 1
    if count.count == k:
        return tree.value
    if tree.left:
        kth = findKth(tree.left, k, count)
        if kth is not None:
            return kth
    return None

## T = O(h + k); S = O(h) where h is the depth of the tree.




# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class KthInfo:
    def __init__(self, count, node):
        self.count = count
        self.node = node

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    kthinfo = KthInfo(0, -1)
    reversedInorder(tree, k, kthinfo)
    return kthinfo.node

def reversedInorder(tree, k, kthinfo):
    if not tree or kthinfo.count >= k:
        return

    reversedInorder(tree.right, k, kthinfo)
    if kthinfo.count < k:
        kthinfo.count += 1
        kthinfo.node = tree.value
        reversedInorder(tree.left, k, kthinfo)

## T = O(k + h); S = (h)


### Iteration method

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    stack = []

    while True:
        while tree:
            stack.append(tree)
            tree = tree.right

        tree = stack.pop()
        k -= 1
        if k == 0:
            return tree.value
        tree = tree.left

## T = O(h + k); S = O(h)



