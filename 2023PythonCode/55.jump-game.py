#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        # DP solution:
        '''
        reachable = [False] * n
        reachable[0] = True 
        for i in range(n):
            if not reachable[i]:
                continue
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                if reachable[j]:
                    continue
                reachable[j] = True
                if j == len(nums)-1:
                    return True

        # If we reach the end of the loop without returning True, then the last index is not reachable
        return False
        '''

        #Greedy solution
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        




        
# @lc code=end

