class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        row_index = 0
        Pattern = [""]*numRows
        for letter in s:
            if row_index == numRows-1:
                grow = False
            elif row_index == 0:
                grow = True 
            Pattern[row_index] += letter
            row_index = (row_index+1) if grow else row_index-1
			                            						
        return "".join(Pattern)