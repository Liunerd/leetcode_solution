class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ret, val = nums[0], 0
        for item in nums:
            val += item
            ret = max(ret, val)
            if val < 0:
                val = 0
        return ret