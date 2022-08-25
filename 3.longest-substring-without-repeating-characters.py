#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #滑动窗口
        if not s:
            return 0
        n=len(s)
        res=0
        i=0
        dic={}
        for k in range(n):
            if s[k] not in dic:
                dic[s[k]]=k
            else:
                i=max(i,dic[s[k]]+1)
                dic[s[k]]=k
            res=max(res,k-i+1)
        return res

# @lc code=end

