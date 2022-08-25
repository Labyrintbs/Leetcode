#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
'''
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1]* (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(i):
            if nums[j] > nums[i]:
                dp[j] = max(dp[i]+1, dp[j])

    return dp[n]
'''
def lengthOfLIS(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
lengthOfLIS([10,9,2,5,3,7,101,18])
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]* (n)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])

        return max(dp)
'''


# @lc code=end

