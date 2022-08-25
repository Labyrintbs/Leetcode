#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = []
        for i in s :
            if i.isalnum():
                s_alnum.append(i.upper())
        return s_alnum[::-1] == s_alnum
        
# @lc code=end

