# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        n = self.nodeCount(root.left)
        if n+1 == k:
            return root.val
        elif n >= k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-n-1)
        
    def nodeCount(self, root):
        if root is None:
            return 0
        return self.nodeCount(root.left) + self.nodeCount(root.right) + 1