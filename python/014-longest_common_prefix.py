class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        ret = strs[0]
        for s in strs:
            ret = self.commonPrefix(ret, s)
        return ret
    
    def commonPrefix(self, a, b):
        '''
        return common prefix of a and b
        '''
        ret = ''
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                break
            ret += a[i]
        return ret