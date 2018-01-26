# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ret = [root.val]
        ret += self.preorderTraversal(root.left)
        ret += self.preorderTraversal(root.right)
        return ret
        
# iteratively

