# Medium

# Write three functions that take in a BST and an empty array, traverse the BST, add its nodes' values
# to the input array, and return that array. The three functions should traverse the BST using the
# in-order, pre-order, and post-order tree-traversal techniques, respectively.

def inOrderTraverse(tree, array):
    # Write your code here.
    if not tree:
        return array
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    if not tree:
        return array
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    if not tree:
        return array

    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array

## T = O(n); S = O(n) space complexity is O(n) because we count in the result.