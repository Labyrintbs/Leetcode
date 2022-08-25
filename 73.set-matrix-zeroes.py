#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def zero_padding(mat, mark):
            m = len(mat)
            n = len(mat[0])
            rang, col = mark[0], mark[1]
            for i in range(n):
                mat[rang][i] = 0
            for j in range(m):
                mat[j][col] = 0

        zero_markers = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_markers.append((i,j))
        
        for marker in zero_markers:
            zero_padding(matrix, marker)
        
        return matrix
        
# @lc code=end

