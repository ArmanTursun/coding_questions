# Hard

# Write a function in the heads of two Single Linked Lists that are in sorted order, respectively. The function
# should merge the lists in place and return the head of the merged list; the merged list should be in sorted order.

# Sample Input
# headOne = 2 -> 6 -> 7 -> 8
# headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10

# Sample Output
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    recursiveMerge(headOne, headTwo, None)
    return headOne if headOne.value < headTwo.value else headTwo

def recursiveMerge(p1, p2, p1Prev):
    if not p1:
        p1Prev.next = p2
        return
    if not p2:
        return

    if p1.value < p2.value:
        recursiveMerge(p1.next, p2, p1)
    else:
        if p1Prev:
            p1Prev.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerge(p1, newP2, p2)
## T = O(n + m); S = O(m + n)


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    if headOne.value <= headTwo.value:
        return merge(headOne, headTwo)
    else:
        return merge(headTwo, headOne)

def merge(headMain, headSub):
    head = headMain

    while headMain and headSub:
        if headMain.next and headMain.next.value >= headSub.value:
            temp = headSub.next
            headSub.next = headMain.next
            headMain.next = headSub
            headSub = temp
            headMain = headMain.next
        elif not headMain.next:
            headMain.next = headSub
            break
        else:
            headMain = headMain.next
    return head
## T = O(n + m); S = O(1)
