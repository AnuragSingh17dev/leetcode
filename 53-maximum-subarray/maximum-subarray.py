class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur_max = sum_max = nums[0]
        for val in nums[1:]:
            cur_max = max(val, cur_max + val)
            sum_max = max(sum_max, cur_max)
        return sum_max