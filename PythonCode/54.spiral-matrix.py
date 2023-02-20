#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
'''
def spiral(matrix):
    if not matrix or not matrix[0]:
        return list()
    
    rows, columns = len(matrix), len(matrix[0])
    order = list()
    left, right, top, bottom = 0, columns - 1, 0, rows - 1
    while left <= right and top <= bottom:
        for column in range(left, right + 1):
            order.append(matrix[top][column])
        for row in range(top + 1, bottom + 1):
            order.append(matrix[row][right])
        if left < right and top < bottom:
            for column in range(right - 1, left, -1):
                order.append(matrix[bottom][column])
            for row in range(bottom, top, -1):
                order.append(matrix[row][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return order

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
print(spiral([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))

def spiral(matrix):
    res = []
    def up(matrix,res):
        if matrix == [[]] or matrix == []: return
        n = len(matrix[0])
        for i in range(n):
            res.append(matrix[0].pop(0))
        matrix.pop(0)
        return res
    
    def right(matrix, res):
        if matrix == [[]] or matrix == []: return
        m = len(matrix)
        for i in range(m):
            res.append(matrix[i].pop(-1))
        cp_matrix = list(matrix)
        for i in range(m):
            if line ==[]:
                matrix.remove(line)

        return res
    
    def down(matrix, res):
        if matrix == [[]] or matrix == []: return
        n = len(matrix[0])
        m = len(matrix)
        for i in range(n-1,-1,-1):
            res.append(matrix[m-1].pop(-1))
        matrix.pop(-1)
        return res
    def left(matrix, res):
        if matrix == [[]] or matrix == []: return
        m = len(matrix)
        for i in range(m-1, -1,-1):
            res.append(matrix[i].pop(0))
        return res
    while len(matrix) >=1:
        up(matrix, res)
        right(matrix,res)
        down(matrix,res)
        left(matrix,res)
    return res
print(spiral([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
'''
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order



# @lc code=end

