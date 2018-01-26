# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        lv, ret = [root], []
        while lv:
            ret.insert(0, [x.val for x in lv])
            nxt = []
            for node in lv:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            lv = nxt
        return ret