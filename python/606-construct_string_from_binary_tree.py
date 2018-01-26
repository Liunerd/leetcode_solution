class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        ret = str(t.val)
        if t.left is None and t.right is None:
            return ret
        ret += '(' + self.tree2str(t.left) + ')'
        if t.right:
            ret += '(' + self.tree2str(t.right) + ')'
        return ret