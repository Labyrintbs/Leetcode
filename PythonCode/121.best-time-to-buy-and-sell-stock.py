#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp to maintain the min price before day i 
        dp = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            max_profit = max(max_profit, prices[i]-dp)
            dp = min(dp, prices[i])
        return max_profit
        
# @lc code=end

