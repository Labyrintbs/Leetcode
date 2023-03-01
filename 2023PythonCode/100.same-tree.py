#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #preorder
        #empty node
        if not p and not q:
            return True
        # leaf node
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        # other case
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

        
        
# @lc code=end

