class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last = {}
        for i, v in enumerate(nums):
            if v in last and i - last[v] <= k:
                return True
            else:
                last[v] = i
        return False