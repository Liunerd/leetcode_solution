class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        way = set()
        if n < 1:
            return False
        it = self.happyIter(n)
        for i in it:
            if i == 1:
                return True
            elif i in way:
                return False
            else:
                way.add(i)
            
    def happyIter(self, n):
        yield n
        while True:
            n = self.nextVal(n)
            yield n
            
    def nextVal(self, v):
        ret = 0
        while v > 0:
            a, b = divmod(v, 10)
            v = a
            ret += b*b
        return ret
                
        