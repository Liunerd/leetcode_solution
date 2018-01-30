class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ret = 0
        for ch in S:
            if ch in J:
                ret += 1
        return ret