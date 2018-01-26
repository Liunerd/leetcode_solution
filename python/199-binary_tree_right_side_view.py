# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, li = [], [root]
        if root is None:
            return ret
        while len(li) != 0:
            ret.append(li[-1].val)
            temp = []
            for node in li:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            li = temp
        return ret