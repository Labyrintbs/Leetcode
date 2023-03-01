#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        if not inorder or postorder:
            return None
        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        rootIndex = inorder.index(rootVal)
        root.left = self.buildTree(inorder[:rootIndex], postorder)
        root.right = self.buildTree(inorder[rootIndex + 1:], postorder)
        return root
        '''
        if not inorder or not postorder:
            return None
        
        # Find the root node
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the index of the root node in the inorder list
        root_index = inorder.index(root_val)
        
        # Build the right subtree recursively
        root.right = self.buildTree(inorder[root_index+1:], postorder)
        
        # Build the left subtree recursively
        root.left = self.buildTree(inorder[:root_index], postorder)
        
        return root

        
        
# @lc code=end

