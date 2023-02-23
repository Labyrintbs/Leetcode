#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Backtrack implementation
        '''
        res = []
        def backtrack(s, opencount, closecount):
            if (len(s) == 2 * n):
                res.append(s)
                return
            
            if opencount < n:
                backtrack(s + '(', opencount + 1, closecount)
            if closecount < opencount:
                backtrack(s + ')', opencount, closecount + 1)
        backtrack('', 0, 0)
        return res
        '''  
        if n == 0:
            return []

        # Dynamic Programming implementation
        DP = [[] for _ in range(n + 1)]
        DP[0].append('')
        for i in range (1, n + 1):
            for j in range(i):
                for x in DP[j]:
                    for y in DP[i - j - 1]:
                        DP[i].append('({}){}'.format(x, y))
        return DP[n]
        
# @lc code=end
