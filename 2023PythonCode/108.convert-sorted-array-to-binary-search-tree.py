#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #false implementation with only insert operation
        '''
        mid = len(nums) // 2
        newValue = nums.pop(mid)
        root = TreeNode(newValue)
        def insertValue(root, newValue):
            if not root:
                return TreeNode(newValue)
            if newValue < root.val:
                root.left = insertValue(root.left, newValue)
            elif newValue > root.val:
                root.right = insertValue(root.right, newValue)
            return root
        for _ in range(len(nums)):
            mid = len(nums) // 2
            newValue = nums.pop(mid)
            root = insertValue(root, newValue)
        return root
        '''
        if not nums:
            return None
        mid = len(nums) // 2
        #newValue = nums.pop(mid)
        newValue = nums[mid]
        root = TreeNode(newValue)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    

        
# @lc code=end

