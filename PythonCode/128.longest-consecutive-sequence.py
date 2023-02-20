#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list_set = set(nums)
        biggest = 0
        for x in list_set:
            if not x-1 in list_set:
                y = x + 1
                while y in list_set:
                    y +=1
                biggest = max(biggest, y-x)
        return biggest

        
# @lc code=end

