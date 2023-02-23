#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]: #not pivoted at left
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1 #pivoted at right
            else: # not pivoted at right
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


        
# @lc code=end

