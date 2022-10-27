# Medium

# Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth
# node from the end of the list.

# The removal should be done in place, meaning that the original data structure should be mutated. Furthermore,
# the input head of the linked list should remain the head of the linked list after the removal is done,
# even if the head is the node that's supposed to be removed, your function should simply mutate its value
# and next pointer.

# Sample Input
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
# k = 4

# Sample Output
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next
    m = count - k + 1
    prev = None
    cur = head

    while cur:
        m -= 1
        if m == 0:
            break
        prev = cur
        cur = cur.next
    if not prev:
        head.value = head.next.value
        head.next = head.next.next
    else:
        prev.next = cur.next



###### More efficient method
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    count = 1
    left = right = head

    while count <= k:
        right = right.next
        count += 1

    if not right:
        head.value = head.next.value
        head.next = head.next.next
        return

    while right.next:
        right = right.next
        left = left.next
    left.next = left.next.next
