class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        w = 0
        for r, v in enumerate(nums):
            if r == 0:
                w += 1
            elif v != nums[w-1]:
                nums[w] = v
                w += 1
        return w
            