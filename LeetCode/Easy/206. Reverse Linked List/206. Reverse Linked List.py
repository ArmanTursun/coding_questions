# Easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        q = head

        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        head = p
        return head
## T = O(n); S = O(1)