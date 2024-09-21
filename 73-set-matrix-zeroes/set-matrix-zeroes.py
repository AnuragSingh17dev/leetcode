class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rows_zero, cols_zero = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_zero.add(i)
                    cols_zero.add(j)

        for row in rows_zero:
            for j in range(cols):
                matrix[row][j] = 0

        for col in cols_zero:
            for i in range(rows):
                matrix[i][col] = 0