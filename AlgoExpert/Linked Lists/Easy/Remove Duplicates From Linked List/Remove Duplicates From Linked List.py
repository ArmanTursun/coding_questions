# Easy

# You're given a head of a Singly Linked List whose nodes are in sorted order.
# Write a function that returns a modified version of the Linked List that doesn't contain
# any nodes with duplicate values.

# Sample Input
# linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

# Sample Output
# 1 -> 3 -> 4 -> 5 -> 6

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    head = linkedList
    while linkedList:
        if linkedList.next and linkedList.value == linkedList.next.value:
            linkedList.next = linkedList.next.next
        else:
            linkedList = linkedList.next

    return head

## T = O(n); S = O(1)