#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return s
        lookup = set()
        r = 0
        max_len = 0
        n = len(s)
        for l in range(n):
            if l != 0:
                lookup.remove(s[l-1])
            while r < n - 1 and s[r + 1] not in lookup:
                lookup.add(s[r + 1])
                r += 1
            max_len = max(max_len, r - l + 1)
        return max_len


            

        
# @lc code=end

