# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        li = [root]
        ret = [-1, -1]
        while len(li) > 0:
            p = li.pop()
            if p.left:
                li.append(p.left)
            if p.right:
                li.append(p.right)
            if ret[0] == -1:
                ret[0] = p.val
            elif p.val < ret[0]:
                ret[1] = ret[0]
                ret[0] = p.val
            elif p.val > ret[0] and (ret[1] == -1 or p.val < ret[1]):
                ret[1] = p.val
        return ret[1]