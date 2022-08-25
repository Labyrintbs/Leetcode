#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
'''
def merge(intervals):
    ordered_intervals = intervals.sort(key = lambda k : k[0])
    res = []
    for interval in ordered_intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        elif res[-1][1] >= interval[0]:
            res.append(res.pop()[0], interval[1])
    return res
print(merge([[1,3],[2,6],[8,10],[15,18]]))
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda k : k[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            elif res[-1][1] >= interval[0]:
                temp = res.pop()
                res.append([temp[0], max( temp[1],interval[1])])
        return res

        
# @lc code=end

