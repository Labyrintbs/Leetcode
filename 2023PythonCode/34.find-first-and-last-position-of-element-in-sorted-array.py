#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        left, right = -1, -1
        def searchHelper(nums, target, leftmin, rightmax):
            l = 0
            r = len(nums)
            mid = (l + r) // 2
            if nums[mid] == target:
                if leftmin == -1:
                    return mid, max(mid, rightmax)
                else:
                    return min(mid, leftmin), max(mid, rightmax)
            leftMin, leftMax = searchHelper(nums[:mid], target, -1, -1)
            rightMin, rightMax = searchHelper(nums[mid + 1:], target, -1, -1)
            return [leftMin, rightMax]
        res = searchHelper(nums, target, -1, -1)
        return res
        """
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]

    def binarySearch(self, nums, target, isFirst):
        n = len(nums)
        left, right = 0, n - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if isFirst:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
            

        
# @lc code=end

