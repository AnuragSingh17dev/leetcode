class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def validGrid(row, col, num):
            for i in range(9):
                if board[row][i] == str(num) or board[i][col] == str(num):
                    return False
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[row_start + i][col_start + j] == str(num):
                        return False
            return True
        
        def solveGrid(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if validGrid(i, j, num):
                                board[i][j] = str(num)
                                if solveGrid(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True
        
        solveGrid(board)