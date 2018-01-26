class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        li = sorted(sorted(S), key=S.count)
        li[1::2], li[::2] = li[:len(S)//2], li[len(S)//2:]
        return ''.join(li) * (li[-1] != li[-2:-1])