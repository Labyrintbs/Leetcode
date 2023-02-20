#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        mem = {}
        mem[1] = 1
        mem[2] = 2
        def helper(m):
            if m in mem:
                return mem[m]
            else:
                mem[m] = helper(m-1) + helper(m-2)
                return mem[m]
        return helper(n)
        '''
        #dp version
        if n == 0 :return 0
        if n== 1: return 1
        if n==2 : return 2
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range (3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
                

        
# @lc code=end

