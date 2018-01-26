class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')': '(', ']': '[', '}': '{'}
        if len(s) % 2 == 1:
            return False
        li = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                li.append(ch)
            elif ch not in d:
                return False
            elif len(li) == 0 or li[-1] != d[ch]:
                return False
            else:
                li.pop()
        return len(li) == 0
                