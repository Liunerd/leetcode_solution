class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = True
        for i, v in enumerate(A):
            if flag: # 2 candidates, i and i+1
                if v == i:
                    continue
                elif v == i+1:
                    flag = False
                else:
                    return False
            else: # only one candidate, i-1
                if v == i-1:
                    flag = True
                else:
                    return False
        return True