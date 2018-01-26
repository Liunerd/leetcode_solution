class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret, sign = (0, 1)
        if x < 0:
            sign = -1
            x = -x
        while x:
            ret = ret*10 + (x%10)
            x = int(x/10)
        ret *= sign
        if ret > 2147483647 or ret < -2147483648:
            ret = 0
        return ret