class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helper(nums, 0, len(nums), target)
        
    def helper(self, nums, start, end, target):
        if start == end-1:
            return start if target <= nums[start] else start+1
        mid = start + (end - start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.helper(nums, start, mid, target)
        else:
            return self.helper(nums, mid, end, target)