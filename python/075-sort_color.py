class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        color = [0,0,0]
        for pixel in nums:
            color[pixel] += 1
        for i in range(len(nums)):
            if color[0]:
                nums[i] = 0
                color[0] -= 1
            elif color[1]:
                nums[i] = 1
                color[1] -= 1
            else:
                nums[i] = 2