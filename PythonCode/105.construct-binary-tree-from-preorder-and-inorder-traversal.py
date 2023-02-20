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
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
        '''
        if not preorder or not inorder:
            return None
        ret_tree = TreeNode(root_val)
        while preorder and inorder:
            root_val = preorder[0]
            left_index = find_leftindex(preorder,root_val)
            right_index = left_index + 1 #attention to limit
            left_tree = buildTree(preorder[1:left_index+1],inorder[:left_index])
            right_tree = buildTree(preorder[left_index+1:],inorder[left_index+1:])
            ret_tree.left = left_tree
            ret_tree.right = right_tree
        '''

        
# @lc code=end

