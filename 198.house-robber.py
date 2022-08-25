#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob = nums[0]
        no_rob = 0
        for i in range(1,n):
            rob, no_rob = nums[i] + no_rob, max(rob, no_rob)
        return max(rob, no_rob)
# @lc code=end

