#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth):
            if not node:
                return depth
            else:
                return max(helper(node.left, depth+1), helper(node.right, depth+1))
        return helper(root,0)
        
# @lc code=end

