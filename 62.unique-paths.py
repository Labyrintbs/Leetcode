#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
'''
def uniquePaths(m,n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0]= 1
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(1,m):
        for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[m-1][n-1]
print(uniquePaths(3,7))
'''
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0]= 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
# @lc code=end

