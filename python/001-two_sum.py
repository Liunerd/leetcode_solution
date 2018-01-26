class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, element in enumerate(nums):
            left = target - element
            if left in dic:
                return [dic[left], i]
            else:
                dic[element] = i
