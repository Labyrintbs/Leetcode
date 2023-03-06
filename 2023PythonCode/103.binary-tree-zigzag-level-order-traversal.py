#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = [root]
        flag = 1
        while queue:
            levelVal = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                levelVal.append(cur.val)
            if flag == 1: 
                res.append(levelVal)
            else:
                res.append(levelVal[::-1])
            flag *= -1
        return res

        
# @lc code=end

