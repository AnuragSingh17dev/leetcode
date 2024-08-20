class Solution(object):
    def twoSum(self, nums, target):
        total = len(nums)
        for i in range(total - 1):
            for j in range (i + 1, total):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        