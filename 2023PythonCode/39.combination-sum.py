#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def backtrack(combination, start_index, target):
            if target == 0:
                #BE CAREFUL OF THE REFERENCE OF MUTABLE OBJECT!
                res.append(list(combination))
                return
            for i in range(start_index, n):
                if candidates[i] > target:
                    break
                combination.append(candidates[i])
                backtrack(combination, i, target - candidates[i])
                # Remove the current candidate from the combination 
                # before moving on to the next iteration
                combination.pop()
        backtrack([],0, target)
        return res

        
# @lc code=end

