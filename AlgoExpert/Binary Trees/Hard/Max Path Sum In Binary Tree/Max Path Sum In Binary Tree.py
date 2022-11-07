# Hard

# Write a function that takes in a Binary Tree and returns its max path sum.

# A path is a collection of connected nodes in a tree, where no nodes is connected to more than two other
# nodes; a path sum is the sum of the values of the nodes in a particular path.

# Sample Input
# tree   =     1
#            /  \
#           2    3
#          / \  / \
#         4  5 6   7

# Sample Output
# 18 (5 + 2 + 1 + 3 + 7)

def maxPathSum(tree):
    # Write your code here.
    _, maxPath = helper(tree)
    return maxPath


def helper(tree):
    if not tree:
        return (0, float("-inf"))

    maxLeftPath, maxLeftSumPath = helper(tree.left)
    maxRightPath, maxRightSumPath = helper(tree.right)

    # larger path between left subtree and right subtree
    maxChildPath = max(maxLeftPath, maxRightPath)

    # the path includes root, include/exclude subtree
    #    -- if max path of subtree is smaller than 0, then only keep root as path
    # this path would return to parent node as branch
    maxSubPath = max(maxChildPath + tree.value, tree.value)

    # the max path that include left-subtree + right-subtree + root
    maxPathWithRoot = maxLeftPath + maxRightPath + tree.value

    # the overall max path will be chosen from two (further divied into four):
    #   -- include root
    #      -- the path from left-subtree to right-subtree, connected by root
    #      -- the path that includes root and one/none of subtrees
    #   -- exclude root
    #      -- max path in left-subtree
    #      -- max path in right-subtree
    maxSubSumPath = max(maxLeftSumPath, maxRightSumPath, maxPathWithRoot, maxSubPath)

    return (maxSubPath, maxSubSumPath)

## T = (n); S = O(log(n))