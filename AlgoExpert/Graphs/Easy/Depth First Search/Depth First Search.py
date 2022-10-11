# Easy

# You're given a Node class that has a name and an array of optional children nodes. When put together,
# nodes form an acyclic tree-like structure.

# Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the
# tree using the Depth-first Search approach (specifically navigating the tree from left to right),
# stores all of the nodes' names in the input array, and returns it.

# Sample Input
#   graph =         A
#               /   |   \
#              B    C    D
#            /  \      /  \
#           E    F    G    H
#               /\     \
#              I  J     K

# Sample Output
# [A, B, E, F, I, J, C, D, G, K, H]

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

# T = O(v + e); S = O(v) -- where v is the numver of vertices and e is edges.