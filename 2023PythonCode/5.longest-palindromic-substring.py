#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) 
        if n < 2:
            return s
        max_len = 1
        refer_index = 0
        DP = [[False] * n for _ in range(n)]
        #Initialization
        for i in range(n):
            DP[i][i] = True
        
        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break

                if s[i] != s[j]:
                    DP[i][j] = False
                else:
                    if j - i < 3:
                        DP[i][j] = True
                    # REASSIGNMENT OF STATE!
                    else:
                        DP[i][j] =  DP[i + 1][j - 1] 
            
                if DP[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    refer_index = i
        
        return s[refer_index:refer_index + max_len] 

        
# @lc code=end

