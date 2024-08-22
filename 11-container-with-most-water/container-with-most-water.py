class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lp = 0
        rp = len(height) - 1
        maxCapacity = 0
        
        while lp < rp:
            width = rp - lp
            
            h = min(height[lp], height[rp])
            
            capacity = width * h
            
            maxCapacity = max(maxCapacity, capacity)
            
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        
        return maxCapacity