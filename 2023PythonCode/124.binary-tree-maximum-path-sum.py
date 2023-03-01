#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        
        def maxPathSumHelper(node):
            
            nonlocal maxSum
            if not node:
                return 0
            
            leftSum = max(0, maxPathSumHelper(node.left))
            rightSum = max(0, maxPathSumHelper(node.right))
            
            currentSum = node.val + leftSum + rightSum
            
            maxSum = max(maxSum, currentSum)
            
            return node.val + max(leftSum, rightSum)
        
        maxPathSumHelper(root)
        return maxSum