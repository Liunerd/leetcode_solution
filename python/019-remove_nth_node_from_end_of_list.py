# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        x, y = head, dummyhead
        while n > 1:
            x = x.next
            n -= 1
        while x.next:
            x = x.next
            y = y.next
        y.next = y.next.next
        return dummyhead.next