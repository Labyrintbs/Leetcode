#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res 
        queue = [root]
        while queue:
            levelVal = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                levelVal.append(cur.val)
            res.append(levelVal)
        return res
                
            
        
# @lc code=end

