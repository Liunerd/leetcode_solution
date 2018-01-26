﻿# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummyhead = curr = ListNode(0)
        while l1 or l2 or carry:
        	if l1:
        		carry += l1.val
        		l1 = l1.next
        	if l2:
        		carry += l2.val
        		l2 = l2.next
        	curr.next = ListNode(carry%10)
        	carry = int(carry/10)
        	curr = curr.next
        return dummyhead.next