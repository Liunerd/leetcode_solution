class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ret = ''
        for t in d:
            if self.valid(s, t) and (len(t) > len(ret) or (len(t) == len(ret) and t < ret)):
                ret = t
        return ret
    
    def valid(self, p, q):
        if len(p) < len(q):
            return False
        elif len(p) == len(q):
            return p == q
        else:
            i = 0
            for ch in p:
                if i >= len(q):
                    break
                elif ch == q[i]:
                    i += 1
            return i == len(q)