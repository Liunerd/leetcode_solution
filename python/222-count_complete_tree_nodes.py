# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        lheight, p = 0, root
        while p:
            lheight += 1
            p = p.left
        return 2**lheight-1 - self.countMissing(root, lheight)
        
    def countMissing(self, root, h):
        if root is None:
            return 1 if h == 1 else 0
        rheight, p = 0, root
        while p:
            rheight += 1
            p = p.right
        if rheight == h:
            return 0
        return self.countMissing(root.left, h-1) + self.countMissing(root.right, h-1)
        