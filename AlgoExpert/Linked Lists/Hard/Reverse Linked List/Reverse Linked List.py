# Hard

# Write a function that takes in the head of a Singly Linked List, reverse the list in place and returns
# its new head. Each LinkedList node has an integer value as well as a next node pointing to the next node
# in the list or to None/null if it's the tail of the list.

# You can assume that the input Linked List will always have at least one node; in other words, the head
# will never be None/null.

# Sample Input
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5

# Sample output
# 0 <- 1 <- 2 <- 3 <- 4 <- 5 (head)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    p = None
    q = head

    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    head = p
    return head

# T = O(n); S = O(1)