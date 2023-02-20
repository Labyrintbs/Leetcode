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
        tot_max = float('-inf')
        def helper(root):
            nonlocal tot_max
            if not root:
                return 0
            elif not root.left and not root.right:
                tot_max = max(tot_max, root.val)
                return root.val
            left_tot = max(helper(root.left),0)
            right_tot = max(helper(root.right), 0)
            tot_max = max(tot_max, left_tot + root.val + right_tot)
            root_val = root.val + max(left_tot, right_tot)
            return root_val
        helper(root)
        return tot_max 
            
            
        
# @lc code=end

