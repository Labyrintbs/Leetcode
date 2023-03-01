#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal = float('-inf')
        maxVal = float('inf')
        return self.checkBST(root, minVal, maxVal)
    def checkBST(self, root, minVal, maxVal):
        if not root:
            return True
        
        if root.val <= minVal or root.val >= maxVal:
            return False
        
        return self.checkBST(root.left, minVal, root.val) and self.checkBST(root.right, root.val, maxVal)
    
        
    
    



        
# @lc code=end
'''
class Solution:
    def isValidBST(self, root):
        if self.isLeaf(root):
            return root.val
        
        leftVal = self.isValidBST(root.left)
        rightVal = self.isValidBST(root.right)
        # determine recursively if it is a valid BST
        if (leftVal < root.val < rightVal):
            return True
        else:
            return False
    
    def isLeaf(self, root):
        if not root.left and not root.right: return True 
        else: return False
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7)))
sol = Solution()
test1 = sol.isValidBST(root)
'''