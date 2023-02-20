#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:return
            l = dfs(root.left)
            r = dfs(root.right)   
            root.left, root.right = r, l
            return root
         
            '''
            '''



        def bfs(root):
            if not root:
                return
            q = [root]
            while q:
                temp = q.pop(0)
                temp.left, temp.right = temp.right, temp.left
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            return root
        return bfs(root)
                

        
# @lc code=end

