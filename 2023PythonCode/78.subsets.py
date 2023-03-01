#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, subset):
            res.append(subset)
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset[:])
                subset.pop()
        backtrack(0, [])
        return res
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(subset, index):
            res.append(subset[:])
            for i in range(index, n):
                subset.append(nums[i])
                backtrack(subset, index + 1)
                subset.pop()
        backtrack([], 0)
        return res
    '''


sol = Solution()
test1 = sol.subsets([1,2,3])
        
# @lc code=end

