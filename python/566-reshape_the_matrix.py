class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums[0]) == 0:
            return nums
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        li = [y for x in nums for y in x]
        return [li[a:a+c] for a in range(0, r*c, c)]