#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        S = (r-l) * min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                l +=1
                new_S = (r-l) * min(height[l], height[r])
                if new_S > S:
                    S = new_S
            else:
                r -= 1
                new_S = (r-l) * min(height[l], height[r])
                if new_S > S:
                    S = new_S
        return S 

                    

# @lc code=end

