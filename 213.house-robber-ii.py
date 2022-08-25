#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


def my_rob(nums):
    def my_rob(nums):
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur
    return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]
my_rob([2,3,2])
# @lc code=start
class Solution:
    def my_rob(nums):
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]







        
# @lc code=end

