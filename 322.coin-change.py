#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if i >=c:
                    dp[i] = min(dp[i], dp[i-c]+1)
        if dp[amount] == amount+1 :
            return -1
        else:
            return dp[amount]
        
# @lc code=end

