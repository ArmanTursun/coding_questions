# Medium

# Write a DoublyLinkedList class that has a head and a tail, both of which point to either a linked list Node
# or None / null. THe class should support:
#   - Setting the head and tail of the linked list.
#   - Inserting nodes before and after other nodes as well as at given positions.
#   - Removing given nodes and removing nodes with given values.
#   - Searching for nodes with given values.

# Note that the setHead, setTail, inserBefore, insertAfter, insertAtPosition, and remove methods all take in
# actual Nodes as input parameters - not integers (except for insertAtPosition, which also takes in an integer
# # representing the position); this means that you don't need to create any new Nodes in these methods. The
# input nodes can be either stand-alone nodes or nodes that are already in the linked list. If they're ndoes
# that are already in the linked list, the methods will effectively be moving the nodes within the linked list.
# You won't be told if the input nodes are already in the linked list, so your code will have to defensively
# handle this scenario.

# Sample Usage
# Assume the following linked list has already been created
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# Assume that we also have the following stand-alone nodes.
# 3, 3, 6
# setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5
# setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6
# insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6  // move existing node 3
# inserAfter(6, 3): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 3 <-> 6 <-> 3  // insert new node 3
# insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 3 <-> 6 <-> 3 // insert new node 3
# removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6
# remove(2): 4 <-> 1 <-> 5 <-> 6
# containsNodeWithValue(5): True

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # T = O(1); S = O(1)
    def setHead(self, node):
        # Write your code here.
        if self.head == node:
            return
        if not self.head:
            self.head = self.tail = node
            return
        self.insertBefore(self.head, node)

    # T = O(1); S = O(1)
    def setTail(self, node):
        # Write your code here.
        if self.tail == node:
            return
        if not self.tail:
            self.head = self.tail = node
            return
        self.insertAfter(self.tail, node)

    # T = O(1); S = O(1)
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        node.prev = nodeToInsert
        if not nodeToInsert.prev:
            self.head = nodeToInsert
        else:
            nodeToInsert.prev.next = nodeToInsert

    # T = O(1); S = O(1)
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        node.next = nodeToInsert
        if not nodeToInsert.next:
            self.tail = nodeToInsert
        else:
            nodeToInsert.next.prev = nodeToInsert

    # T = O(p); S = O(1) where p is the position
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        i = 1
        while i < position and node:
            node = node.next
            i += 1

        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # T = O(n); S = O(1)
    def removeNodesWithValue(self, value):
        nextNode = self.head
        while nextNode:
            curNode = nextNode
            nextNode = nextNode.next
            if curNode.value == value:
                self.remove(curNode)

    # T = O(1); S = O(1)
    def remove(self, node):
        # Write your code here.

        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    # T = O(n); S = O(1)
    def containsNodeWithValue(self, value):
        # Write your code here.
        curNode = self.head
        while curNode:
            if curNode.value == value:
                return True
            curNode = curNode.next
        return False
