#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
'''
def search(nums, target) -> int:
    if not nums:
        return -1
    n = len(nums)
    l, r = 0, n-1
    while l<=r :
        mid = (r+l) // 2 
        if nums[mid] == target:
            return mid
        if nums[l] < nums[mid]:# situation that good order in the letf
            if nums[l] <= target < nums[mid]:
                r = mid -1
            else:
                l = mid+1
        else:#good order in right
            if nums[mid] < target <= nums[r]:
                l = mid+1
            else:
                r = mid-1
    return -1

search([3,1],1)
'''
class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        '''
        if not nums:
            return -1
        n = len(nums)
        l, r = 0, n-1
        while l<=r :
            mid = (r+l) // 2 
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:# situation that good order in the letf
                if nums[0] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid+1
            else:#good order in right
                if nums[mid] < target <= nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
        '''
        try:
            return nums.index(target)
        except ValueError:
            return -1



        
# @lc code=end

