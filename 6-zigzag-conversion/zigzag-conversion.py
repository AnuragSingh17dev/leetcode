class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        pattern = [''] * numRows
        initial = 0
        move = False
        
        for letter in s:
            pattern[initial] += letter
            
            if initial == 0 or initial == numRows - 1:
                move = not move
            
            initial += 1 if move else -1
        
        return ''.join(pattern)