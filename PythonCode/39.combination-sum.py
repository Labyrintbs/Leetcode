#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, path, res):
            if target == 0:
                res.append(path)
                return
            for i in range(len(candidates)):
                if target < candidates[i]:
                    break
                dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)
        res = []
        dfs(sorted(candidates), target, [], res)
        return res
        
# @lc code=end

