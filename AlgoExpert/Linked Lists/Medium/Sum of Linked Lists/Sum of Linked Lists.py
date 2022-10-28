# Medium

# Your're given two linked lists of potentially unequal length. Each Linked List represents a non-negetive
# integer, where each node in the Linked List is a digit of that integer, and the first node in each Linked
# List always represents the least significant digit of the integer, Write a function that returns the head
# of a new Linked List that represents the sum of the integers represented by the two input Linked Lists.
# Note that your function must create and return a new Linked List, and you're not allowed to modify either
# of the input Linked Lists.

# Sample Input
# linkedListOne = 2 -> 4 -> 7 -> 1
# linkedListTwo = 9 -> 4 -> 5

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    carryOut = 0
    result = LinkedList(0)
    head = result

    while linkedListOne and linkedListTwo:
        cur_sum = linkedListOne.value + linkedListTwo.value + carryOut
        cur_value = cur_sum % 10
        carryOut = cur_sum // 10

        result.value = cur_value
        if linkedListOne.next or linkedListTwo.next:
            result.next = LinkedList(0)
            result = result.next
        linkedListOne = linkedListOne.next
        linkedListTwo = linkedListTwo.next

    if linkedListOne:
        while linkedListOne:
            cur_sum = linkedListOne.value + carryOut
            cur_value = cur_sum % 10
            carryOut = cur_sum // 10
            result.value = cur_value
            if linkedListOne.next:
                result.next = LinkedList(0)
                result = result.next
            linkedListOne = linkedListOne.next

    if linkedListTwo:
        while linkedListTwo:
            cur_sum = linkedListTwo.value + carryOut
            cur_value = cur_sum % 10
            carryOut = cur_sum // 10
            result.value = cur_value
            if linkedListTwo.next:
                result.next = LinkedList(0)
                result = result.next
            linkedListTwo = linkedListTwo.next

    if carryOut:
        result.next = LinkedList(carryOut)
    return head



def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    head = None
    curNode = head
    carryOut = 0

    while linkedListOne or linkedListTwo or carryOut: ## CarryOut is edge case for there is one carry left at last.
        valueOne = linkedListOne.value if linkedListOne else 0
        valueTwo = linkedListTwo.value if linkedListTwo else 0
        curSum = valueOne + valueTwo + carryOut

        curValue = curSum % 10
        carryOut = curSum // 10
        if not head:
            head = curNode = LinkedList(curValue)
        else:
            curNode.next = LinkedList(curValue)
            curNode = curNode.next

        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None

    return head

## T = O(max(n, m)); S = O(max(n, m))
