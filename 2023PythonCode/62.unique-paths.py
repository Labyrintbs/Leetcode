#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        #dfs solve
        res = 0
        def dfs(m, n):
            nonlocal res
            if m == 0 and n == 0:
                res += 1
                return
            elif m < 0 or n < 0:
                return
            dfs(m - 1, n)
            dfs(m, n - 1)
        dfs(m-1, n-1)
        return res
        '''
        #f(i,j) -> ways from (0, 0) to i, j
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


        
# @lc code=end

