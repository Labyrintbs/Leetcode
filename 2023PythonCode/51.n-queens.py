#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(board, row):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'
        
        def is_valid(board, row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check diagonal
            i, j = row-1, col-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i, j = row-1, col+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return result
        
# @lc code=end

