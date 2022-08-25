#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
'''
def maxProduct(nums):
    n = len(nums)
    if n ==1 :
        return nums[0]
    elif n == 2:
        return max(nums[0] * nums[1], nums[1]) 

    dp_max = nums[0]
    dp_min = nums[0]
    res_max = nums[0]

    for i in range(1, n):
        dp_max, dp_min  = max(nums[i], dp_max * nums[i], dp_min * nums[i]), min(nums[i], dp_max * nums[i], dp_min * nums[i])
        res_max = max(dp_max, res_max)
    return dp_max 
maxProduct([2,3,-2,4])
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1 :
            return nums[0]
        elif n == 2:
            return max(nums[0] * nums[1], nums[1]) 
        dp_max = nums[0]
        dp_min = nums[0]
        res_max = nums[0]

        for i in range(1, n):
            dp_max, dp_min  = max(nums[i], dp_max * nums[i], dp_min * nums[i]), min(nums[i], dp_max * nums[i], dp_min * nums[i])
            res_max = max(dp_max, res_max)
        return res_max 
        
# @lc code=end

