# Medium

# You're given a Node class that has a name and ran array of optional children nodes.
# When you put together, nodes from an acyclic tree-like structure.

# Implement the breadthFirstSearch method on the Node class, which takes in an empty array,
# traverses the tree using the BFS approach, stores all of the nodes' names in the input array,
# and returns it.

# Sample Input
# graph      =        A
#                 /   |   \
#                B    C    D
#              /  \       / \
#             E   F      G   H
#                / \      \
#               I   J      K

# Sample Output
# [A, B, C, D, E, F, G, H, I, J, K]

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        q = deque()
        q.append(self)
        while q:
            cur = q.popleft()
            array.append(cur.name)
            for child in cur.children:
                q.append(child)
        return array

## T = O(v + e); S = O(v)
