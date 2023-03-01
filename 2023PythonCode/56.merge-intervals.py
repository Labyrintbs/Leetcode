#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        sorted = []
        cur = intervals[0]
        for i in range(n):
            if cur[1] >= intervals[i][0]:
                cur = self.mergeTwoInterval(cur, intervals[i])
            else:
                sorted.append(cur)
                cur = intervals[i]
        sorted.append(cur)
        return sorted
    def mergeTwoInterval(self, cur, tomerge):
        return [min(cur[0], tomerge[0]), max(cur[1], tomerge[1])]

        
# @lc code=end

