#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
'''
def merge(nums1,m,nums2,n):
    #nums1 = nums1 + [0] * n
    if m==0:
        nums1 = nums2[:]
    for n2 in range(len(nums2)):
        for n1 in range(len(nums1)-1):
            if nums2[n2] < nums1[n1+1] or nums1[n1+1]==0:
                nums1.insert(n1+1,nums2[n2])
                nums1.pop()
                break

merge([1,2,3,0,0,0],3,[2,5,6],3)
merge([0],0,[1],1)
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for n2 in range(len(nums2)):
            for n1 in range(len(nums1)):
                if nums2[n2] < nums1[n1] :
                    nums1.insert(n1,nums2[n2])
                    nums1.pop()
                    break
                elif n1 == m+n2:
                    nums1.insert(n1,nums2[n2])
                    nums1.pop()
                    break


            
# @lc code=end

