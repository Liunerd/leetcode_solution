class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rn = [['I', 'V'],['X', 'L'],['C', 'D'],['M', '']]
        ret, lv, li = '', 0, []
        while num > 0:
            a, b = divmod(num, 10)
            if 0 < b < 4:
                s = rn[lv][0]*b
                li.append(s)
            elif b == 4:
                li.append(rn[lv][0]+rn[lv][1])
            elif b == 5:
                li.append(rn[lv][1])
            elif 5 < b < 9:
                li.append(rn[lv][1]+rn[lv][0]*(b-5))
            elif b == 9:
                li.append(rn[lv][0]+rn[lv+1][0])
            num = a
            lv += 1
        return ''.join(li[::-1])
            