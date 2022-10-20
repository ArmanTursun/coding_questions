# Medium
# LC 1650

# You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor
# property pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree
# and the other two inputs are descendants in the ancestral tree.

# Write a function that returns the youngest common ancestor to the two descendants.
# Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, the
# youngest common ancestor to nodes A and B is node A
#   A
#  /
# B

# Sample Input
# topAncestor = node A
# descendantOne = node E
# descendantTwo = node I

#             A
#          /    \
#        B       C
#      /  \    /  \
#     D    E  F    G
#   /  \
#  H    I

# Sample Output
# node B

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    visited = set()

    while descendantOne or descendantTwo:
        if descendantOne and descendantOne in visited:
            return descendantOne
        elif descendantOne:
            visited.add(descendantOne)
            descendantOne = descendantOne.ancestor

        if descendantTwo and descendantTwo in visited:
            return descendantTwo
        elif descendantTwo:
            visited.add(descendantTwo)
            descendantTwo = descendantTwo.ancestor

## T = O(h); S = O(n)


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depthOne = getDepth(descendantOne, topAncestor)
    depthTwo = getDepth(descendantTwo, topAncestor)

    if depthOne > depthTwo:
        return getAncestor(depthOne, descendantOne, depthTwo, descendantTwo)
    else:
        return getAncestor(depthTwo, descendantTwo, depthOne, descendantOne)


def getDepth(node, root):
    depth = 0
    while node != root:
        node = node.ancestor
        depth += 1
    return depth


def getAncestor(lowerDepth, lowerNode, higherDepth, higherNode):
    while lowerDepth > higherDepth:
        lowerDepth -= 1
        lowerNode = lowerNode.ancestor

    while lowerNode != higherNode:
        higherNode = higherNode.ancestor
        lowerNode = lowerNode.ancestor

    return lowerNode

# T = O(n); S = O(1)



######################################
########## Simple Method #############

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    p, q = descendantOne, descendantTwo
    while p != q:
        p = p.ancestor if p.ancestor else descendantTwo
        q = q.ancestor if q.ancestor else descendantOne
    return p

## T = O(n); S = O(1)
