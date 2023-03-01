#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootVal = preorder.pop(0)
        rootIndex = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder, inorder[:rootIndex])
        root.right = self.buildTree(preorder, inorder[rootIndex + 1 :])
        return root



        
# @lc code=end

