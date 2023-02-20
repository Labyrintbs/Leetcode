#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#store_digits(2345)
'''
def canJump(nums):
    max_len = 0
    for i in range(len(nums)-1):
        if i <=max_len:
            max_len = max(max_len, i+nums[i])
            if max_len >= len(nums) - 1:
                return True
    return False
canJump([0,2,3])
'''
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        for i in range(len(nums)):
            if i <= max_len:
                max_len = max(max_len, i+nums[i])
                if max_len >= len(nums) - 1:
                    return True
        return False
        



        
# @lc code=end

