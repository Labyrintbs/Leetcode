#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxArea = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                maxArea = max(maxArea, height[left] * (right - left))
                left += 1
            else:
                maxArea = max(maxArea, height[right] * (right - left))
                right -= 1
        return maxArea
        
# @lc code=end

