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
        index, move = 0, 1

        for x in s:
            Pattern[index] += x
            if index == 0:
                move = 1
            elif index == numRows -1:
                move = -1
            index += move

        return ''.join(Pattern)