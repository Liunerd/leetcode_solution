# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        x = dummyhead
        while l1 or l2:
            if l1 is None:
                x.next = l2
                l2 = l2.next
            elif l2 is None:
                x.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                x.next = l1
                l1 = l1.next
            else:
                x.next = l2
                l2 = l2.next
            x = x.next
        return dummyhead.next
        