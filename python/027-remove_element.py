class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        w = 0
        for r, v in enumerate(nums):
            if v != val:
                nums[w] = v
                w += 1
        return w