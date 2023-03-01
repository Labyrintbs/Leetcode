#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathSumHelper(root, target):
            if not root:
                return target == 0
            elif not root.left and not root.right:
                return target == root.val 
            
            #if root.left: leftSum = hasPathSumHelper(root.left, target - root.val)
            #if root.right: rightSum = hasPathSumHelper(root.right, target - root.val)
            leftSum, rightSum = False, False
            leftSum = hasPathSumHelper(root.left, target - root.val) if root.left else False
            rightSum = hasPathSumHelper(root.right, target - root.val) if root.right else False
            return leftSum or rightSum
        
        if not root:
            return False
        res = hasPathSumHelper(root, targetSum)
        return res
'''
            
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        def hasPathSumHelper(root, target):
            if not root:
                return target == 0
            elif not root.left and not root.right:
                return target == root.val 
            if root.left: leftSum = hasPathSumHelper(root.left, target - root.val)
            if root.right: rightSum = hasPathSumHelper(root.right, target - root.val)
            return root.left or root.right
        
        return hasPathSumHelper(root, targetSum)

test1 = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
sol.hasPathSum(test1, 5)
    
'''
# @lc code=end

