# Medium

# Given a non-empty array of integers representing the pre-order traversal of a BST, write a function
# that creates the relevant BST and returns its root node.

# The Input array will contain the values of BST nodes in the order in which these nodes would be visited
# with a pre-order traversal.

# Sample Input
# preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]

# Sample Output
#              10
#            /    \
#           4      17
#         /  \      \
#        2    5      19
#       /           /
#      1          18

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    return construct(None, preOrderTraversalValues, 0, len(preOrderTraversalValues) - 1)


def construct(root, array, left, right):
    if root is None:
        root = BST(array[left])

    left_idx = left
    right_idx = right + 1
    for i in range(left + 1, right + 1):
        if array[i] < root.value:
            left_idx = i
            break
    for j in range(left + 1, right + 1):
        if array[j] >= root.value:
            right_idx = j
            break
    if left_idx > left:
        root.left = construct(root.left, array, left_idx, right_idx - 1)
    if right_idx < right + 1:
        root.right = construct(root.right, array, right_idx, right)
    return root
## T = O(n^2); S = O(n)


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    return construct(preOrderTraversalValues, 0, len(preOrderTraversalValues))


def construct(array, left, right):
    if right <= left:
        return None

    cur_value = array[left]
    right_idx = right

    for idx in range(left + 1, right):
        value = array[idx]
        if value >= cur_value:
            right_idx = idx
            break

    leftSubtree = construct(array, left + 1, right_idx)
    rightSubtree = construct(array, right_idx, right)
    return BST(cur_value, leftSubtree, rightSubtree)
## T = (n^2); S = O(n)




# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Idx:
    def __init__(self):
        self.idx = 0


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    cur_idx = Idx()
    return construct(preOrderTraversalValues, float("-inf"), float("inf"), cur_idx)


def construct(array, low, high, cur_idx):
    if cur_idx.idx == len(array):
        return None

    cur_value = array[cur_idx.idx]
    if cur_value < low or cur_value >= high:
        return None
    cur_idx.idx += 1
    leftSubtree = construct(array, low, cur_value, cur_idx)
    rightSubtree = construct(array, cur_value, high, cur_idx)
    return BST(cur_value, leftSubtree, rightSubtree)
## T = O(n); S = O(n)