#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
'''
def numIslands(grid) -> int:
    row = len(grid)
    col = len(grid[0])
    #visited = [[0 for _ in range(col)] for _ in range(row)]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    island_nb = 0
    def dfs(r,c):
        grid[r][c] = '0' 
        for x, y in directions:
            x, y = r+x, c+y
            if 0<= x < row and 0<= y < col and grid[x][y]== '1':
                dfs(x,y)
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                island_nb +=1
                dfs(i,j)
    return island_nb
numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
)
'''
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        #visited = [[0 for _ in range(col)] for _ in range(row)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        island_nb = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    island_nb += 1
                    q = [(i,j)]
                    while q:
                        r, c = q.pop(0)
                        for x, y in directions:
                            x, y = r+x, c+y
                            if 0<= x < row and 0<= y < col and grid[x][y]== '1':
                                grid[x][y] = '0'
                                q.append((x,y))
        return island_nb

        def dfs(r,c):
            grid[r][c] = '0' 
            for x, y in directions:
                x, y = r+x, c+y
                if 0<= x < row and 0<= y < col and grid[x][y]== '1':
                    dfs(x,y)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    island_nb +=1
                    dfs(i,j)
        return island_nb


        



            
        
# @lc code=end

