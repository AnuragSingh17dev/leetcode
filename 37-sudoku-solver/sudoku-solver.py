class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """        
        def validGrid(row, col, ch):
            row, col = int(row), int(col)
            
            for i in range(9):
                
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                    return False
            return True
            
        def solveGrid(row, col):
            if row == 9:
                return True
            if col == 9:
                return solveGrid(row+1, 0)
            
            if board[row][col] == ".":
                for i in range(1, 10):
                    if validGrid(row, col, str(i)):
                        board[row][col] = str(i)
                        
                        if solveGrid(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solveGrid(row, col + 1)

        solveGrid(0, 0)