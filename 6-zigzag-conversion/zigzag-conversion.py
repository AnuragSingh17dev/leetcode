class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        Pattern = [''] * numRows
        row_index, move = 0, 1

        for x in s:
            Pattern[row_index] += x
            if row_index == 0:
                move = 1
            elif row_index == numRows -1:
                move = -1
            row_index += move

        return ''.join(Pattern)