#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
'''
def maxSubArray(nums):
    max_sum = nums[0]
    cur_sum = 0
    for num in nums:
        cur_sum = cur_sum + num
        if cur_sum <0:
            cur_sum = 0
        max_sum = max(cur_sum, max_sum)
    return max_sum
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


def maxSubArray(nums):
    n = len(nums)
    dp = [0] * n
    for i in range(1,n):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    return max(dp)
maxSubArray([5,4,-1,7,8])
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        #greedy algorithme
        max_sum = float('-inf')
        cur_sum = 0
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(cur_sum, max_sum)
        return max_sum
        '''
        #dynamic programming
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)



        
# @lc code=end

