#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
'''
def insert(intervals, newInterval):
    res = []
    t= 0
    for interval in intervals:
        if interval[1]<newInterval[0]:
            res.append(interval)
        elif interval[0] > newInterval[1]:
            break
        else:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1],newInterval[1])
        t += 1
    return res + [newInterval] + intervals[t:]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
'''
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        n = len(intervals)
        l, r =0, n
        l1, r1 = l,r
        l2, r2 = l,r
        mid1 = (l1 + r1) // 2
        mid2 = (l2 + r2) // 2
        left_index = 0
        right_index = 0
        #left research
        while l1 < r1:
            if newInterval[0] < intervals[mid1][0]:
                r1 = mid1
            elif newInterval[0] > intervals[mid1][1]:
                l1 = mid1
            else:
                left_index = mid1
            mid1 = (l1+r1)//2
        while l2 < r1:
            if newInterval[0] < intervals[mid2][0]:
                r1 = mid2
            elif newInterval[0] > intervals[mid2][1]:
                l2 = mid2
            else:
                right_index = mid2
            mid2 = (l2+r2)//2
        '''

        res = []
        t= 0
        for interval in intervals:
            if interval[1]<newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                break
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
            t += 1
        return res + [newInterval] + intervals[t:]

        

        
# @lc code=end

