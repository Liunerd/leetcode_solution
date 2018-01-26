from math import ceil as ceil
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        li, p = [], head
        while p:
            li.append(p)
            p = p.next
        li[::2], li[1::2] = li[:ceil(len(li)/2)], li[:ceil(len(li)/2)-1:-1]
        for i in range(len(li)-1):
            li[i].next = li[i+1]
        li[-1].next = None
        