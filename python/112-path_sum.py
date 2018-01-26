# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        target = sum - root.val
        if root.left and self.hasPathSum(root.left, target):
            return True
        if root.right and self.hasPathSum(root.right, target):
            return True
        return False