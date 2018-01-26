# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev, curr, nxt = None, head, head.next
        while True:
            curr.next = prev
            if nxt is None:
                break
            prev = curr
            curr = nxt
            nxt = nxt.next
        return curr