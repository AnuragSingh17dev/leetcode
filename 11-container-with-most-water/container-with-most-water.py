class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxCapacity, lp, rp = 0, 0, len(height)-1
        while (lp < rp):
            if height[lp] <= height[rp]:
                capacity = height[lp] * (rp - lp)
                lp += 1
            else:
                capacity = height[rp] * (rp - lp)
                rp -= 1
            if capacity > maxCapacity: maxCapacity = capacity
        return maxCapacity