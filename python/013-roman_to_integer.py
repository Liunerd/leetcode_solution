class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        values = []
        for ch in s:
            v = roman[ch]
            if values and values[-1] < v:
                values[-1] = -values[-1]
            values.append(v)
        return sum(values)