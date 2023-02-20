#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 1
            elif not root.left or not root.right:
                return 1 + max(dfs(root.left), dfs(root.right))
            else:
                return 1+ min(dfs(root.left), dfs(root.right))
        def bfs(root):
            if not root:
                return 0
            queue = collections.deque([(root, 1)])
            while queue:
                node, level = queue.popleft()
                if node:
                    if not node.left and not node.right:
                        return level
                    else:
                        queue.append((node.left, level+1))
                        queue.append((node.right, level+1))
        return bfs(root)
            
            

        
# @lc code=end

