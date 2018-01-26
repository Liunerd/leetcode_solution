class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        a = 0
        while x > a:
            i, j = divmod(x, 10)
            a *= 10
            a += j
            x = i
        return x == a or a == (x*10 + a%10)