# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return abs(self.tsum(root.left) - self.tsum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
        
    def tsum(self, root):
        if root is None:
            return 0
        return self.tsum(root.left) + self.tsum(root.right) + root.val