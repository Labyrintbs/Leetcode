#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List 
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        toSumDict = {}
        for i, v in enumerate(nums):
            if not v in toSumDict:
                toSumDict[target - v] = i
            else:
                return toSumDict[v], i
        '''
        #O(n^2 solution)
        n = len(nums)
        for i in range(n) :
            for j in range(n) :
                if nums[i] + nums[j] == target :
                    return i, j  
        '''
        
# @lc code=end

