# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        oddhead, evenhead, odd, even = ListNode(0), ListNode(0), head, head.next
        otail, etail = oddhead, evenhead
        while odd and even:
            otail.next, etail.next = odd, even
            otail, etail = otail.next, etail.next
            odd = even.next
            if odd is None:
                break
            even = odd.next
            if even is None:
                otail.next = odd
                otail = otail.next
                break
        otail.next, etail.next = evenhead.next, None
        return oddhead.next