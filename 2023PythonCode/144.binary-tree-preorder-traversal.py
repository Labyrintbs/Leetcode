#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #preorder
        res = []
        def preorderHelper(root):
            if not root:
                return
            res.append(root.val)
            preorderHelper(root.left)
            preorderHelper(root.right)
        preorderHelper(root)
        return res
# @lc code=end

