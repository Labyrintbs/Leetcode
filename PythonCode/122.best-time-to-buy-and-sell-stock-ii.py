#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        '''
        dp = [0, -prices[0]]
        for i in range(1,len(prices)):

            dp[0], dp[1] = max(dp[0], dp[1]+prices[i]), max(dp[1], dp[0]-prices[i])
        return max(dp[0], dp[1])
        '''
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += (prices[i]-prices[i-1])
        return max_profit

        
# @lc code=end

