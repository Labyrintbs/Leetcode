#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right== -1:
                return -1
            return max(left, right)+1 if abs(left-right) <=1 else -1
        return helper(root) != -1

        
        
# @lc code=end

