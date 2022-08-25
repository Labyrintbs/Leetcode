#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):  
        d = {}
        for i, v in enumerate(nums):
            if not v in d.keys():
                d[v] = i
            tofind = target - v
            if tofind in d.keys() and d[tofind]!= i:
                return [i, d[tofind]]
# @lc code=end

