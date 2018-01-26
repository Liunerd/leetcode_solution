class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, c = 0, 0
        for i in nums:
            if c == 0:
                c = 1
                ret = i
            elif ret != i:
                c -= 1
            else:
                c += 1
        return ret