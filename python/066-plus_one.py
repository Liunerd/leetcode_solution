class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            a, b = divmod(digits[i] + carry, 10)
            digits[i] = b
            carry = a
        if carry:
            digits.insert(0, carry)
        return digits