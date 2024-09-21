class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        row_zero = [False] * m
        col_zero = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    row_zero[row] = True
                    col_zero[col] = True

        for row in range(m):
            for col in range(n):
                if row_zero[row] or col_zero[col]:
                    matrix[row][col] = 0