#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(combination, curNums):
            if not curNums:
                res.append(list(combination))
                return
            '''
            for num in curNums:
                combination.append(num)
                backtrack(combination, list(curNums).remove(num))
                combination.pop()
            ''' 
            for i in range(len(curNums)):
                num = curNums[i]
                combination.append(num)
                backtrack(combination, curNums[:i] + curNums[i+1:])
                combination.pop()
        
        backtrack([], nums)
        return res
        
# @lc code=end

'''
def permute(nums):
    res = []
    n = len(nums)
    def backtrack(combination, curNums):
        if not curNums:
            res.append(list(combination))
            return
        for num in curNums:
            combination.append(num)
            backtrack(combination, list(curNums).remove(num))
            combination.pop()
        for i in range(len(curNums)):
            num = curNums[i]
            combination.append(num)
            backtrack(combination, curNums[:i] + curNums[i+1:])
            combination.pop()
    
    backtrack([], nums)
    return res

permute([1,2,3])
'''
