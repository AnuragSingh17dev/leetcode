class Solution(object):
    def twoSum(self, nums, target):
        total = {}
        for i in range(len(nums)):
            if target - nums[i] in total:
                return [total[target - nums[i]], i]
            total[nums[i]] = i
        return []
        