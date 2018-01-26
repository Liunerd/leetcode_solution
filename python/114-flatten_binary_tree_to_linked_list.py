# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        if root.left:
            l, r = root.left, root.right
            root.left = None
            self.flatten(l)
            root.right = l
            while l.right:
                l = l.right
            l.right = r
        self.flatten(root.right)