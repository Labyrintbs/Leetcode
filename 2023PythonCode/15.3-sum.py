#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if (not nums or n <3):
            return []
        ans = []
        #iterate through i, not j
        for i in range(n):
            if nums[i] > 0:
                return ans
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else: # found the triple
                    ans.append([nums[i], nums[j], nums[k]])
                    # omit repeating elements:
                    while (j < k and nums[j] == nums[j + 1]):
                        j += 1
                    while (j < k and nums[k] == nums[k - 1]):
                        k -= 1
                    k -= 1
                    j += 1
        return ans
'''
sol = Solution()
test1 = sol.threeSum([-1,0,1,2,-1,-4])
'''


        
# @lc code=end

