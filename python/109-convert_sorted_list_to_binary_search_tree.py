# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow, fast, tail = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            tail = slow
            slow = slow.next
        ret = TreeNode(slow.val)
        tail.next = None
        ret.left = self.sortedListToBST(head)
        ret.right = self.sortedListToBST(slow.next)
        return ret
        