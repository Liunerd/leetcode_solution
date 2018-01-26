# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        lv, ret = [root], []
        while lv:
            ret.append([x.val for x in lv])
            nxt = []
            for node in lv:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            lv = nxt
        for i in range(1, len(ret), 2):
            ret[i] = ret[i][::-1]
        return ret